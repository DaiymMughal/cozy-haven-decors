// ========================================
// PINTEREST AFFILIATE WEBSITE - JAVASCRIPT
// Interactivity & Conversion Optimization
// ========================================

// Wait for DOM to load
document.addEventListener('DOMContentLoaded', function() {
    
    // === MOBILE NAVIGATION ===
    const navToggle = document.getElementById('navToggle');
    const navMenu = document.getElementById('navMenu');
    
    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
        });
        
        // Close menu when clicking outside
        document.addEventListener('click', function(event) {
            if (!navToggle.contains(event.target) && !navMenu.contains(event.target)) {
                navMenu.classList.remove('active');
            }
        });
    }
    
    // === BACK TO TOP BUTTON ===
    const backToTopBtn = document.getElementById('backToTop');
    
    if (backToTopBtn) {
        window.addEventListener('scroll', function() {
            if (window.pageYOffset > 300) {
                backToTopBtn.classList.add('visible');
            } else {
                backToTopBtn.classList.remove('visible');
            }
        });
        
        backToTopBtn.addEventListener('click', function() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }
    
    // === EMAIL FORM HANDLERS ===
    
    // Main email form
    const emailForm = document.getElementById('emailForm');
    if (emailForm) {
        emailForm.addEventListener('submit', handleEmailSubmit);
    }
    
    // Sidebar email form
    const sidebarEmailForm = document.getElementById('sidebarEmailForm');
    if (sidebarEmailForm) {
        sidebarEmailForm.addEventListener('submit', handleEmailSubmit);
    }
    
    // Post email form
    const postEmailForm = document.getElementById('postEmailForm');
    if (postEmailForm) {
        postEmailForm.addEventListener('submit', handleEmailSubmit);
    }
    
    // Footer email forms
    const footerEmailForms = document.querySelectorAll('.footer-email-form');
    footerEmailForms.forEach(form => {
        form.addEventListener('submit', handleEmailSubmit);
    });
    
    // Email submission handler
    async function handleEmailSubmit(e) {
        e.preventDefault();
        
        const form = e.target;
        const emailInput = form.querySelector('input[type="email"]');
        const submitBtn = form.querySelector('button[type="submit"]');
        const email = emailInput.value.trim();
        
        // Validate email
        if (!isValidEmail(email)) {
            showMessage(form, 'Please enter a valid email address.', 'error');
            return;
        }
        
        // Disable button and show loading state
        const originalBtnText = submitBtn.innerHTML;
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Subscribing...';
        
        try {
            // Send to server
            const response = await fetch('/subscribe', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ email: email })
            });
            
            const data = await response.json();
            
            if (data.success) {
                showMessage(form, '🎉 Success! Check your email for your free resources.', 'success');
                emailInput.value = '';
                
                // Track conversion (Google Analytics, Facebook Pixel, etc.)
                trackConversion('email_signup', email);
            } else {
                showMessage(form, data.message || 'Something went wrong. Please try again.', 'error');
            }
        } catch (error) {
            console.error('Subscription error:', error);
            showMessage(form, 'Network error. Please check your connection and try again.', 'error');
        } finally {
            // Re-enable button
            submitBtn.disabled = false;
            submitBtn.innerHTML = originalBtnText;
        }
    }
    
    // Email validation
    function isValidEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }
    
    // Show message to user
    function showMessage(form, message, type) {
        // Remove any existing messages
        const existingMsg = form.querySelector('.form-message');
        if (existingMsg) {
            existingMsg.remove();
        }
        
        // Create new message
        const msgDiv = document.createElement('div');
        msgDiv.className = `form-message ${type}`;
        msgDiv.textContent = message;
        msgDiv.style.cssText = `
            margin-top: 1rem;
            padding: 0.875rem 1.25rem;
            border-radius: 0.5rem;
            font-weight: 600;
            animation: fadeIn 0.3s ease;
            ${type === 'success' ? 
                'background: #d1fae5; color: #065f46;' : 
                'background: #fee2e2; color: #991b1b;'}
        `;
        
        form.appendChild(msgDiv);
        
        // Auto-remove after 5 seconds
        setTimeout(() => {
            msgDiv.style.opacity = '0';
            setTimeout(() => msgDiv.remove(), 300);
        }, 5000);
    }
    
    // === CONVERSION TRACKING ===
    function trackConversion(eventName, value) {
        // Google Analytics 4
        if (typeof gtag !== 'undefined') {
            gtag('event', eventName, {
                'value': value
            });
        }
        
        // Facebook Pixel
        if (typeof fbq !== 'undefined') {
            fbq('track', 'Lead', {
                content_name: eventName
            });
        }
        
        // Console log for debugging
        console.log('Conversion tracked:', eventName, value);
    }
    
    // === AFFILIATE LINK TRACKING ===
    document.querySelectorAll('a[href*="example.com"]').forEach(link => {
        link.addEventListener('click', function(e) {
            const linkUrl = this.href;
            const linkText = this.textContent.trim();
            
            // Track affiliate click
            trackConversion('affiliate_click', linkText);
            
            console.log('Affiliate link clicked:', linkUrl);
        });
    });
    
    // === SMOOTH SCROLL FOR ANCHOR LINKS ===
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href !== '#' && href !== '#0') {
                const target = document.querySelector(href);
                if (target) {
                    e.preventDefault();
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });
    
    // === LAZY LOADING IMAGES ===
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    if (img.dataset.src) {
                        img.src = img.dataset.src;
                        img.removeAttribute('data-src');
                        observer.unobserve(img);
                    }
                }
            });
        });
        
        document.querySelectorAll('img[data-src]').forEach(img => {
            imageObserver.observe(img);
        });
    }
    
    // === FADE IN ON SCROLL ANIMATION ===
    const fadeElements = document.querySelectorAll('.fade-in');
    
    if (fadeElements.length > 0 && 'IntersectionObserver' in window) {
        const fadeObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, {
            threshold: 0.1
        });
        
        fadeElements.forEach(el => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(20px)';
            el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            fadeObserver.observe(el);
        });
    }
    
    // === COPY TO CLIPBOARD (for sharing links) ===
    function copyToClipboard(text) {
        navigator.clipboard.writeText(text).then(() => {
            console.log('Copied to clipboard:', text);
        }).catch(err => {
            console.error('Failed to copy:', err);
        });
    }
    
    // === READING PROGRESS BAR (for blog posts) ===
    const progressBar = document.createElement('div');
    progressBar.id = 'reading-progress';
    progressBar.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 0%;
        height: 4px;
        background: linear-gradient(90deg, #6366f1, #8b5cf6);
        z-index: 9999;
        transition: width 0.1s ease;
    `;
    
    // Only add to blog post pages
    if (document.querySelector('.post-article')) {
        document.body.appendChild(progressBar);
        
        window.addEventListener('scroll', () => {
            const windowHeight = window.innerHeight;
            const documentHeight = document.documentElement.scrollHeight - windowHeight;
            const scrolled = window.pageYOffset;
            const progress = (scrolled / documentHeight) * 100;
            
            progressBar.style.width = progress + '%';
        });
    }
    
    // === PINTEREST HOVER PIN IT BUTTON ===
    // Add "Pin It" button on image hover
    document.querySelectorAll('.post-featured-image img, .post-body img').forEach(img => {
        const wrapper = document.createElement('div');
        wrapper.style.position = 'relative';
        wrapper.style.display = 'inline-block';
        wrapper.style.width = '100%';
        
        img.parentNode.insertBefore(wrapper, img);
        wrapper.appendChild(img);
        
        const pinBtn = document.createElement('a');
        pinBtn.className = 'pinterest-pin-btn';
        pinBtn.href = `https://pinterest.com/pin/create/button/?url=${encodeURIComponent(window.location.href)}&media=${encodeURIComponent(img.src)}&description=${encodeURIComponent(document.title)}`;
        pinBtn.target = '_blank';
        pinBtn.rel = 'noopener';
        pinBtn.innerHTML = '<i class="fab fa-pinterest"></i> Pin It';
        pinBtn.style.cssText = `
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: #e60023;
            color: white;
            padding: 0.75rem 1.5rem;
            border-radius: 0.5rem;
            font-weight: 600;
            text-decoration: none;
            opacity: 0;
            transition: opacity 0.3s ease;
            z-index: 10;
        `;
        
        wrapper.appendChild(pinBtn);
        
        wrapper.addEventListener('mouseenter', () => {
            pinBtn.style.opacity = '1';
        });
        
        wrapper.addEventListener('mouseleave', () => {
            pinBtn.style.opacity = '0';
        });
    });
    
    // === LOCAL STORAGE FOR PREFERENCES ===
    // Remember user preferences (e.g., dismissed banners)
    function savePreference(key, value) {
        try {
            localStorage.setItem(key, JSON.stringify(value));
        } catch (e) {
            console.error('Failed to save preference:', e);
        }
    }
    
    function getPreference(key) {
        try {
            const value = localStorage.getItem(key);
            return value ? JSON.parse(value) : null;
        } catch (e) {
            console.error('Failed to get preference:', e);
            return null;
        }
    }
    
    // === PRINT FUNCTIONALITY ===
    function printPage() {
        window.print();
    }
    
    // === SHARE FUNCTIONALITY ===
    if (navigator.share) {
        // Modern Web Share API (mobile)
        document.querySelectorAll('.share-native').forEach(btn => {
            btn.addEventListener('click', async () => {
                try {
                    await navigator.share({
                        title: document.title,
                        text: document.querySelector('meta[name="description"]')?.content || '',
                        url: window.location.href
                    });
                } catch (err) {
                    console.log('Share cancelled or failed:', err);
                }
            });
        });
    }
    
    console.log('🚀 Affiliate website loaded successfully!');
});

// === EXTERNAL LINK WARNING (optional) ===
document.addEventListener('click', function(e) {
    const link = e.target.closest('a');
    
    if (link && link.hostname !== window.location.hostname && link.target === '_blank') {
        // You can add a confirmation dialog here if desired
        // For affiliate sites, we usually don't want to interrupt the flow
        console.log('External link clicked:', link.href);
    }
});

// === PERFORMANCE MONITORING ===
window.addEventListener('load', function() {
    // Check page load time
    const perfData = window.performance.timing;
    const pageLoadTime = perfData.loadEventEnd - perfData.navigationStart;
    
    console.log('Page load time:', (pageLoadTime / 1000).toFixed(2) + 's');
    
    // Track slow loading pages
    if (pageLoadTime > 3000) {
        console.warn('Page loaded slowly. Consider optimization.');
    }
});
