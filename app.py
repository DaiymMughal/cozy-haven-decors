from flask import Flask, render_template, request, jsonify, redirect, url_for
from datetime import datetime
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-this-in-production'

# Sample blog posts data (in real app, this would come from a database)
BLOG_POSTS = [
    {
        'id': 1,
        'title': '10 Must-Have Amazon Home Decor Items Under $50',
        'slug': '10-must-have-amazon-home-decor-under-50',
        'excerpt': 'Transform your space without breaking the bank! Discover our top picks for affordable yet stylish home decor from Amazon.',
        'image': 'https://images.unsplash.com/photo-1556228720-195a672e8a03?w=800',
        'category': 'Budget Decor',
        'date': '2026-02-15',
        'read_time': '8 min read',
        'affiliate_link': 'https://www.amazon.com/home-decor'
    },
    {
        'id': 2,
        'title': 'Bohemian Living Room Ideas: Complete Shopping Guide',
        'slug': 'bohemian-living-room-ideas-guide',
        'excerpt': 'Create your dream boho living room with our curated selection of Amazon decor. Step-by-step styling guide included!',
        'image': 'https://images.unsplash.com/photo-1556228453-efd6c1ff04f6?w=800',
        'category': 'Living Room',
        'date': '2026-02-12',
        'read_time': '12 min read',
        'affiliate_link': 'https://www.amazon.com/boho-decor'
    },
    {
        'id': 3,
        'title': 'Cozy Bedroom Makeover: Best Amazon Finds for 2026',
        'slug': 'cozy-bedroom-makeover-amazon-finds',
        'excerpt': 'Turn your bedroom into a cozy sanctuary with these highly-rated Amazon products. Perfect for any style!',
        'image': 'https://images.unsplash.com/photo-1616594039964-ae9021a400a0?w=800',
        'category': 'Bedroom',
        'date': '2026-02-10',
        'read_time': '10 min read',
        'affiliate_link': 'https://www.amazon.com/bedroom-decor'
    },
    {
        'id': 4,
        'title': 'Modern Minimalist Kitchen Essentials from Amazon',
        'slug': 'modern-minimalist-kitchen-essentials',
        'excerpt': 'Achieve that clean, minimalist kitchen aesthetic with our carefully selected Amazon products. Function meets style!',
        'image': 'https://images.unsplash.com/photo-1556911261-6bd341186b2f?w=800',
        'category': 'Kitchen',
        'date': '2026-02-08',
        'read_time': '9 min read',
        'affiliate_link': 'https://www.amazon.com/kitchen-organization'
    },
    {
        'id': 5,
        'title': 'Small Space Solutions: Amazon Decor That Maximizes Space',
        'slug': 'small-space-solutions-amazon',
        'excerpt': 'Living in a small apartment? These clever Amazon finds will help you maximize every inch while staying stylish.',
        'image': 'https://images.unsplash.com/photo-1556020685-ae41abfc9365?w=800',
        'category': 'Small Spaces',
        'date': '2026-02-05',
        'read_time': '11 min read',
        'affiliate_link': 'https://www.amazon.com/space-saving'
    },
    {
        'id': 6,
        'title': 'Wall Art & Gallery Wall Ideas: Amazon\'s Best Selections',
        'slug': 'wall-art-gallery-amazon',
        'excerpt': 'Create stunning gallery walls with affordable art from Amazon. Complete guide with layout tips and product recommendations.',
        'image': 'https://images.unsplash.com/photo-1513519245088-0e12902e35ca?w=800',
        'category': 'Wall Decor',
        'date': '2026-02-02',
        'read_time': '10 min read',
        'affiliate_link': 'https://www.amazon.com/wall-art'
    }
]

# ============================================
# YOUR FEATURED AMAZON PRODUCTS
# ============================================
# To add more products, copy the template at the bottom and fill in details
# Make sure each product link includes your tracking ID: cozyhaven20-20
# ============================================

