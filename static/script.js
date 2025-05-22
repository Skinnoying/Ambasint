const form = document.getElementById('checkForm');
const loading = document.getElementById('loading');
const submitBtn = document.getElementById('submitBtn');
const input = document.getElementById('usernameInput');

form.addEventListener('submit', () => {
  submitBtn.disabled = true;
  loading.style.display = 'flex';
});

input.addEventListener('input', () => {
  if (submitBtn.disabled) {
    submitBtn.disabled = false;
    loading.style.display = 'none';
  }
});

console.log("Username Checker loaded");
