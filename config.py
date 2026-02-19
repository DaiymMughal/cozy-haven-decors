# Configuration file for your home decor affiliate website

# ============================================
# SITE INFORMATION
# ============================================
SITE_NAME = "Cozy Haven Decor"
SITE_TAGLINE = "Beautiful Home Decor from Amazon"
SITE_DESCRIPTION = "Transform your home with curated decor finds from Amazon. Discover styling guides, product recommendations, and inspiration for every room."

# ============================================
# YOUR INFORMATION
# ============================================
YOUR_NAME = "Your Name"
YOUR_EMAIL = "your.email@example.com"

# ============================================
# SOCIAL MEDIA LINKS
# ============================================
PINTEREST_URL = "https://pinterest.com/yourprofile"
FACEBOOK_URL = ""
INSTAGRAM_URL = ""
TWITTER_URL = ""
YOUTUBE_URL = ""

# ============================================
# AMAZON AFFILIATE SETTINGS
# Replace with your actual Amazon Associates tracking ID
# Sign up at: https://affiliate-program.amazon.com
# ============================================
AMAZON_ASSOCIATES_TAG = "cozyhaven20-20"  # Your Amazon Associates tracking ID

# Example Amazon product categories you can promote
AMAZON_CATEGORIES = {
    'throw_pillows': f'https://www.amazon.com/s?k=throw+pillows&tag={AMAZON_ASSOCIATES_TAG}',
    'wall_art': f'https://www.amazon.com/s?k=wall+art&tag={AMAZON_ASSOCIATES_TAG}',
    'home_decor': f'https://www.amazon.com/s?k=home+decor&tag={AMAZON_ASSOCIATES_TAG}',
    'lighting': f'https://www.amazon.com/s?k=decorative+lighting&tag={AMAZON_ASSOCIATES_TAG}',
    'plants': f'https://www.amazon.com/s?k=artificial+plants&tag={AMAZON_ASSOCIATES_TAG}',
}

# ============================================
# EMAIL MARKETING
# ============================================
# Add your email service API keys here
MAILCHIMP_API_KEY = ""
MAILCHIMP_LIST_ID = ""

# Or use ConvertKit
CONVERTKIT_API_KEY = ""
CONVERTKIT_FORM_ID = ""

# ============================================
# GOOGLE ANALYTICS (Optional)
# ============================================
GOOGLE_ANALYTICS_ID = ""  # Format: G-XXXXXXXXXX

# ============================================
# MONETIZATION
# ============================================
# Add your ad network IDs when approved
GOOGLE_ADSENSE_ID = ""
EZOIC_ID = ""
MEDIAVINE_ID = ""

# ============================================
# SEO SETTINGS
# ============================================
SITE_URL = "https://yoursite.com"  # Update when you have a domain
KEYWORDS = "make money online, passive income, affiliate marketing, side hustles, financial freedom"

# ============================================
# FLASK SETTINGS
# ============================================
SECRET_KEY = "change-this-to-random-secret-key-in-production"
DEBUG = True  # Set to False in production