FEATURED_PRODUCTS = [
    {
        'title': '2x6 Hallway Washable Runner Rug',
        'description': 'Non-slip washable runner rug perfect for hallways, kitchen, or entryway. Easy to clean and durable.',
        'price': '$39.99',
        'rating': 4.6,
        'image': 'https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?w=400',
        'link': 'https://www.amazon.com/dp/B0D89V1RX1?tag=cozyhaven20-20',
        'reviews': '2,847'
    },
    {
        'title': 'Adhesive Towel Holder Organizer',
        'description': 'Rustproof stainless steel adhesive organizer. No drilling required - perfect for bathroom or kitchen.',
        'price': '$16.99',
        'rating': 4.5,
        'image': 'https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=400',
        'link': 'https://www.amazon.com/dp/B0BLSCY6PR?tag=cozyhaven20-20',
        'reviews': '5,632'
    },
    {
        'title': 'Bedsure White Fleece Throw Blanket',
        'description': 'Ultra-soft fleece blanket perfect for cozy nights. Lightweight yet warm, great for sofas and beds.',
        'price': '$19.99',
        'rating': 4.7,
        'image': 'https://images.unsplash.com/photo-1631679706033-7b9be9e8c7e0?w=400',
        'link': 'https://www.amazon.com/dp/B0BPLB81LX?tag=cozyhaven20-20',
        'reviews': '18,456'
    },
]

# ============================================
# TEMPLATE - To add more products, copy this:
# ============================================
# {
#     'title': 'Product Name Here',
#     'description': 'Short description of the product. What makes it great?',
#     'price': '$00.00',
#     'rating': 4.5,
#     'image': 'PASTE_AMAZON_IMAGE_URL_HERE',
#     'link': 'https://www.amazon.com/dp/PRODUCT_ID?tag=cozyhaven20-20',
#     'reviews': '0,000'
# },

@app.route('/')
def home():
    """Homepage with featured content"""
    featured_posts = BLOG_POSTS[:3]
    return render_template('index.html', 
                         featured_posts=featured_posts,
                         featured_products=FEATURED_PRODUCTS)

@app.route('/blog')
def blog():
    """Blog listing page"""
    category = request.args.get('category', None)
    
    if category:
        filtered_posts = [p for p in BLOG_POSTS if p['category'] == category]
    else:
        filtered_posts = BLOG_POSTS
    
    categories = list(set([p['category'] for p in BLOG_POSTS]))
    
    return render_template('blog.html', 
                         posts=filtered_posts,
                         categories=categories,
                         selected_category=category)

@app.route('/blog/<slug>')
def blog_post(slug):
    """Individual blog post page"""
    post = next((p for p in BLOG_POSTS if p['slug'] == slug), None)
    
    if not post:
        return "Post not found", 404
    
    # Get related posts (same category)
    related_posts = [p for p in BLOG_POSTS 
                    if p['category'] == post['category'] 
                    and p['id'] != post['id']][:3]
    
    return render_template('post.html', 
                         post=post,
                         related_posts=related_posts)

@app.route('/resources')
def resources():
    """Resources and tools page"""
    return render_template('resources.html',
                         products=FEATURED_PRODUCTS)

@app.route('/start-here')
def start_here():
    """Getting started guide for beginners"""
    return render_template('start-here.html')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """Handle email subscription"""
    data = request.get_json()
    email = data.get('email', '')
    
    # In production, save to database or email service (Mailchimp, ConvertKit, etc.)
    # For now, just return success
    
    if email and '@' in email:
        # You would integrate with email service here
        return jsonify({
            'success': True,
            'message': 'Thanks for subscribing! Check your email for free resources.'
        })
    else:
        return jsonify({
            'success': False,
            'message': 'Please enter a valid email address.'
        }), 400

@app.route('/privacy')
def privacy():
    """Privacy policy page"""
    return render_template('privacy.html')

@app.route('/disclaimer')
def disclaimer():
    """Affiliate disclaimer page"""
    return render_template('disclaimer.html')

@app.errorhandler(404)
def page_not_found(e):
    """404 error handler"""
    return render_template('404.html'), 404

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') != 'production'
    app.run(debug=debug, host='0.0.0.0', port=port)
