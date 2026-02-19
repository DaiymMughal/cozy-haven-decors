# Quick Setup Guide for Your Affiliate Website

## 🚀 Get Your Site Running in 5 Minutes

### Prerequisites
- Windows PC
- Python 3.8 or higher installed
- Internet connection

---

## Step 1: Install Python (if not already installed)

1. Go to [python.org/downloads](https://www.python.org/downloads/)
2. Download Python 3.11 or later
3. **IMPORTANT**: Check "Add Python to PATH" during installation
4. Click "Install Now"
5. Verify installation:
   ```powershell
   python --version
   ```

---

## Step 2: Install Requirements

Open PowerShell in the project folder and run:

```powershell
cd "c:\Users\Rayyan Tech\OneDrive\Desktop\Pinterest\Affiliate Website"
pip install -r requirements.txt
```

This will install Flask and all necessary dependencies.

---

## Step 3: Customize Your Website

### Edit config.py

Open `config.py` and customize:

```python
# Your Information
SITE_NAME = "Your Site Name Here"
YOUR_NAME = "Your Name"
YOUR_EMAIL = "your.email@gmail.com"

# Social Media
PINTEREST_URL = "https://pinterest.com/yourprofile"

# Affiliate Links (IMPORTANT!)
AFFILIATE_LINKS = {
    'legendary_marketer': 'https://your-affiliate-link-here.com',
    'wealthy_affiliate': 'https://your-affiliate-link-here.com',
    'clickfunnels': 'https://your-affiliate-link-here.com',
}
```

### Add Your Affiliate Links

Replace ALL instances of `https://example.com/` with your real affiliate links in:
- [config.py](config.py)
- [app.py](app.py) (in the BLOG_POSTS and FEATURED_PRODUCTS sections)

---

## Step 4: Run Your Website

### Option A: Double-click run.bat
Just double-click the `run.bat` file - it will:
- Check Python installation
- Install/update requirements
- Start the server automatically

### Option B: Manual command
```powershell
python app.py
```

### Access Your Site
Open your browser and go to:
```
http://localhost:5000
```

---

## Step 5: Add Content

### Add Blog Posts

Edit `app.py` and add to the `BLOG_POSTS` list:

```python
{
    'id': 7,
    'title': 'Your New Blog Post Title',
    'slug': 'your-new-blog-post-title',
    'excerpt': 'Brief description of your post...',
    'image': 'https://images.unsplash.com/photo-xxxxx?w=800',
    'category': 'Make Money Online',
    'date': '2026-01-30',
    'read_time': '8 min read',
    'affiliate_link': 'https://your-affiliate-link.com'
}
```

### Get Free Images

Use these sites for free, high-quality images:
- [Unsplash](https://unsplash.com) - Copy image URL
- [Pexels](https://pexels.com) - Copy image URL
- [Pixabay](https://pixabay.com) - Copy image URL

---

## Step 6: Customize Design

### Change Colors

Edit `static/css/style.css` at the top:

```css
:root {
    --primary-color: #6366f1;    /* Main color */
    --secondary-color: #8b5cf6;  /* Accent color */
    --success-color: #10b981;    /* Success messages */
}
```

Try these color combinations:
- **Blue Theme**: #2563eb and #3b82f6
- **Purple Theme**: #7c3aed and #a855f7
- **Green Theme**: #059669 and #10b981
- **Pink Theme**: #db2777 and #ec4899

### Change Site Name & Logo

Edit `templates/index.html` (and other template files):
```html
<a href="/" class="logo">
    <i class="fas fa-chart-line"></i>  <!-- Change icon -->
    <span>Your Site Name</span>        <!-- Change name -->
</a>
```

Find more icons at [FontAwesome](https://fontawesome.com/icons)

---

## Step 7: Set Up Email Capture

### Free Email Services:

#### Option 1: ConvertKit (Recommended)
1. Sign up at [convertkit.com](https://convertkit.com) (free up to 1000 subscribers)
2. Create a form
3. Copy API key and form ID
4. Add to `config.py`:
   ```python
   CONVERTKIT_API_KEY = "your_api_key"
   CONVERTKIT_FORM_ID = "your_form_id"
   ```

#### Option 2: Mailchimp
1. Sign up at [mailchimp.com](https://mailchimp.com) (free up to 500 subscribers)
2. Create an audience
3. Get API key and list ID
4. Add to `config.py`:
   ```python
   MAILCHIMP_API_KEY = "your_api_key"
   MAILCHIMP_LIST_ID = "your_list_id"
   ```

---

## Step 8: Test Everything

### Checklist:
- [ ] Homepage loads correctly
- [ ] All navigation links work
- [ ] Blog posts display properly
- [ ] Resources page shows products
- [ ] Mobile view looks good (resize browser)
- [ ] All affiliate links work (click to test)
- [ ] Email forms display (integration comes later)

---

## Step 9: Create Pinterest Pins

### Using Canva (Free):
1. Sign up at [canva.com](https://canva.com)
2. Search "Pinterest Pin" templates
3. Customize with your blog post titles
4. Download as PNG
5. Upload to Pinterest with link to your website

### Pin Specs:
- Size: 1000 x 1500 pixels (2:3 ratio)
- Format: PNG or JPG
- Text: Large, bold, readable
- Colors: Eye-catching, on-brand

---

## Step 10: Go Live (Deploy)

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions.

### Free Hosting Options:
- PythonAnywhere (free tier)
- Replit (free tier)
- Railway (free trial)

### Paid Hosting (Recommended):
- DigitalOcean ($5/month)
- Heroku ($7/month)
- Vercel (free for personal)

---

## 🆘 Troubleshooting

### "Python is not recognized"
- Reinstall Python
- Make sure to check "Add to PATH" during installation
- Restart your computer

### "Module not found" error
```powershell
pip install --upgrade -r requirements.txt
```

### Site won't start
```powershell
# Check if port 5000 is busy
netstat -ano | findstr :5000

# Try a different port
# Edit app.py, change last line to:
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Changes not showing
- Hard refresh browser: Ctrl + F5
- Clear browser cache
- Restart Flask server

---

## 📚 Next Steps

1. **Create Content** - Write 10-15 blog posts
2. **Design Pins** - Create 50+ Pinterest pins
3. **Start Pinning** - Post 5-10 pins daily
4. **Build Email List** - Offer a free lead magnet
5. **Track Analytics** - Add Google Analytics
6. **Apply for Programs** - Join affiliate networks
7. **Deploy Site** - Put it online with a custom domain

---

## 💡 Quick Tips

- **Content First**: Focus on 10 great blog posts before worrying about design
- **Consistency**: Post to Pinterest daily for best results
- **SEO**: Use keywords in titles, descriptions, URLs
- **Email List**: Your most valuable asset - build it from day 1
- **Patience**: Typically takes 30-60 days to see significant traffic

---

## 🎯 Your First Week Plan

### Day 1-2: Setup
- Install and customize website
- Add your affiliate links
- Test everything locally

### Day 3-4: Content
- Write 3 blog posts
- Find/create images
- Add posts to website

### Day 5-6: Pinterest
- Create 15 pin designs (3 per post)
- Set up Pinterest business account
- Link to your website

### Day 7: Launch
- Deploy website online
- Start pinning to Pinterest
- Join affiliate programs

---

**Need more help?** Check out:
- [README.md](README.md) - Complete documentation
- [DEPLOYMENT.md](DEPLOYMENT.md) - Deployment guide
- [config.py](config.py) - Configuration options

**You've got this! 🚀**
