#!/usr/bin/env python3

"""
Tidio Affiliate SEO Site Builder
High-Scale GitHub Pages Static Site Generator

Domain:
https://brightlane.github.io/tidio/

Affiliate:
https://affiliate.tidio.com/hdqdb2cqrrjp
"""

import json
import random
import shutil
from pathlib import Path
from datetime import datetime

# =========================================================
# CONFIG
# =========================================================

SITE_NAME = "Tidio AI Growth Hub"

DOMAIN = "https://brightlane.github.io/tidio"

AFFILIATE_URL = "https://affiliate.tidio.com/hdqdb2cqrrjp"

YEAR = datetime.now().year

TODAY = datetime.now().strftime("%Y-%m-%d")

# =========================================================
# CTA VARIATIONS
# =========================================================

CTAS = [
    "Start Using Tidio Free",
    "Boost Sales With AI Chat",
    "Automate Customer Support",
    "Launch Tidio Today",
    "Improve Website Conversion Rates",
    "Try Tidio AI Chatbots",
    "Grow Faster With Tidio",
]

# =========================================================
# BUYER INTENT PAGES
# =========================================================

PAGES = [
    {
        "slug": "index",
        "title": "Tidio Live Chat & AI Customer Support",
        "description": "Boost conversions using Tidio AI chatbots and live chat.",
        "keyword": "tidio live chat"
    },

    {
        "slug": "best-ai-chatbots",
        "title": "Best AI Chatbots For Small Business",
        "description": "Compare top AI chatbot platforms for customer support.",
        "keyword": "best ai chatbot"
    },

    {
        "slug": "tidio-vs-intercom",
        "title": "Tidio vs Intercom",
        "description": "Compare Tidio and Intercom features and pricing.",
        "keyword": "tidio vs intercom"
    },

    {
        "slug": "tidio-vs-zendesk",
        "title": "Tidio vs Zendesk",
        "description": "Which support platform is best for ecommerce?",
        "keyword": "tidio vs zendesk"
    },

    {
        "slug": "shopify-live-chat",
        "title": "Best Shopify Live Chat Apps",
        "description": "Top live chat apps for Shopify stores.",
        "keyword": "shopify live chat"
    },

    {
        "slug": "woocommerce-chatbot",
        "title": "Best WooCommerce Chatbot Plugins",
        "description": "Improve WooCommerce sales using AI chatbots.",
        "keyword": "woocommerce chatbot"
    },

    {
        "slug": "customer-support-automation",
        "title": "Customer Support Automation Guide",
        "description": "Reduce support costs using AI automation.",
        "keyword": "customer support automation"
    },

    {
        "slug": "reduce-cart-abandonment",
        "title": "Reduce Cart Abandonment With Live Chat",
        "description": "Recover abandoned carts using Tidio live chat.",
        "keyword": "reduce cart abandonment"
    }
]

# =========================================================
# INDUSTRY PAGES
# =========================================================

INDUSTRIES = [
    "law-firms",
    "real-estate",
    "dentists",
    "restaurants",
    "ecommerce",
    "saas",
    "agencies",
    "coaches",
    "consultants",
    "gyms"
]

# =========================================================
# BLOG TOPICS
# =========================================================

BLOG_TOPICS = [
    "How AI Chatbots Increase Ecommerce Revenue",
    "Best Live Chat Tools For Shopify",
    "How To Automate Customer Support",
    "Best AI Chatbot Software",
    "How To Improve Conversion Rates",
    "Benefits Of Live Chat Support",
    "Best Help Desk Software",
    "How To Reduce Cart Abandonment",
    "AI Customer Support Trends",
    "How Small Businesses Use AI Chatbots"
]

# =========================================================
# PATHS
# =========================================================

BASE_DIR = Path(__file__).parent

DIST_DIR = BASE_DIR / "dist"

ASSETS_DIR = DIST_DIR / "assets"

BLOG_DIR = DIST_DIR / "blog"

TAG_DIR = DIST_DIR / "tag"

# =========================================================
# CLEAN DIST
# =========================================================

if DIST_DIR.exists():
    shutil.rmtree(DIST_DIR)

DIST_DIR.mkdir()
ASSETS_DIR.mkdir()
BLOG_DIR.mkdir()
TAG_DIR.mkdir()

# =========================================================
# CSS
# =========================================================

