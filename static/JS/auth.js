/**
 * Authentication Utilities
 * Provides form validation, password strength checking, and helper functions
 */

// Password strength calculator
function checkPasswordStrength(password) {
    let strength = 0;
    const feedback = [];

    if (password.length >= 8) strength++;
    else feedback.push('At least 8 characters');

    if (/[a-z]/.test(password)) strength++;
    else feedback.push('Lowercase letter');

    if (/[A-Z]/.test(password)) strength++;
    else feedback.push('Uppercase letter');

    if (/[0-9]/.test(password)) strength++;
    else feedback.push('Number');

    if (/[^a-zA-Z0-9]/.test(password)) strength++;
    else feedback.push('Special character');

    const levels = ['weak', 'weak', 'medium', 'medium', 'strong', 'strong'];
    return {
        level: levels[strength],
        feedback: feedback,
        score: strength
    };
}

// Update password strength UI
function updatePasswordStrength(password, barElement, textElement) {
    const result = checkPasswordStrength(password);
    
    barElement.className = `password-strength-bar ${result.level}`;
    
    if (password.length === 0) {
        barElement.className = 'password-strength-bar';
        textElement.textContent = '';
    } else {
        const text = result.level.charAt(0).toUpperCase() + result.level.slice(1);
        textElement.textContent = `${text} password${result.feedback.length ? ' - Missing: ' + result.feedback.join(', ') : ''}`;
    }
}

// Email validation
function isValidEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

// Show error message
function showMessage(messageElement, text, type = 'error') {
    messageElement.textContent = text;
    messageElement.className = `message ${type}`;
    messageElement.style.display = 'block';
    
    // Auto-hide success messages after 3 seconds
    if (type === 'success') {
        setTimeout(() => {
            messageElement.style.display = 'none';
        }, 3000);
    }
}

// Hide message
function hideMessage(messageElement) {
    messageElement.style.display = 'none';
}

// Toggle password visibility
function togglePasswordVisibility(inputElement, iconElement) {
    if (inputElement.type === 'password') {
        inputElement.type = 'text';
        iconElement.textContent = '👁️';
    } else {
        inputElement.type = 'password';
        iconElement.textContent = '👁️‍🗨️';
    }
}

// Set button loading state
function setButtonLoading(button, isLoading) {
    if (isLoading) {
        button.classList.add('loading');
        button.disabled = true;
        button.dataset.originalText = button.textContent;
        button.textContent = '';
    } else {
        button.classList.remove('loading');
        button.disabled = false;
        button.textContent = button.dataset.originalText || button.textContent;
    }
}

// Check if user is already logged in
function isUserLoggedIn() {
    return localStorage.getItem('token') !== null;
}

// Redirect if already logged in
function redirectIfLoggedIn(url) {
    if (isUserLoggedIn()) {
        console.log('User already logged in, redirecting...');
        window.location.href = url;
    }
}

// Export functions
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        checkPasswordStrength,
        updatePasswordStrength,
        isValidEmail,
        showMessage,
        hideMessage,
        togglePasswordVisibility,
        setButtonLoading,
        isUserLoggedIn,
        redirectIfLoggedIn
    };
}
