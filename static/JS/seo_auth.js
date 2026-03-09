/**
 * SEO & Accessibility Optimized Auth Logic
 * Focus: Lightweight, Accessible, Semantic validation
 */

document.addEventListener('DOMContentLoaded', () => {

    // Redirect if already logged in (UX best practice)
    if (localStorage.getItem('token')) {
        window.location.href = '/';
    }

    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', handleFormSubmit);
    }

    // Initialize Password Toggles
    document.querySelectorAll('.password-toggle').forEach(btn => {
        btn.addEventListener('click', togglePasswordVisibility);
    });

    // Initialize Real-time Validation
    document.querySelectorAll('.form-input').forEach(input => {
        input.addEventListener('blur', validateInput);
        input.addEventListener('input', () => {
            // Clear error on generic input
            if (input.getAttribute('aria-invalid') === 'true') {
                clearError(input);
            }

            // Allow specialized handlers (like password strength)
            if (input.id === 'password' && document.getElementById('strength-bar')) {
                updatePasswordStrength(input.value);
            }
        });
    });
});

/**
 * Handles form submission with accessibility in mind
 */
async function handleFormSubmit(e) {
    e.preventDefault();
    const form = e.target;
    const submitBtn = form.querySelector('button[type="submit"]');
    const originalBtnText = submitBtn.innerHTML;
    const messageContainer = document.getElementById('global-message');

    // 1. Client-side Validation
    let isValid = true;
    form.querySelectorAll('.form-input[required]').forEach(input => {
        if (!validateInput({ target: input })) {
            isValid = false;
        }
    });

    if (!isValid) {
        // Accessibility: Focus first invalid input
        const firstError = form.querySelector('[aria-invalid="true"]');
        if (firstError) firstError.focus();
        return;
    }

    // 2. UX: Loading State
    setLoading(submitBtn, true);
    if (messageContainer) messageContainer.classList.remove('error', 'success', 'visible');

    // 3. Prepare Data
    const formData = new FormData(form);

    try {
        const action = form.getAttribute('action') || window.location.href;
        // Handle Django URL patterns if necessary, though fetch handles relative paths
        // Assuming action is set in HTML form attribute

        const response = await fetch(action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            }
        });

        const data = await response.json();

        if (data.status === 'success') {
            // Success
            if (data.token) localStorage.setItem('token', data.token);

            showGlobalMessage('Success! Redirecting...', 'success');

            // Delay for UX reading time
            setTimeout(() => {
                window.location.href = '/'; // Go to homepage
            }, 1000);

        } else if (data.status === 'student already exists') {
            showGlobalMessage('That username is already taken. Please try another.', 'error');
            const usernameInput = document.getElementById('username');
            if (usernameInput) {
                setError(usernameInput, 'Username already taken');
                usernameInput.focus();
            }
        } else {
            showGlobalMessage(data.status || 'Authentication failed. Please check your credentials.', 'error');
        }

    } catch (error) {
        console.error('Submission error:', error);
        showGlobalMessage('A network error occurred. Please try again later.', 'error');
    } finally {
        setLoading(submitBtn, false, originalBtnText);
    }
}

/**
 * Toggles password visibility with accessible button state
 */
function togglePasswordVisibility(e) {
    const btn = e.currentTarget;
    const input = document.getElementById(btn.getAttribute('aria-controls'));
    const icon = btn.querySelector('.icon');

    if (input.type === 'password') {
        input.type = 'text';
        btn.setAttribute('aria-label', 'Hide password');
        btn.innerHTML = `
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"></path><line x1="1" y1="1" x2="23" y2="23"></line></svg>
        `;
    } else {
        input.type = 'password';
        btn.setAttribute('aria-label', 'Show password');
        btn.innerHTML = `
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg>
        `;
    }
}

/**
 * Accessibility-friendly Input Validation
 */
function validateInput(e) {
    const input = e.target;
    const value = input.value.trim();

    if (input.hasAttribute('required') && !value) {
        setError(input, 'This field is required');
        return false;
    }

    if (input.type === 'email' && value) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(value)) {
            setError(input, 'Please enter a valid email address');
            return false;
        }
    }

    if (input.id === 'password' && input.form.id === 'register-form') {
        if (value.length < 8) {
            setError(input, 'Password must be at least 8 characters');
            return false;
        }
    }

    clearError(input);
    return true;
}

function setError(input, message) {
    const errorId = input.getAttribute('aria-describedby');
    const errorEl = document.getElementById(errorId);

    input.setAttribute('aria-invalid', 'true');
    if (errorEl) {
        errorEl.textContent = message;
        errorEl.classList.add('visible');
    }
}

function clearError(input) {
    const errorId = input.getAttribute('aria-describedby');
    const errorEl = document.getElementById(errorId);

    input.setAttribute('aria-invalid', 'false');
    if (errorEl) {
        errorEl.textContent = '';
        errorEl.classList.remove('visible');
    }
}

function showGlobalMessage(text, type) {
    const msg = document.getElementById('global-message');
    if (!msg) return;

    msg.textContent = text;
    msg.className = `form-group message ${type}`; // reset classes
    msg.style.display = 'block';

    // Style directly for simplicity if css helper classes correspond
    if (type === 'error') msg.style.color = '#dc2626';
    if (type === 'success') msg.style.color = '#16a34a';
}

function setLoading(btn, isLoading, originalText = '') {
    if (isLoading) {
        btn.disabled = true;
        btn.innerHTML = `<div class="spinner"></div> Processing...`;
    } else {
        btn.disabled = false;
        btn.innerHTML = originalText;
    }
}

function updatePasswordStrength(password) {
    const bar = document.getElementById('strength-bar');
    if (!bar) return;

    let strength = 0;
    if (password.length >= 8) strength += 1;
    if (password.match(/[A-Z]/)) strength += 1;
    if (password.match(/[0-9]/)) strength += 1;
    if (password.match(/[^a-zA-Z0-9]/)) strength += 1;

    const width = (strength / 4) * 100;
    bar.style.width = `${width}%`;

    if (strength <= 1) bar.style.backgroundColor = '#dc2626'; // Red
    else if (strength <= 3) bar.style.backgroundColor = '#d97706'; // Orange
    else bar.style.backgroundColor = '#16a34a'; // Green
}