STYLE = """
*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

body{
    background:#0f172a;
    color:#e2e8f0;
    font-family:Arial,sans-serif;
    line-height:1.7;
}

header{
    background:#111827;
    padding:20px 0;
    border-bottom:2px solid #06b6d4;
    position:sticky;
    top:0;
    z-index:999;
}

.container{
    width:92%;
    max-width:1200px;
    margin:auto;
}

.logo{
    font-size:2rem;
    color:#06b6d4;
    font-weight:bold;
}

nav{
    margin-top:15px;
}

nav a{
    color:#cbd5e1;
    text-decoration:none;
    margin-right:18px;
    font-weight:bold;
}

nav a:hover{
    color:#06b6d4;
}

.hero{
    text-align:center;
    padding:120px 20px;
    background:linear-gradient(to right,#111827,#1e293b);
}

.hero h1{
    font-size:3.5rem;
    color:#06b6d4;
    margin-bottom:20px;
}

.hero p{
    max-width:850px;
    margin:auto;
    margin-bottom:35px;
    font-size:1.2rem;
}

.button{
    display:inline-block;
    background:#06b6d4;
    color:white;
    padding:15px 30px;
    border-radius:6px;
    text-decoration:none;
    font-weight:bold;
}

.button:hover{
    background:#0891b2;
}

.section{
    padding:80px 0;
}

.card{
    background:#1e293b;
    padding:30px;
    border-radius:10px;
    border:1px solid #334155;
    margin-bottom:30px;
}

.card h2,
.card h3{
    color:#06b6d4;
    margin-bottom:15px;
}

.related a{
    display:block;
    color:#06b6d4;
    margin-bottom:10px;
}

table{
    width:100%;
    border-collapse:collapse;
    margin-top:20px;
}

th, td{
    border:1px solid #334155;
    padding:12px;
}

th{
    background:#111827;
}

footer{
    background:#020617;
    padding:40px 20px;
    text-align:center;
    border-top:2px solid #06b6d4;
}
"""

(ASSETS_DIR / "style.css").write_text(
    STYLE,
    encoding="utf-8"
)

# =========================================================
# NAVIGATION
# =========================================================

def build_nav():

    links = []

    for page in PAGES:

        file = (
            "index.html"
            if page["slug"] == "index"
            else f"{page['slug']}.html"
        )

        links.append(
            f'<a href="{file}">{page["title"]}</a>'
        )

    links.append('<a href="blog/index.html">Blog</a>')

    return "\n".join(links)

NAV = build_nav()

# =========================================================
# CTA
# =========================================================

def random_cta():
    return random.choice(CTAS)

# =========================================================
# RELATED LINKS
# =========================================================

def related_links(current_slug):

    pages = []

    for page in PAGES:

        if page["slug"] == current_slug:
            continue

        file = (
            "index.html"
            if page["slug"] == "index"
            else f"{page['slug']}.html"
        )

        pages.append(
            f'<a href="{file}">{page["title"]}</a>'
        )

    random.shuffle(pages)

    return "\n".join(pages[:5])

# =========================================================
# LONG CONTENT
# =========================================================

def generate_content(keyword):

    html = []

    for i in range(1, 9):

        html.append(f"""
        <div class="card">

        <h2>{keyword.title()} Guide {i}</h2>

        <p>
        Businesses increasingly use AI chatbots and live chat systems
        to improve customer engagement, automate support workflows,
        and increase website conversion rates.
        </p>

        <p>
        Tidio combines chatbot automation, help desk tools,
        AI customer support, and real-time messaging into
        one scalable customer communication platform.
        </p>

        <p>
        Ecommerce stores, SaaS companies, agencies, and small businesses
        use live chat software to increase sales and improve support efficiency.
        </p>

        <a class="button" href="{AFFILIATE_URL}">
        {random_cta()}
        </a>

        </div>
        """)

    return "\n".join(html)

# =========================================================
# FAQ SCHEMA
# =========================================================

FAQ_SCHEMA = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": "What is Tidio?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Tidio is an AI-powered live chat and customer support platform."
            }
        },
        {
            "@type": "Question",
            "name": "Does Tidio support AI chatbots?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Yes. Tidio includes AI chatbot automation."
            }
        },
        {
            "@type": "Question",
            "name": "Can Tidio increase conversion rates?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Live chat and chatbot automation can improve engagement and conversion rates."
            }
        }
    ]
}

# =========================================================
# TEMPLATE
# =========================================================

PAGE_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>{title}</title>

