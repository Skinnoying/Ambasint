from flask import Flask, render_template, request
from checker.hybrid_checker import check_username
from checker.platforms import load_platforms

app = Flask(__name__)

platforms = load_platforms()

@app.route("/", methods=["GET", "POST"])
def index():
    results = None
    username = None
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        if username:
            results = check_username(username)

    return render_template("index.html", results=results, username=username, platforms=platforms)

if __name__ == "__main__":
    print(f"Loaded {len(platforms)} platforms from data.json")
    app.run(debug=True)
