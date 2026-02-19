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

# Featured affiliate products from Amazon
FEATURED_PRODUCTS = [
    {
        'title': 'Modern Throw Pillow Set',
        'description': 'Set of 4 velvet throw pillows with inserts. Perfect for sofas and beds.',
        'price': '$29.99',
        'rating': 4.7,
        'image': 'https://images.unsplash.com/photo-1584100936595-c0654b55a2e2?w=400',
        'link': 'https://www.amazon.com/s?k=throw+pillows',
        'reviews': '12,458'
    },
    {
        'title': 'Boho Macrame Wall Hanging',
        'description': 'Handwoven macrame wall decor. Adds texture and warmth to any room.',
        'price': '$24.99',
        'rating': 4.8,
        'image': 'https://images.unsplash.com/photo-1615876063272-e3c08fe576a8?w=400',
        'link': 'https://www.amazon.com/s?k=macrame+wall+hanging',
        'reviews': '8,932'
    },
    {
        'title': 'Smart LED Strip Lights',
        'description': 'WiFi-enabled color-changing LED strips. App and voice control compatible.',
        'price': '$19.99',
        'rating': 4.6,
        'image': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=400',
        'link': 'https://www.amazon.com/s?k=led+strip+lights',
        'reviews': '45,231'
    },
    {
        'title': 'Ceramic Vase Set',
        'description': 'Set of 3 modern white ceramic vases. Perfect for flowers or standalone decor.',
        'price': '$34.99',
        'rating': 4.9,
        'image': 'https://images.unsplash.com/photo-1578500494198-246f612d3b3d?w=400',
        'link': 'https://www.amazon.com/s?k=ceramic+vase',
        'reviews': '3,421'
    },
    {
        'title': 'Faux Eucalyptus Plant',
        'description': 'Lifelike artificial eucalyptus in decorative pot. No maintenance required!',
        'price': '$22.99',
        'rating': 4.7,
        'image': 'https://images.unsplash.com/photo-1585567370656-2ebcf8f4e498?w=400',
        'link': 'https://www.amazon.com/s?k=faux+plants',
        'reviews': '7,654'
    },
    {
        'title': 'Gold Storage Baskets',
        'description': 'Set of 3 woven storage baskets with handles. Stylish and functional.',
        'price': '$39.99',
        'rating': 4.8,
        'image': 'https://images.unsplash.com/photo-1585562835530-d4b8fe022e9d?w=400',
        'link': 'https://www.amazon.com/s?k=decorative+baskets',
        'reviews': '9,123'
    }
]

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
