/**
 * Interactive Effects for Authentication Pages
 * Adds mouse tracking, particles, ripples, and other dynamic effects
 */

// ========== Mouse Tracking Background ==========
function initMouseTracking() {
    const authPage = document.querySelector('.auth-page');
    if (!authPage) return;

    authPage.addEventListener('mousemove', (e) => {
        const { clientX, clientY } = e;
        const { innerWidth, innerHeight } = window;

        const xPercent = (clientX / innerWidth) * 100;
        const yPercent = (clientY / innerHeight) * 100;

        authPage.style.backgroundPosition = `${xPercent}% ${yPercent}%`;
    });
}

// ========== Interactive Particle System ==========
class ParticleSystem {
    constructor(container) {
        this.container = container;
        this.particles = [];
        this.canvas = null;
        this.ctx = null;
        this.init();
    }

    init() {
        // Create canvas
        this.canvas = document.createElement('canvas');
        this.canvas.style.position = 'absolute';
        this.canvas.style.top = '0';
        this.canvas.style.left = '0';
        this.canvas.style.width = '100%';
        this.canvas.style.height = '100%';
        this.canvas.style.pointerEvents = 'none';
        this.canvas.style.zIndex = '0';

        this.container.insertBefore(this.canvas, this.container.firstChild);
        this.ctx = this.canvas.getContext('2d');

        this.resize();
        window.addEventListener('resize', () => this.resize());

        // Create particles
        for (let i = 0; i < 50; i++) {
            this.particles.push(this.createParticle());
        }

        // Start animation
        this.animate();

        // Mouse interaction
        this.container.addEventListener('mousemove', (e) => this.onMouseMove(e));
    }

    resize() {
        this.canvas.width = this.container.offsetWidth;
        this.canvas.height = this.container.offsetHeight;
    }

    createParticle() {
        return {
            x: Math.random() * this.canvas.width,
            y: Math.random() * this.canvas.height,
            size: Math.random() * 3 + 1,
            speedX: (Math.random() - 0.5) * 0.5,
            speedY: (Math.random() - 0.5) * 0.5,
            opacity: Math.random() * 0.5 + 0.2
        };
    }

    onMouseMove(e) {
        const rect = this.canvas.getBoundingClientRect();
        const mouseX = e.clientX - rect.left;
        const mouseY = e.clientY - rect.top;

        this.particles.forEach(particle => {
            const dx = mouseX - particle.x;
            const dy = mouseY - particle.y;
            const dist = Math.sqrt(dx * dx + dy * dy);

            if (dist < 100) {
                particle.x -= dx / dist * 2;
                particle.y -= dy / dist * 2;
            }
        });
    }

    animate() {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

        this.particles.forEach(particle => {
            // Update position
            particle.x += particle.speedX;
            particle.y += particle.speedY;

            // Wrap around edges
            if (particle.x < 0) particle.x = this.canvas.width;
            if (particle.x > this.canvas.width) particle.x = 0;
            if (particle.y < 0) particle.y = this.canvas.height;
            if (particle.y > this.canvas.height) particle.y = 0;

            // Draw particle
            this.ctx.fillStyle = `rgba(255, 255, 255, ${particle.opacity})`;
            this.ctx.beginPath();
            this.ctx.arc(particle.x, particle.y, particle.size, 0, Math.PI * 2);
            this.ctx.fill();
        });

        requestAnimationFrame(() => this.animate());
    }
}

// ========== Ripple Effect ==========
function createRipple(button) {
    button.addEventListener('click', function (e) {
        const ripple = document.createElement('span');
        const rect = this.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height);
        const x = e.clientX - rect.left - size / 2;
        const y = e.clientY - rect.top - size / 2;

        ripple.style.width = ripple.style.height = size + 'px';
        ripple.style.left = x + 'px';
        ripple.style.top = y + 'px';
        ripple.classList.add('ripple');

        this.appendChild(ripple);

        ripple.addEventListener('animationend', () => {
            ripple.remove();
        });
    });
}

// ========== Shake Animation on Error ==========
function shakeElement(element) {
    element.classList.add('shake');
    setTimeout(() => {
        element.classList.remove('shake');
    }, 500);
}

// ========== Success Confetti ==========
function createConfetti() {
    const colors = ['#667eea', '#764ba2', '#f093fb', '#f5576c', '#51cf66', '#ffd93d'];
    const confettiCount = 50;

    for (let i = 0; i < confettiCount; i++) {
        const confetti = document.createElement('div');
        confetti.className = 'confetti';
        confetti.style.left = Math.random() * 100 + 'vw';
        confetti.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
        confetti.style.animationDelay = Math.random() * 0.3 + 's';
        confetti.style.animationDuration = (Math.random() * 2 + 2) + 's';

        document.body.appendChild(confetti);

        confetti.addEventListener('animationend', () => {
            confetti.remove();
        });
    }
}

// ========== Floating Label Animation ==========
function initFloatingLabels() {
    const inputs = document.querySelectorAll('.input-field');

    inputs.forEach(input => {
        const label = input.previousElementSibling;
        if (!label || !label.classList.contains('input-label')) return;

        input.addEventListener('focus', () => {
            label.style.transform = 'translateY(-2px) scale(1.05)';
            label.style.boxShadow = '0 4px 12px rgba(102, 126, 234, 0.4)';
        });

        input.addEventListener('blur', () => {
            label.style.transform = '';
            label.style.boxShadow = '';
        });
    });
}

// ========== Input Focus Glow Effect ==========
function initInputGlow() {
    const inputs = document.querySelectorAll('.input-field');

    inputs.forEach(input => {
        input.addEventListener('focus', () => {
            input.style.boxShadow = '0 0 25px rgba(102, 126, 234, 0.5), 0 0 50px rgba(118, 75, 162, 0.3)';
        });

        input.addEventListener('blur', () => {
            input.style.boxShadow = '';
        });
    });
}

// ========== Card Tilt Effect ==========
function initCardTilt() {
    const card = document.querySelector('.auth-card');
    if (!card) return;

    card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;

        const centerX = rect.width / 2;
        const centerY = rect.height / 2;

        const rotateX = (y - centerY) / 20;
        const rotateY = (centerX - x) / 20;

        card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
    });

    card.addEventListener('mouseleave', () => {
        card.style.transform = '';
    });
}

// ========== Typing Animation Helper ==========
function typeText(element, text, speed = 50) {
    let i = 0;
    element.textContent = '';

    const type = () => {
        if (i < text.length) {
            element.textContent += text.charAt(i);
            i++;
            setTimeout(type, speed);
        }
    };

    type();
}

// ========== Initialize All Effects ==========
function initInteractiveEffects() {
    // Mouse tracking
    initMouseTracking();

    // Particle system
    const authPage = document.querySelector('.auth-page');
    if (authPage) {
        new ParticleSystem(authPage);
    }

    // Ripple effects on buttons
    document.querySelectorAll('.auth-button').forEach(btn => {
        createRipple(btn);
    });

    // Floating labels
    initFloatingLabels();

    // Input glow
    initInputGlow();

    // Card tilt
    initCardTilt();
}

// Auto-initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initInteractiveEffects);
} else {
    initInteractiveEffects();
}

// Export for manual use
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        initMouseTracking,
        ParticleSystem,
        createRipple,
        shakeElement,
        createConfetti,
        initFloatingLabels,
        initInputGlow,
        initCardTilt,
        typeText,
        initInteractiveEffects
    };
}