<meta name="description" content="{description}">

<meta name="keywords" content="{keyword}">

<link rel="canonical" href="{canonical}">

<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">

<link rel="stylesheet" href="assets/style.css">

<script type="application/ld+json">
{schema}
</script>

<script type="application/ld+json">
{faq_schema}
</script>

</head>

<body>

<header>

<div class="container">

<div class="logo">
{site_name}
</div>

<nav>
{navigation}
</nav>

</div>

</header>

<section class="hero">

<div class="container">

<h1>{title}</h1>

<p>{description}</p>

<a class="button" href="{affiliate}">
{cta}
</a>

</div>

</section>

<section class="section">

<div class="container">

<div class="card">

<h2>
Why Businesses Use Tidio
</h2>

<p>
Tidio combines AI chatbot automation, live chat,
customer support software, and ecommerce automation
into one scalable communication platform.
</p>

<a class="button" href="{affiliate}">
{cta}
</a>

</div>

<div class="card">

<h2>
Feature Comparison
</h2>

<table>

<tr>
<th>Feature</th>
<th>Tidio</th>
<th>Traditional Support</th>
</tr>

<tr>
<td>AI Chatbots</td>
<td>Yes</td>
<td>No</td>
</tr>

<tr>
<td>Live Chat</td>
<td>Yes</td>
<td>Limited</td>
</tr>

<tr>
<td>Automation</td>
<td>Advanced</td>
<td>Manual</td>
</tr>

<tr>
<td>24/7 Availability</td>
<td>Yes</td>
<td>No</td>
</tr>

</table>

</div>

{content}

<div class="card related">

<h2>
Related Guides
</h2>

{related_links}

</div>

<div class="card">

<h2>
Get AI Chat Tips
</h2>

<form>

<input
type="email"
placeholder="Enter your email"
style="padding:12px;width:100%;margin-bottom:15px;"
>

<button
style="padding:12px 24px;background:#06b6d4;color:white;border:none;"
>
Subscribe
</button>

</form>

</div>

</div>

</section>

<footer>

<p>
© {year} {site_name}
</p>

<p style="margin-top:20px;">
<a class="button" href="{affiliate}">
{cta}
</a>
</p>

</footer>

</body>

</html>
"""

# =========================================================
# GENERATE CORE PAGES
# =========================================================

all_urls = []

for page in PAGES:

    filename = (
        "index.html"
        if page["slug"] == "index"
        else f"{page['slug']}.html"
    )

    canonical = (
        DOMAIN + "/"
        if page["slug"] == "index"
        else f"{DOMAIN}/{page['slug']}.html"
    )

    all_urls.append(canonical)

    schema = json.dumps({
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": page["title"],
        "description": page["description"]
    }, indent=2)

    html = PAGE_TEMPLATE.format(
        title=page["title"],
        description=page["description"],
        keyword=page["keyword"],
        canonical=canonical,
        schema=schema,
        faq_schema=json.dumps(FAQ_SCHEMA, indent=2),
        site_name=SITE_NAME,
        navigation=NAV,
        affiliate=AFFILIATE_URL,
        cta=random_cta(),
        content=generate_content(page["keyword"]),
        related_links=related_links(page["slug"]),
        year=YEAR
    )

    (DIST_DIR / filename).write_text(
        html,
        encoding="utf-8"
    )

# =========================================================
# INDUSTRY PAGES
# =========================================================

for industry in INDUSTRIES:

    slug = f"live-chat-for-{industry}"

    title = f"Best Live Chat For {industry.replace('-', ' ').title()}"

    keyword = f"live chat for {industry.replace('-', ' ')}"

    filename = f"{slug}.html"

    canonical = f"{DOMAIN}/{filename}"

    all_urls.append(canonical)

    schema = json.dumps({
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": keyword
    }, indent=2)

    html = PAGE_TEMPLATE.format(
        title=title,
        description=f"Discover how AI chatbots help {industry.replace('-', ' ')} businesses improve customer support.",
        keyword=keyword,
        canonical=canonical,
        schema=schema,
        faq_schema=json.dumps(FAQ_SCHEMA, indent=2),
        site_name=SITE_NAME,
        navigation=NAV,
        affiliate=AFFILIATE_URL,
        cta=random_cta(),
        content=generate_content(keyword),
        related_links=related_links("index"),
        year=YEAR
    )

    (DIST_DIR / filename).write_text(
        html,
        encoding="utf-8"
    )

# =========================================================
# DAILY BLOG POSTS
# =========================================================

blog_links = []

for i in range(5):

    topic = random.choice(BLOG_TOPICS)

    slug = f"{TODAY}-{i}"

    filename = f"{slug}.html"

    canonical = f"{DOMAIN}/blog/{filename}"

    all_urls.append(canonical)

    blog_links.append(
        f'<li><a href="{filename}">{topic}</a></li>'
    )

    html = f"""
    <!DOCTYPE html>
    <html lang="en">

    <head>

    <meta charset="UTF-8">

    <title>{topic}</title>

    <link rel="stylesheet" href="../assets/style.css">

    </head>

    <body>

    <section class="hero">

    <div class="container">

    <h1>{topic}</h1>

    <p>
    Learn how AI chatbots and live chat software improve customer support.
    </p>

    <a class="button" href="{AFFILIATE_URL}">
    {random_cta()}
    </a>

    </div>

    </section>

    <section class="section">

    <div class="container">

    {generate_content(topic)}

    </div>

    </section>

    </body>

    </html>
    """

    (BLOG_DIR / filename).write_text(
        html,
        encoding="utf-8"
    )

# =========================================================
# BLOG INDEX
# =========================================================

BLOG_INDEX = f"""
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<title>Tidio AI Blog</title>

