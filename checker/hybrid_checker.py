import asyncio
import aiohttp
import cloudscraper
from checker.platforms import load_platforms

platforms = load_platforms()

async def fetch_async(session, url):
    try:
        async with session.get(url, timeout=15) as response:
            text = await response.text()
            status = response.status
            return status, text
    except Exception:
        return None, None

async def check_username_async(username):
    results = {}

    async with aiohttp.ClientSession() as session:
        tasks = []
        for name, data in platforms.items():
            if not isinstance(data, dict):
                continue
            url = data["url"].format(username)
            tasks.append(fetch_async(session, url))

        responses = await asyncio.gather(*tasks)

        i = 0
        for name, data in platforms.items():
            if not isinstance(data, dict):
                continue
            status, text = responses[i]
            i += 1
            if status is None:
                results[name] = {"valid": False, "url": None}
                continue
            err_type = data.get("errorType")
            if err_type == "status_code":
                claimed = data.get("username_claimed")
                valid = (status != 404 and status != 403 and status != 400)
                if claimed:
                    valid = (status == 200)
                results[name] = {"valid": valid, "url": data["url"].format(username)}
            elif err_type == "message":
                error_msg = data.get("errorMsg")
                if isinstance(error_msg, list):
                    valid = True
                    for err in error_msg:
                        if err in text:
                            valid = False
                            break
                else:
                    valid = error_msg not in text
                results[name] = {"valid": valid, "url": data["url"].format(username)}
            else:
                results[name] = {"valid": (status == 200), "url": data["url"].format(username)}

    return results

def is_valid_profile(text, data):
    # Jika ada pesan error dalam bentuk list atau string
    error_msg = data.get("errorMsg")
    if error_msg:
        if isinstance(error_msg, list):
            for em in error_msg:
                if em in text:
                    return False
        elif isinstance(error_msg, str):
            if error_msg in text:
                return False

    # Cek apakah halaman mengandung username_claimed (user dummy)
    claimed = data.get("username_claimed")
    if claimed and claimed.lower() in text.lower():
        return False

    return True

# Contoh untuk fungsi sync checker (async sama saja tinggal disesuaikan)
def check_username_sync(username):
    scraper = cloudscraper.create_scraper()
    results = {}
    for name, data in platforms.items():
        if not isinstance(data, dict):
            continue
        url = data["url"].format(username)
        try:
            resp = scraper.get(url, timeout=15)
            status = resp.status_code
            text = resp.text
        except Exception:
            results[name] = {"valid": False, "url": None}
            continue

        err_type = data.get("errorType")

        if err_type == "status_code":
            if status == 200 and is_valid_profile(text, data):
                results[name] = {"valid": True, "url": url}
            else:
                results[name] = {"valid": False, "url": url}
        elif err_type == "message":
            if is_valid_profile(text, data):
                results[name] = {"valid": True, "url": url}
            else:
                results[name] = {"valid": False, "url": url}
        else:
            results[name] = {"valid": (status == 200), "url": url}
    return results

def check_username(username):
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    try:
        results = loop.run_until_complete(check_username_async(username))
    except Exception:
        results = check_username_sync(username)
    return results
