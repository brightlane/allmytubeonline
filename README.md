# AllMyTube Affiliate Site — build.py v3

A complete, production-ready affiliate marketing website for [AllMyTube by Wondershare](https://www.wondershare.com), built for GitHub Pages at:

**`https://brightlane.github.io/allmytube/`**

---

## Quick Start

### Run locally
```bash
python3 build.py
```
Outputs everything into `allmytube-site/` next to `build.py`. No dependencies, no npm, no pip installs.

### Deploy to GitHub Pages
Push `build.py` and the workflow file to your repo. GitHub Actions does everything else automatically on every push to `main`.

```
Your repo root
├── build.py
├── README.md
└── .github/
    └── workflows/
        └── deploy.yml
```

---

## How Deployment Works

1. You push any change to `main`
2. GitHub Actions runs `python3 build.py`
3. `allmytube-site/` is generated with all 21 pages
4. That folder is force-pushed to the `gh-pages` branch
5. GitHub Pages serves `gh-pages` → your site is live

**Required one-time setup:** Go to `Settings → Pages → Source` and set it to the `gh-pages` branch, root `/`.

---

## What Gets Built

### 21 HTML Pages

| Page | URL | Primary Keywords |
|---|---|---|
| Homepage | `/` | AllMyTube download, video downloader |
| Features | `/features/` | AllMyTube features, 4K downloader |
| Supported Sites | `/supported-sites/` | YouTube downloader, TikTok downloader |
| How It Works | `/how-it-works/` | how to download YouTube videos |
| Pricing | `/pricing/` | AllMyTube price, AllMyTube cost |
| Review | `/review/` | AllMyTube review, is AllMyTube good |
| FAQ | `/faq/` | AllMyTube safe, AllMyTube free |
| Download | `/download/` | download AllMyTube Windows Mac |
| Blog | `/blog/` | video download tutorials |
| YouTube Guide | `/youtube-downloader/` | YouTube downloader, YouTube 4K |
| TikTok Guide | `/tiktok-downloader/` | TikTok downloader no watermark |
| MP3 Extractor | `/mp3-extractor/` | YouTube to MP3, extract audio |
| 4K Downloader | `/4k-downloader/` | 4K video downloader, Ultra HD |
| Playlist Guide | `/playlist-downloader/` | YouTube playlist downloader |
| Alternatives | `/alternatives/` | best video downloader alternatives |
| vs 4K Downloader | `/vs-4k-video-downloader/` | AllMyTube vs 4K Video Downloader |
| vs yt-dlp | `/vs-ytdlp/` | AllMyTube vs yt-dlp |
| vs Videoder | `/vs-videoder/` | AllMyTube vs Videoder |
| Privacy Policy | `/privacy/` | — |
| Disclaimer | `/disclaimer/` | — |
| 404 | `/404.html` | — |

### SEO & Meta Files

| File | Purpose |
|---|---|
| `sitemap.xml` | Full XML sitemap with `lastmod`, priority and changefreq — submit to Google Search Console |
| `robots.txt` | Allows all crawlers, points to sitemap |
| `llms.txt` | Structured site summary for AI crawlers (ChatGPT, Perplexity, etc.) |
| `feed.xml` | RSS feed for blog articles |
| `assets/favicon.svg` | Branded SVG icon |
| `.nojekyll` | Prevents GitHub Pages from processing files through Jekyll |

---

## SEO Built Into Every Page

- Unique `<title>` and `<meta description>` per page
- `<link rel="canonical">` to prevent duplicate content
- Open Graph tags for social sharing (`og:title`, `og:description`, `og:image`, `og:url`, `og:type`)
- Twitter Card meta tags
- `<link rel="alternate" type="application/rss+xml">` pointing to RSS feed
- **JSON-LD structured data on every page:**
  - `SoftwareApplication` schema (product info + aggregate rating)
  - `BreadcrumbList` schema on every inner page
  - `FAQPage` schema on `/faq/` and `/pricing/`
  - `Review` schema on `/review/`
  - `article` Open Graph type on guide and review pages
- Mobile-responsive layout (hamburger nav on mobile)
- Semantic HTML (`<nav>`, `<section>`, `<footer>`, `<details>`)

### After deploying, submit your sitemap:

1. **Google Search Console** → Add property → Submit sitemap
   ```
   https://brightlane.github.io/allmytube/sitemap.xml
   ```
2. **Bing Webmaster Tools** → Import from Google or submit sitemap directly
3. `robots.txt` points crawlers to your sitemap automatically

---

## Affiliate Link

Every download button and CTA in the entire site uses:

```
https://www.linkconnector.com/ta.php?lc=007949042649004532&atid=allmytubeweb
```

To update it, change the `AFF` variable at the top of `build.py` and re-run:

```python
AFF = "https://www.linkconnector.com/ta.php?lc=007949042649004532&atid=allmytubeweb"
```

---

## Customisation

All global settings are at the top of `build.py`:

```python
BASE      = Path(__file__).parent / "allmytube-site"  # Output folder — always relative, works anywhere
SITE_ROOT = "/allmytube"                               # GitHub Pages sub-path
SITE_URL  = "https://brightlane.github.io/allmytube"  # Canonical base URL
AFF       = "https://..."                              # Your affiliate link
YEAR      = date.today().year                          # Auto-updates every build
```

The entire CSS is one string near the top — edit it to change colours, fonts, spacing or layout across all 21 pages at once.

**To add a new page:**
1. Write a `pg_mypage()` function following the same pattern as the existing ones
2. Call `write("my-page/index.html", pg_mypage())` inside `main()`
3. Add the URL to `sitemap()` inside `pages = [...]`

---

## Tech Stack

| Layer | Choice | Why |
|---|---|---|
| Generator | Python 3 stdlib only | Zero dependencies, runs anywhere |
| HTML/CSS/JS | Vanilla — no frameworks | Instant load, no build step |
| Fonts | Google Fonts CDN | Bebas Neue + Inter — sharp, professional |
| Hosting | GitHub Pages | Free, HTTPS, custom domain support |
| CI/CD | GitHub Actions | Auto-deploy on every push |

---

## Design System

The site uses a dark tech aesthetic with a consistent set of CSS variables:

| Variable | Value | Usage |
|---|---|---|
| `--acc` | `#00d4ff` | Primary cyan — CTAs, headings, links |
| `--acc2` | `#ff3d6b` | Red accent — logo highlight, warnings |
| `--acc3` | `#7c3aff` | Purple — gradient partner to cyan |
| `--gold` | `#fbbf24` | Gold — star ratings, highlights |
| `--green` | `#22c55e` | Green — checkmarks, positive indicators |
| `--bg` | `#03060f` | Near-black background |
| `--txt` | `#f0f2f8` | Primary text |
| `--muted` | `#7c88a2` | Secondary / body text |

---

## File Structure After Build

```
allmytube-site/
├── .nojekyll
├── index.html
├── 404.html
├── sitemap.xml
├── robots.txt
├── llms.txt
├── feed.xml
├── assets/
│   └── favicon.svg
├── features/index.html
├── supported-sites/index.html
├── how-it-works/index.html
├── pricing/index.html
├── review/index.html
├── faq/index.html
├── download/index.html
├── blog/index.html
├── youtube-downloader/index.html
├── tiktok-downloader/index.html
├── mp3-extractor/index.html
├── 4k-downloader/index.html
├── playlist-downloader/index.html
├── alternatives/index.html
├── vs-4k-video-downloader/index.html
├── vs-ytdlp/index.html
├── vs-videoder/index.html
├── privacy/index.html
└── disclaimer/index.html
```

---

## v3 Changelog (vs v2)

- **+6 new pages** — YouTube, TikTok, MP3, 4K, Playlist guides + RSS feed
- **Review schema** added to `/review/` for rich results in Google
- **FAQ schema** on `/faq/` and `/pricing/` for expandable search results
- **Breadcrumb schema** on every inner page
- **RSS feed** (`feed.xml`) for blog article syndication
- **`llms.txt`** for AI crawler structured discovery
- **`lastmod` in sitemap** — accurate dates for every URL
- **Rating bars** on review page with visual fill percentages
- **Mobile nav** now slides in properly with JavaScript toggle
- **Pulsing CTA animation** on primary buttons
- **Fade-up hero animation** with staggered delays
- **All pages have fully unique content** — no template-copied descriptions
- **`BASE` path is always relative** — runs correctly on any machine or CI runner

---

## License

This codebase is provided for your personal affiliate use. AllMyTube is a product of Wondershare Software Ltd. This site is an independent affiliate guide and is not affiliated with or endorsed by Wondershare.