<link rel="stylesheet" href="../assets/style.css">

</head>

<body>

<section class="section">

<div class="container">

<div class="card">

<h1>
Tidio AI Blog
</h1>

<ul>

{"".join(blog_links)}

</ul>

<p style="margin-top:20px;">

<a class="button" href="{AFFILIATE_URL}">
{random_cta()}
</a>

</p>

</div>

</div>

</section>

</body>

</html>
"""

(BLOG_DIR / "index.html").write_text(
    BLOG_INDEX,
    encoding="utf-8"
)

# =========================================================
# TAG PAGES
# =========================================================

tags = [
    "ai-chatbot",
    "live-chat",
    "customer-support",
    "help-desk",
    "ecommerce"
]

for tag in tags:

    filename = f"{tag}.html"

    html = f"""
    <!DOCTYPE html>
    <html lang="en">

    <head>

    <meta charset="UTF-8">

    <title>{tag}</title>

    <link rel="stylesheet" href="../assets/style.css">

    </head>

    <body>

    <section class="section">

    <div class="container">

    <div class="card">

    <h1>{tag.replace('-', ' ').title()}</h1>

    <p>
    Explore resources related to {tag.replace('-', ' ')}.
    </p>

    <a class="button" href="{AFFILIATE_URL}">
    {random_cta()}
    </a>

    </div>

    </div>

    </section>

    </body>

    </html>
    """

    (TAG_DIR / filename).write_text(
        html,
        encoding="utf-8"
    )

# =========================================================
# SITEMAP
# =========================================================

sitemap_urls = []

for url in all_urls:

    sitemap_urls.append(f"""
    <url>
    <loc>{url}</loc>
    </url>
    """)

SITEMAP = f"""<?xml version="1.0" encoding="UTF-8"?>

<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">

{''.join(sitemap_urls)}

</urlset>
"""

(DIST_DIR / "sitemap.xml").write_text(
    SITEMAP,
    encoding="utf-8"
)

# =========================================================
# ROBOTS
# =========================================================

ROBOTS = f"""
User-agent: *
Allow: /

Sitemap: {DOMAIN}/sitemap.xml
"""

(DIST_DIR / "robots.txt").write_text(
    ROBOTS,
    encoding="utf-8"
)

# =========================================================
# EXPORT CONFIG
# =========================================================

with open(DIST_DIR / "site.json", "w") as f:

    json.dump(
        {
            "site_name": SITE_NAME,
            "domain": DOMAIN,
            "affiliate_url": AFFILIATE_URL,
            "pages": PAGES,
            "industries": INDUSTRIES
        },
        f,
        indent=2
    )

# =========================================================
# DONE
# =========================================================

print("=" * 60)
print("TIDIO AFFILIATE SEO SITE GENERATED")
print("=" * 60)
print(f"Core Pages: {len(PAGES)}")
print(f"Industry Pages: {len(INDUSTRIES)}")
print("Daily Blog Posts: 5")
print(f"Output Folder: {DIST_DIR}")
print("Ready For GitHub Pages Deployment")
print("=" * 60)
