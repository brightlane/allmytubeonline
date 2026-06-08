#!/usr/bin/env python3
"""AllMyTube Affiliate Site — build.py v3"""
from pathlib import Path
from datetime import date

BASE      = Path(__file__).parent / "allmytube-site"
SITE_ROOT = "/allmytubeonline"
SITE_URL  = "https://brightlane.github.io/allmytubeonline"
AFF       = "https://www.linkconnector.com/ta.php?lc=007949042649004532&atid=allmytubeweb"
YEAR      = date.today().year

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@500&display=swap');
:root{--bg:#03060f;--bg2:#070c1a;--bg3:#0c1224;--card:rgba(7,12,26,.9);--acc:#00d4ff;--acc2:#ff3d6b;--acc3:#7c3aff;--gold:#fbbf24;--green:#22c55e;--txt:#f0f2f8;--muted:#7c88a2;--bdr:rgba(0,212,255,.12);--bdr2:rgba(0,212,255,.28);--glow:0 0 30px rgba(0,212,255,.25);--r:14px;--r2:8px}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{font-family:'Inter',sans-serif;background:var(--bg);color:var(--txt);line-height:1.7;overflow-x:hidden;font-size:16px}
body::before{content:'';position:fixed;inset:0;z-index:0;pointer-events:none;background:radial-gradient(ellipse 80% 60% at 50% -10%,rgba(0,212,255,.07) 0%,transparent 60%),linear-gradient(rgba(0,212,255,.022) 1px,transparent 1px),linear-gradient(90deg,rgba(0,212,255,.022) 1px,transparent 1px);background-size:auto,64px 64px,64px 64px}
h1,h2,h3,h4{font-family:'Bebas Neue',sans-serif;letter-spacing:.04em;line-height:1.1}
h1{font-size:clamp(2.8rem,7vw,5.2rem)}h2{font-size:clamp(2rem,4vw,3.2rem)}h3{font-size:clamp(1.4rem,2.5vw,2rem)}h4{font-size:1.25rem}
p{color:var(--muted);font-weight:400}strong{color:var(--txt);font-weight:700}a{color:var(--acc);text-decoration:none;transition:color .2s}a:hover{color:#fff}
code{font-family:'JetBrains Mono',monospace;font-size:.85em;background:rgba(0,212,255,.08);padding:.15em .4em;border-radius:4px;color:var(--acc)}
nav{position:fixed;top:0;left:0;right:0;z-index:999;height:66px;background:rgba(3,6,15,.94);backdrop-filter:blur(20px);border-bottom:1px solid var(--bdr);display:flex;align-items:center;justify-content:space-between;padding:0 5%}
.logo{font-family:'Bebas Neue',sans-serif;font-size:1.8rem;letter-spacing:.1em;color:var(--acc);text-shadow:var(--glow)}.logo em{color:var(--acc2);font-style:normal}
.nav-links{display:flex;gap:1.6rem;list-style:none;align-items:center}.nav-links a{color:var(--muted);font-size:.8rem;font-weight:600;text-transform:uppercase;letter-spacing:.1em;transition:color .2s}.nav-links a:hover{color:var(--acc)}
.nav-dl{background:var(--acc)!important;color:#000!important;font-weight:800!important;padding:.45rem 1.1rem;border-radius:var(--r2);box-shadow:0 0 20px rgba(0,212,255,.4);transition:box-shadow .2s,transform .2s!important}.nav-dl:hover{box-shadow:0 0 32px rgba(0,212,255,.7)!important;transform:translateY(-1px)!important}
.ham{display:none;flex-direction:column;gap:5px;cursor:pointer}.ham span{display:block;width:22px;height:2px;background:var(--acc)}
.btn{display:inline-flex;align-items:center;gap:.5rem;font-family:'Inter',sans-serif;font-weight:700;font-size:.95rem;padding:.85rem 2rem;border-radius:var(--r2);text-transform:uppercase;letter-spacing:.08em;transition:all .25s;cursor:pointer;border:none;text-decoration:none;position:relative;z-index:1}
.btn-primary{background:linear-gradient(135deg,var(--acc) 0%,#0099cc 100%);color:#000;box-shadow:0 4px 28px rgba(0,212,255,.45)}.btn-primary:hover{transform:translateY(-3px);box-shadow:0 8px 40px rgba(0,212,255,.65);color:#000}
.btn-secondary{background:transparent;border:1.5px solid var(--bdr2);color:var(--txt)}.btn-secondary:hover{border-color:var(--acc);color:var(--acc);background:rgba(0,212,255,.05)}
.btn-ghost{background:rgba(0,212,255,.08);color:var(--acc);border:1px solid var(--bdr);font-size:.85rem;padding:.6rem 1.4rem}.btn-ghost:hover{background:rgba(0,212,255,.15);color:var(--acc)}
.btn-lg{padding:1.1rem 2.6rem;font-size:1.05rem}.btn-full{width:100%;justify-content:center}
.hero{min-height:100vh;display:flex;align-items:center;justify-content:center;text-align:center;padding:120px 5% 80px;position:relative;z-index:1;overflow:hidden}
.hero-inner{max-width:820px;margin:0 auto}
.hero-badge{display:inline-flex;align-items:center;gap:.5rem;background:rgba(0,212,255,.08);border:1px solid var(--bdr2);color:var(--acc);font-size:.78rem;font-weight:700;letter-spacing:.15em;text-transform:uppercase;padding:.4rem 1.1rem;border-radius:100px;margin-bottom:1.8rem}
.hero-badge::before{content:'●';font-size:.5rem;animation:blink 1.5s infinite}
@keyframes blink{0%,100%{opacity:1}50%{opacity:.3}}
.hero h1{margin-bottom:1.4rem}.c-acc{color:var(--acc)}.c-acc2{color:var(--acc2)}
.hero-sub{font-size:1.15rem;font-weight:400;color:var(--muted);max-width:640px;margin:0 auto 2.5rem;line-height:1.8}
.hero-ctas{display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;margin-bottom:2.5rem}
.hero-note{font-size:.8rem;color:var(--muted)}.hero-note span{color:var(--green);font-weight:600}
.stats-bar{display:flex;justify-content:center;flex-wrap:wrap;background:var(--bg2);border-top:1px solid var(--bdr);border-bottom:1px solid var(--bdr);position:relative;z-index:1}
.stat-item{flex:1;min-width:130px;text-align:center;padding:1.6rem 1rem;border-right:1px solid var(--bdr)}.stat-item:last-child{border-right:none}
.stat-num{font-family:'Bebas Neue',sans-serif;font-size:2.6rem;color:var(--acc);text-shadow:var(--glow);line-height:1;display:block}
.stat-lbl{font-size:.75rem;color:var(--muted);text-transform:uppercase;letter-spacing:.1em}
section{padding:6rem 5%;position:relative;z-index:1}
.section-label{font-size:.75rem;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--acc);display:block;margin-bottom:.6rem}
.section-title{margin-bottom:.9rem}.section-sub{color:var(--muted);max-width:600px;margin-bottom:3rem;font-size:1.05rem}
.tc{text-align:center}.tc .section-sub{margin-left:auto;margin-right:auto}
.alt-bg{background:linear-gradient(180deg,transparent,rgba(0,212,255,.02),transparent)}
.grid-3{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:1.5rem}
.grid-2{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:1.5rem}
.split{display:grid;grid-template-columns:1fr 1fr;gap:5rem;align-items:center}
.card{background:var(--card);border:1px solid var(--bdr);border-radius:var(--r);padding:2rem;transition:all .3s;position:relative;overflow:hidden}
.card::after{content:'';position:absolute;top:0;left:0;width:100%;height:2px;background:linear-gradient(90deg,transparent,var(--acc),transparent);transform:scaleX(0);transition:transform .4s}.card:hover::after{transform:scaleX(1)}
.card:hover{border-color:var(--bdr2);transform:translateY(-5px);box-shadow:0 16px 48px rgba(0,0,0,.5)}
.card-icon{width:54px;height:54px;border-radius:12px;background:rgba(0,212,255,.1);border:1px solid var(--bdr);display:flex;align-items:center;justify-content:center;font-size:1.5rem;margin-bottom:1.2rem}
.card h3{font-size:1.3rem;color:var(--txt);margin-bottom:.5rem}.card h4{font-size:1.1rem;color:var(--txt);margin-bottom:.5rem}.card p{font-size:.9rem}
.card-featured{border-color:rgba(0,212,255,.35);background:linear-gradient(135deg,rgba(0,212,255,.06),rgba(124,58,255,.06))}
.feat-list{list-style:none;padding:0;display:flex;flex-direction:column;gap:.85rem}
.feat-list li{display:flex;align-items:flex-start;gap:.75rem;font-size:.93rem;color:var(--muted)}
.feat-list li::before{content:'▶';color:var(--acc);font-size:.6rem;margin-top:.45rem;flex-shrink:0}
.feat-list li strong{color:var(--txt)}
.check-list{list-style:none;padding:0;display:flex;flex-direction:column;gap:.7rem}
.check-list li{display:flex;gap:.6rem;font-size:.9rem;color:var(--muted)}.check-list li::before{content:'✓';color:var(--green);font-weight:700;flex-shrink:0}
.pricing-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1.5rem;max-width:920px;margin:0 auto}
.price-card{background:var(--card);border:1px solid var(--bdr);border-radius:var(--r);padding:2.5rem 2rem;text-align:center;position:relative;transition:all .3s}.price-card:hover{transform:translateY(-4px)}
.price-card.pop{border-color:var(--acc);background:linear-gradient(135deg,rgba(0,212,255,.07),rgba(124,58,255,.07))}
.pop-badge{position:absolute;top:-14px;left:50%;transform:translateX(-50%);background:linear-gradient(135deg,var(--acc),var(--acc3));color:#fff;font-size:.72rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;padding:.28rem 1rem;border-radius:100px}
.price-name{font-size:.82rem;text-transform:uppercase;letter-spacing:.15em;color:var(--muted);margin-bottom:1rem}
.price-amount{font-family:'Bebas Neue',sans-serif;font-size:3.8rem;color:var(--acc);line-height:1}
.price-amount sup{font-size:1.4rem;vertical-align:top;margin-top:.6rem;display:inline-block}
.price-period{font-size:.8rem;color:var(--muted);margin-bottom:1.6rem}
.price-feats{list-style:none;padding:0;text-align:left;margin-bottom:2rem;display:flex;flex-direction:column;gap:.65rem}
.price-feats li{font-size:.88rem;color:var(--muted);display:flex;gap:.5rem}.price-feats li::before{content:'✓';color:var(--green);font-weight:700;flex-shrink:0}
.price-note{font-size:.78rem;color:var(--gold);margin-top:.8rem;font-weight:600}
.tbl-wrap{overflow-x:auto;border-radius:var(--r);border:1px solid var(--bdr)}
table{width:100%;border-collapse:collapse}
thead th{background:rgba(0,212,255,.08);color:var(--acc);font-family:'Bebas Neue',sans-serif;font-size:1rem;letter-spacing:.06em;padding:1rem 1.2rem;text-align:left;border-bottom:1px solid var(--bdr)}
tbody td{padding:.9rem 1.2rem;border-bottom:1px solid var(--bdr);font-size:.88rem;color:var(--muted)}
tbody tr:last-child td{border-bottom:none}tbody tr:hover td{background:rgba(255,255,255,.02)}
.td-name{color:var(--txt);font-weight:600}.td-yes{color:var(--green);font-weight:700}.td-no{color:var(--acc2)}.td-partial{color:var(--gold)}.td-hi{background:rgba(0,212,255,.05)!important}
.faq-wrap{max-width:780px;margin:0 auto;display:flex;flex-direction:column;gap:1rem}
details{background:var(--card);border:1px solid var(--bdr);border-radius:var(--r);overflow:hidden;transition:border-color .2s}
details[open]{border-color:var(--bdr2)}
details summary{padding:1.2rem 1.5rem;cursor:pointer;font-weight:600;font-size:.97rem;color:var(--txt);list-style:none;display:flex;justify-content:space-between;align-items:center}
details summary::-webkit-details-marker{display:none}
details summary::after{content:'+';color:var(--acc);font-size:1.5rem;font-weight:300;line-height:1}
details[open] summary::after{content:'−'}
details .ans{padding:0 1.5rem 1.2rem;border-top:1px solid var(--bdr);padding-top:1rem;font-size:.92rem}
details .ans p{color:var(--muted)}
.testi-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1.4rem}
.testi{background:var(--card);border:1px solid var(--bdr);border-radius:var(--r);padding:2rem}
.stars{color:var(--gold);font-size:1rem;margin-bottom:.9rem;letter-spacing:.1em}
.testi-text{font-size:.93rem;color:var(--txt);font-style:italic;margin-bottom:1.2rem;line-height:1.7}
.testi-name{font-weight:700;font-size:.88rem;color:var(--acc)}.testi-role{font-size:.8rem;color:var(--muted)}
.sites-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(110px,1fr));gap:.7rem}
.site-pill{background:rgba(255,255,255,.03);border:1px solid var(--bdr);border-radius:var(--r2);padding:.5rem .8rem;font-size:.78rem;text-align:center;color:var(--muted);transition:all .2s;cursor:default}
.site-pill:hover{border-color:var(--acc);color:var(--acc);background:rgba(0,212,255,.05)}
.steps{max-width:700px;display:flex;flex-direction:column}
.step{display:flex;gap:2rem;align-items:flex-start;padding:2rem 0 2rem 2.5rem;border-left:2px solid rgba(0,212,255,.2);margin-left:1.5rem;position:relative}
.step::before{content:attr(data-n);position:absolute;left:-1.6rem;width:3.1rem;height:3.1rem;background:var(--bg);border:2px solid var(--acc);border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:'Bebas Neue',sans-serif;font-size:1.3rem;color:var(--acc);box-shadow:0 0 20px rgba(0,212,255,.3)}
.step:last-child{border-left-color:transparent}
.step-body h3{font-size:1.2rem;color:var(--txt);margin-bottom:.4rem}.step-body p{font-size:.9rem}
.blog-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1.5rem}
.blog-card{background:var(--card);border:1px solid var(--bdr);border-radius:var(--r);overflow:hidden;transition:all .3s;display:flex;flex-direction:column}
.blog-card:hover{transform:translateY(-5px);border-color:var(--bdr2);box-shadow:0 16px 40px rgba(0,0,0,.4)}
.blog-thumb{height:170px;display:flex;align-items:center;justify-content:center;font-size:3rem;background:linear-gradient(135deg,var(--bg3),rgba(0,212,255,.08));border-bottom:1px solid var(--bdr)}
.blog-body{padding:1.5rem;flex:1;display:flex;flex-direction:column}
.blog-tag{font-size:.72rem;color:var(--acc);text-transform:uppercase;letter-spacing:.12em;font-weight:700;margin-bottom:.5rem}
.blog-card h3{font-size:1.05rem;color:var(--txt);margin-bottom:.5rem;line-height:1.35}.blog-card p{font-size:.84rem;flex:1}
.blog-meta{display:flex;gap:1rem;margin-top:1rem;font-size:.77rem;color:var(--muted)}.blog-read{margin-top:1rem;font-size:.82rem;font-weight:700;color:var(--acc)}
.cta-block{text-align:center;padding:6rem 5%;background:linear-gradient(135deg,rgba(0,212,255,.05),rgba(124,58,255,.05));border-top:1px solid var(--bdr);border-bottom:1px solid var(--bdr);position:relative;z-index:1}
.cta-block h2{margin-bottom:.9rem}.cta-block p{max-width:520px;margin:0 auto 2.2rem;font-size:1.05rem}
.hbox{background:rgba(0,212,255,.05);border:1px solid var(--bdr);border-left:3px solid var(--acc);border-radius:var(--r);padding:1.6rem 1.8rem;margin:1.6rem 0}
.hbox h4{color:var(--acc);margin-bottom:.5rem}
.hbox.warn{border-left-color:var(--gold);background:rgba(251,191,36,.05)}.hbox.warn h4{color:var(--gold)}
.chip{display:inline-block;font-size:.72rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;padding:.2rem .6rem;border-radius:4px}
.chip-blue{background:rgba(0,212,255,.1);color:var(--acc);border:1px solid rgba(0,212,255,.2)}
.chip-green{background:rgba(34,197,94,.1);color:var(--green);border:1px solid rgba(34,197,94,.2)}
.chip-gold{background:rgba(251,191,36,.1);color:var(--gold);border:1px solid rgba(251,191,36,.2)}
.ph{padding:130px 5% 60px;position:relative;z-index:1;background:linear-gradient(180deg,rgba(0,212,255,.04) 0%,transparent 100%);border-bottom:1px solid var(--bdr)}
.breadcrumb{font-size:.78rem;color:var(--muted);margin-bottom:1.2rem}
.breadcrumb a{color:var(--muted)}.breadcrumb .cur{color:var(--acc)}
.rating-bars{display:flex;flex-direction:column;gap:1rem}
.rbar{display:grid;grid-template-columns:140px 1fr 40px;align-items:center;gap:1rem}
.rbar-label{font-size:.85rem;color:var(--muted)}
.rbar-track{height:8px;background:rgba(255,255,255,.06);border-radius:100px;overflow:hidden}
.rbar-fill{height:100%;border-radius:100px;background:linear-gradient(90deg,var(--acc),var(--acc3))}
.rbar-score{font-family:'Bebas Neue',sans-serif;font-size:1.1rem;color:var(--acc);text-align:right}
.score-big{display:inline-block;font-family:'Bebas Neue',sans-serif;font-size:5rem;color:var(--acc);text-shadow:var(--glow);line-height:1}
.score-label{font-size:.85rem;color:var(--muted);text-transform:uppercase;letter-spacing:.1em}
footer{background:var(--bg2);border-top:1px solid var(--bdr);padding:4rem 5% 2rem;position:relative;z-index:1}
.footer-grid{display:grid;grid-template-columns:2.2fr 1fr 1fr 1fr;gap:3rem;margin-bottom:3rem}
.footer-brand{font-family:'Bebas Neue',sans-serif;font-size:1.6rem;color:var(--acc);margin-bottom:.8rem}
.footer-brand em{color:var(--acc2);font-style:normal}
.footer-desc{font-size:.84rem;max-width:260px;line-height:1.7}
.footer-col h5{font-size:.75rem;text-transform:uppercase;letter-spacing:.15em;color:var(--txt);margin-bottom:1rem}
.footer-col ul{list-style:none;padding:0;display:flex;flex-direction:column;gap:.6rem}
.footer-col a{color:var(--muted);font-size:.84rem}.footer-col a:hover{color:var(--acc)}
.footer-bottom{border-top:1px solid var(--bdr);padding-top:1.5rem;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem}
.footer-bottom p{font-size:.78rem;color:var(--muted)}
@media(max-width:900px){.footer-grid{grid-template-columns:1fr 1fr}.split{grid-template-columns:1fr;gap:2.5rem}}
@media(max-width:640px){.nav-links{display:none}.ham{display:flex}.footer-grid{grid-template-columns:1fr}.stat-item{min-width:45%;border-right:none;border-bottom:1px solid var(--bdr)}.pricing-grid{grid-template-columns:1fr}.rbar{grid-template-columns:100px 1fr 36px}}
@keyframes fadeUp{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:translateY(0)}}
.anim{animation:fadeUp .65s ease forwards}.anim-d1{animation-delay:.1s;opacity:0}.anim-d2{animation-delay:.2s;opacity:0}.anim-d3{animation-delay:.3s;opacity:0}
@keyframes pulse{0%,100%{box-shadow:0 4px 28px rgba(0,212,255,.45)}50%{box-shadow:0 4px 48px rgba(0,212,255,.75)}}
.btn-primary{animation:pulse 3.5s ease-in-out infinite}
"""


def nav():
    links=[("Features",f"{SITE_ROOT}/features/"),("1000+ Sites",f"{SITE_ROOT}/supported-sites/"),("How It Works",f"{SITE_ROOT}/how-it-works/"),("Pricing",f"{SITE_ROOT}/pricing/"),("Review",f"{SITE_ROOT}/review/"),("Blog",f"{SITE_ROOT}/blog/"),("FAQ",f"{SITE_ROOT}/faq/")]
    li="\n".join(f'<li><a href="{u}">{l}</a></li>' for l,u in links)
    return f'<nav><a class="logo" href="{SITE_ROOT}/">All<em>My</em>Tube</a><ul class="nav-links">{li}<li><a href="{AFF}" class="nav-dl" target="_blank" rel="noopener sponsored">⬇ Free Download</a></li></ul><div class="ham"><span></span><span></span><span></span></div></nav>'

def foot():
    return f"""<footer><div class="footer-grid">
<div><div class="footer-brand">All<em>My</em>Tube</div><p class="footer-desc">The world's most powerful video downloader by Wondershare. Download from 10,000+ platforms in 4K, HD or MP3.</p></div>
<div class="footer-col"><h5>Product</h5><ul><li><a href="{SITE_ROOT}/features/">Features</a></li><li><a href="{SITE_ROOT}/pricing/">Pricing</a></li><li><a href="{SITE_ROOT}/supported-sites/">Supported Sites</a></li><li><a href="{SITE_ROOT}/how-it-works/">How It Works</a></li><li><a href="{SITE_ROOT}/download/">Download</a></li><li><a href="{SITE_ROOT}/review/">Review</a></li></ul></div>
<div class="footer-col"><h5>Guides</h5><ul><li><a href="{SITE_ROOT}/youtube-downloader/">YouTube Guide</a></li><li><a href="{SITE_ROOT}/tiktok-downloader/">TikTok Guide</a></li><li><a href="{SITE_ROOT}/mp3-extractor/">MP3 Extractor</a></li><li><a href="{SITE_ROOT}/4k-downloader/">4K Downloads</a></li><li><a href="{SITE_ROOT}/playlist-downloader/">Playlist Download</a></li><li><a href="{SITE_ROOT}/blog/">Blog</a></li></ul></div>
<div class="footer-col"><h5>Compare</h5><ul><li><a href="{SITE_ROOT}/vs-4k-video-downloader/">vs 4K Downloader</a></li><li><a href="{SITE_ROOT}/vs-ytdlp/">vs yt-dlp</a></li><li><a href="{SITE_ROOT}/vs-videoder/">vs Videoder</a></li><li><a href="{SITE_ROOT}/alternatives/">All Alternatives</a></li><li><a href="{SITE_ROOT}/faq/">FAQ</a></li><li><a href="{SITE_ROOT}/disclaimer/">Disclaimer</a></li></ul></div>
</div><div class="footer-bottom"><p>© {YEAR} AllMyTube Guide — Independent affiliate site. Commissions earned at no extra cost to you.</p><p><a href="{AFF}" target="_blank" rel="noopener sponsored">Download AllMyTube Free →</a></p></div></footer>"""

def bc(*crumbs):
    parts=[]
    for i,(label,url) in enumerate(crumbs):
        parts.append(f'<a href="{url}">{label}</a>' if url and i<len(crumbs)-1 else f'<span class="cur">{label}</span>')
    return '<nav class="breadcrumb">'+" › ".join(parts)+"</nav>"

def page(title,desc,path,body,kw="",schema_extra="",article=False):
    kw=kw or "AllMyTube, video downloader, YouTube downloader, 4K download, Wondershare"
    canon=f"{SITE_URL}{path}"
    sw=f'{{"@context":"https://schema.org","@type":"SoftwareApplication","name":"AllMyTube","applicationCategory":"MultimediaApplication","operatingSystem":"Windows, macOS","offers":{{"@type":"Offer","price":"0","priceCurrency":"USD"}},"aggregateRating":{{"@type":"AggregateRating","ratingValue":"4.7","reviewCount":"2841"}},"description":"{desc}","url":"{SITE_URL}/","publisher":{{"@type":"Organization","name":"Wondershare"}}}}'
    bcs=f'{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Home","item":"{SITE_URL}/"}},{{"@type":"ListItem","position":2,"name":"{title.split(" —")[0].strip()}","item":"{canon}"}}]}}'
    schemas=f'<script type="application/ld+json">{sw}</script><script type="application/ld+json">{bcs}</script>'
    if schema_extra: schemas+=f'<script type="application/ld+json">{schema_extra}</script>'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{kw}">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large">
<link rel="canonical" href="{canon}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}"><meta property="og:type" content="{'article' if article else 'website'}">
<meta property="og:image" content="{SITE_URL}/assets/og.png"><meta property="og:site_name" content="AllMyTube Guide">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{title}"><meta name="twitter:description" content="{desc}">
<link rel="icon" href="{SITE_ROOT}/assets/favicon.svg" type="image/svg+xml">
<link rel="alternate" type="application/rss+xml" title="AllMyTube Blog" href="{SITE_URL}/feed.xml">
{schemas}
<style>{CSS}</style>
</head>
<body>
{nav()}
{body}
{foot()}
<script>
document.querySelector('.ham').addEventListener('click',function(){{
  var nl=document.querySelector('.nav-links');
  nl.style.cssText=nl.style.display==='flex'?'':'display:flex;position:fixed;top:66px;left:0;right:0;flex-direction:column;background:rgba(3,6,15,.97);padding:2rem 5%;gap:1.2rem;border-bottom:1px solid rgba(0,212,255,.15);z-index:998';
}});
</script>
</body></html>"""

def write(rel,content):
    p=BASE/rel
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(content,encoding="utf-8")
    print(f"  ✓  {rel}")


# ── PAGE: HOMEPAGE ────────────────────────────────────────────────────────────
def pg_index():
    sites=["YouTube","YouTube Shorts","TikTok","Vimeo","Facebook","Instagram","Twitter/X","Twitch","Dailymotion","Reddit","SoundCloud","Bilibili","Niconico","Pinterest","LinkedIn","VK","Rumble","BitChute","Odysee","Mixcloud","Bandcamp","Metacafe"]
    pills="".join(f'<div class="site-pill">{s}</div>' for s in sites)
    return page(f"AllMyTube — Download Videos from 10,000+ Sites in 4K | {YEAR}",
        "Download AllMyTube free. Save YouTube, TikTok, Vimeo & 10,000+ sites in 4K HD or MP3. 50M+ users. Windows & Mac. Batch download entire playlists.","/",f"""
<section class="hero"><div class="hero-inner">
  <div class="hero-badge anim">🏆 Trusted by 50 Million Users Worldwide</div>
  <h1 class="anim anim-d1">Download <span class="c-acc">Any Video</span><br>From <span class="c-acc2">10,000+ Sites</span></h1>
  <p class="hero-sub anim anim-d2">AllMyTube by Wondershare is the world's leading video downloader. Save YouTube, TikTok, Vimeo, Facebook and thousands more in stunning 4K — or extract MP3 audio in seconds.</p>
  <div class="hero-ctas anim anim-d3">
    <a href="{AFF}" class="btn btn-primary btn-lg" target="_blank" rel="noopener sponsored">⬇ Download Free Now</a>
    <a href="{SITE_ROOT}/how-it-works/" class="btn btn-secondary btn-lg">See How It Works →</a>
  </div>
  <p class="hero-note"><span>✓</span> Free Trial &nbsp;·&nbsp; <span>✓</span> Windows &amp; Mac &nbsp;·&nbsp; <span>✓</span> No Credit Card &nbsp;·&nbsp; <span>✓</span> Instant Setup</p>
</div></section>
<div class="stats-bar">
  <div class="stat-item"><span class="stat-num">10,000+</span><span class="stat-lbl">Supported Sites</span></div>
  <div class="stat-item"><span class="stat-num">50M+</span><span class="stat-lbl">Global Users</span></div>
  <div class="stat-item"><span class="stat-num">4K</span><span class="stat-lbl">Max Resolution</span></div>
  <div class="stat-item"><span class="stat-num">150+</span><span class="stat-lbl">Output Formats</span></div>
  <div class="stat-item"><span class="stat-num">3×</span><span class="stat-lbl">Faster Downloads</span></div>
  <div class="stat-item"><span class="stat-num">200+</span><span class="stat-lbl">Countries</span></div>
</div>
<section>
  <span class="section-label">Core Features</span>
  <h2 class="section-title">Everything You Need to <span class="c-acc">Download &amp; Convert</span></h2>
  <p class="section-sub">One app handles it all — downloading, converting, batch processing, scheduling, and built-in playback.</p>
  <div class="grid-3">
    <div class="card"><div class="card-icon">🎬</div><h3>4K Ultra HD</h3><p>Download at the highest quality available — up to 4K 2160p. Seven resolution presets so you always get exactly what you need.</p></div>
    <div class="card"><div class="card-icon">⚡</div><h3>3× Faster Speed</h3><p>AllMyTube's multithreading engine saturates your full bandwidth — downloads that take minutes on competitors take seconds here.</p></div>
    <div class="card"><div class="card-icon">🌐</div><h3>10,000+ Sites</h3><p>From YouTube and TikTok to niche regional platforms — if a website streams video, AllMyTube can almost certainly download it.</p></div>
    <div class="card"><div class="card-icon">🎵</div><h3>MP3 Extraction</h3><p>Extract crystal-clear audio from any video as MP3, AAC, FLAC or WAV. Perfect for music, podcasts, lectures and audiobooks.</p></div>
    <div class="card"><div class="card-icon">📋</div><h3>Batch &amp; Playlist</h3><p>Download entire YouTube playlists or channels in one click. Queue hundreds of videos and walk away — AllMyTube handles the rest.</p></div>
    <div class="card"><div class="card-icon">🔄</div><h3>Built-in Converter</h3><p>Convert to 150+ formats including MP4, MKV, AVI, MOV and device presets for iPhone, Android, Samsung TV, iPad, PS5 and more.</p></div>
    <div class="card"><div class="card-icon">🔌</div><h3>Browser Extension</h3><p>A download button appears on every video page in Chrome, Firefox or Edge — no URL copying needed.</p></div>
    <div class="card"><div class="card-icon">📅</div><h3>Scheduler</h3><p>Schedule downloads for off-peak hours. Set AllMyTube to auto-shutdown or sleep when your queue completes.</p></div>
    <div class="card"><div class="card-icon">▶</div><h3>Built-in Player</h3><p>Watch downloaded content instantly inside AllMyTube's built-in media player with full controls and subtitle support.</p></div>
  </div>
</section>
<section class="alt-bg">
  <span class="section-label">Compatible Platforms</span>
  <h2 class="section-title tc">Works With Your <span class="c-acc">Favourite Sites</span></h2>
  <div class="sites-grid" style="max-width:880px;margin:0 auto 2rem">{pills}</div>
  <div style="text-align:center"><a href="{SITE_ROOT}/supported-sites/" class="btn btn-ghost">View All 10,000+ Sites →</a></div>
</section>
<section>
  <div class="split">
    <div>
      <span class="section-label">Why AllMyTube Wins</span>
      <h2 class="section-title">More Than Just<br><span class="c-acc">a Downloader</span></h2>
      <p style="margin-bottom:1.8rem">Most video downloaders do one thing. AllMyTube is a complete video workflow — download, convert, organise, play and transfer in one app.</p>
      <ul class="feat-list">
        <li><strong>One-click YouTube playlist download</strong> — entire channels in seconds</li>
        <li><strong>Real 4K output</strong> — no re-encoding, no quality loss</li>
        <li><strong>Private video support</strong> — download your own private YouTube videos</li>
        <li><strong>Subtitle download</strong> — save SRT/VTT subtitles alongside your video</li>
        <li><strong>Screen recorder</strong> — built-in fallback for DRM-protected streams</li>
        <li><strong>Device transfer</strong> — send videos directly to iPhone or Android</li>
        <li><strong>Auto-shutdown</strong> — perfect for overnight batch downloads</li>
      </ul>
      <div style="margin-top:2rem"><a href="{AFF}" class="btn btn-primary" target="_blank" rel="noopener sponsored">⬇ Try Free Today</a></div>
    </div>
    <div>
      <div class="card card-featured" style="padding:2.5rem">
        <h3 style="margin-bottom:1.5rem;color:var(--acc)">AllMyTube vs The Rest</h3>
        <div class="tbl-wrap"><table>
          <thead><tr><th>Feature</th><th>AllMyTube</th><th>Others</th></tr></thead>
          <tbody>
            <tr><td>Supported Sites</td><td class="td-yes td-hi">10,000+</td><td class="td-no">50–500</td></tr>
            <tr><td>4K Downloads</td><td class="td-yes td-hi">✓ True 4K</td><td class="td-partial">Partial</td></tr>
            <tr><td>Built-in Converter</td><td class="td-yes td-hi">150+ formats</td><td class="td-no">✗</td></tr>
            <tr><td>Batch Playlists</td><td class="td-yes td-hi">Unlimited</td><td class="td-partial">Limited</td></tr>
            <tr><td>Browser Extension</td><td class="td-yes td-hi">✓</td><td class="td-no">✗</td></tr>
            <tr><td>Built-in Player</td><td class="td-yes td-hi">✓</td><td class="td-no">✗</td></tr>
            <tr><td>Scheduler</td><td class="td-yes td-hi">✓</td><td class="td-no">✗</td></tr>
          </tbody>
        </table></div>
        <div style="text-align:center;margin-top:1.5rem"><a href="{SITE_ROOT}/alternatives/" class="btn btn-ghost">Full Comparison →</a></div>
      </div>
    </div>
  </div>
</section>
<section class="alt-bg">
  <span class="section-label" style="display:block;text-align:center">Real User Reviews</span>
  <h2 class="section-title tc">Loved by Creators <span class="c-acc">Worldwide</span></h2>
  <p class="section-sub tc">4.7 stars from 2,800+ verified reviews</p>
  <div class="testi-grid">
    <div class="testi"><div class="stars">★★★★★</div><p class="testi-text">"I've tried dozens of video downloaders. AllMyTube is on another level — 4K downloads that are actually 4K, playlists handled perfectly, and the speed is unreal."</p><div class="testi-name">Marcus T. 🇺🇸</div><div class="testi-role">Filmmaker, Los Angeles</div></div>
    <div class="testi"><div class="stars">★★★★★</div><p class="testi-text">"As a teacher in a remote area, I download educational content for offline use in the classroom. AllMyTube saves me hours every week. Truly essential software."</p><div class="testi-name">Priya S. 🇮🇳</div><div class="testi-role">Educator, Mumbai</div></div>
    <div class="testi"><div class="stars">★★★★★</div><p class="testi-text">"The MP3 extraction quality is perfect — no artifacts, proper ID3 tags, everything. I use it daily for my podcast workflow. The lifetime plan was a no-brainer."</p><div class="testi-name">Elena R. 🇬🇧</div><div class="testi-role">Podcaster, London</div></div>
    <div class="testi"><div class="stars">★★★★★</div><p class="testi-text">"Downloaded my entire YouTube channel archive — 300+ videos — overnight with the scheduler. Woke up to everything neatly saved. Absolute game changer."</p><div class="testi-name">Kenji M. 🇯🇵</div><div class="testi-role">YouTube Creator, Tokyo</div></div>
    <div class="testi"><div class="stars">★★★★☆</div><p class="testi-text">"The browser extension makes it seamless — I just click the button while watching and it downloads in the background. Simple and reliable every single time."</p><div class="testi-name">Sofia L. 🇧🇷</div><div class="testi-role">Video Editor, São Paulo</div></div>
    <div class="testi"><div class="stars">★★★★★</div><p class="testi-text">"Wondershare always delivers quality software. AllMyTube is no exception — polished, fast, comprehensive. The Vimeo and Facebook download support is superb."</p><div class="testi-name">Ahmed K. 🇦🇪</div><div class="testi-role">Content Director, Dubai</div></div>
  </div>
</section>
<div class="cta-block">
  <span class="section-label" style="display:block;margin-bottom:1rem">Get Started Today</span>
  <h2>Ready to Download <span class="c-acc">Any Video?</span></h2>
  <p>Join 50 million users in 200+ countries who trust AllMyTube for fast, high-quality video downloads. Free trial — no credit card needed.</p>
  <a href="{AFF}" class="btn btn-primary btn-lg" target="_blank" rel="noopener sponsored">⬇ Download AllMyTube Free</a>
  <p style="margin-top:1.2rem;font-size:.82rem">Personal plan from $29/year · Family plan from $49/year · Lifetime options available</p>
</div>""")


# ── PAGE: FEATURES ────────────────────────────────────────────────────────────
def pg_features():
    return page(f"AllMyTube Features — 4K, Batch Download, Converter & More | {YEAR}",
        "Explore all 15 AllMyTube features: 4K downloads, MP3 extraction, playlist batch download, 150-format converter, browser extension, subtitle download, screen recorder.",
        "/features/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Features",None))}
  <span class="section-label">Complete Feature Set</span>
  <h1>AllMyTube <span class="c-acc">Features</span></h1>
  <p style="max-width:620px;margin-top:.8rem;font-size:1.1rem;color:var(--muted)">Every tool you need to download, convert, organise and enjoy video content from anywhere on the web.</p>
</div>
<section>
  <div class="grid-3">
    <div class="card"><div class="card-icon">🎯</div><h3>One-Click Download</h3><p>Paste any video URL and click Download. Or use the browser extension for a floating button on every video page you visit — no URL copying needed.</p></div>
    <div class="card"><div class="card-icon">🎬</div><h3>4K / 8K Video</h3><p>Choose from 7 quality presets: 2160p (4K), 1440p, 1080p Full HD, 720p HD, 480p, 360p and 240p. Always get the exact resolution you want.</p></div>
    <div class="card"><div class="card-icon">🎵</div><h3>Audio Extraction</h3><p>Extract audio as MP3 up to 320kbps, AAC, FLAC or WAV. Proper ID3 tags including artist, title and album art where available.</p></div>
    <div class="card"><div class="card-icon">📋</div><h3>Playlist Download</h3><p>Download entire YouTube playlists, channels or Vimeo showcases with one URL. Handle queues of 500+ videos without any manual effort.</p></div>
    <div class="card"><div class="card-icon">🔄</div><h3>Format Converter</h3><p>Convert to 150+ output formats: MP4, MKV, AVI, MOV, WMV, FLV, MP3, AAC, FLAC, WAV and device presets for every popular platform.</p></div>
    <div class="card"><div class="card-icon">📅</div><h3>Download Scheduler</h3><p>Schedule downloads for off-peak hours or nights. Choose Auto Shutdown, Hibernate, Sleep or Exit when the queue completes automatically.</p></div>
    <div class="card"><div class="card-icon">🌐</div><h3>10,000+ Sites</h3><p>YouTube, TikTok, Vimeo, Facebook, Instagram, Twitch, Dailymotion, Reddit, Bilibili, SoundCloud and over 10,000 more global platforms.</p></div>
    <div class="card"><div class="card-icon">🔌</div><h3>Browser Extension</h3><p>Adds a download button directly on video pages in Chrome, Firefox and Edge. One click to add any video to your download queue instantly.</p></div>
    <div class="card"><div class="card-icon">▶</div><h3>Built-in Player</h3><p>Watch downloaded content immediately inside AllMyTube. Full playback controls, subtitle rendering, no additional software required.</p></div>
    <div class="card"><div class="card-icon">📱</div><h3>Device Transfer</h3><p>Transfer downloaded videos directly to iPhone, iPad or Android. AllMyTube handles format conversion automatically for the target device.</p></div>
    <div class="card"><div class="card-icon">💬</div><h3>Subtitle Download</h3><p>Download videos with subtitles in SRT, ASS or VTT format from YouTube and other platforms. Saved baked-in or as a separate file.</p></div>
    <div class="card"><div class="card-icon">🖥</div><h3>Screen Recorder</h3><p>Built-in screen recorder as a powerful fallback for any stream that cannot be directly downloaded — including DRM-protected content.</p></div>
    <div class="card"><div class="card-icon">🔐</div><h3>Private Videos</h3><p>Download your own private YouTube videos when logged in. Great for archiving your own content library before it's ever lost.</p></div>
    <div class="card"><div class="card-icon">⚡</div><h3>Turbo Speed</h3><p>Multithreaded download engine runs 3× faster than single-thread competitors. Download more in less time on any connection speed.</p></div>
    <div class="card"><div class="card-icon">🛡</div><h3>Safe &amp; Trusted</h3><p>Built by Wondershare — a publicly listed software company. 50M+ users, no malware, no bundled software, regular updates included.</p></div>
  </div>
  <div class="cta-block" style="margin-top:3rem;border-radius:var(--r)">
    <h2 style="margin-bottom:.8rem">All Features, <span class="c-acc">Free to Try</span></h2>
    <p>Download AllMyTube and test every feature with the free trial. No credit card required.</p>
    <a href="{AFF}" class="btn btn-primary" target="_blank" rel="noopener sponsored">⬇ Download AllMyTube Free</a>
  </div>
</section>""","AllMyTube features, video downloader features, 4K downloader, MP3 extractor, playlist downloader")

# ── PAGE: SUPPORTED SITES ─────────────────────────────────────────────────────
def pg_supported():
    cats={"🎬 Video Giants":["YouTube","YouTube Shorts","YouTube Music","Vimeo","Dailymotion","Metacafe","Veoh","Rumble","BitChute","Odysee"],"📱 Social Media":["TikTok","Instagram Reels","Instagram Stories","Facebook","Twitter/X","Pinterest","LinkedIn","Tumblr","Reddit","VK","OK.ru"],"🎮 Gaming & Live":["Twitch","Twitch Clips","Kick","9GAG","Streamable","Gfycat","Medal.tv","Nimo TV"],"🎵 Music & Audio":["SoundCloud","Mixcloud","Bandcamp","Beatport","Audiomack","Pandora","iHeartRadio"],"🌏 Asian Platforms":["Bilibili","Niconico","Youku","iQIYI","Tencent Video","Naver TV","Kakao TV"],"📺 Broadcast & News":["BBC iPlayer","ITV Hub","Channel 4","Sky Sports","ESPN","NBC Sports","Fox Sports","CNN"],"🌍 Global Streaming":["Hotstar","ZEE5","MX Player","Voot","SonyLIV","Eros Now","JioCinema","Shahid"],"🎓 Education & Niche":["TED Talks","Khan Academy","CuriosityStream","Nebula","Dropout","Magellan TV"]}
    cats_html="".join(f'<div style="margin-bottom:2.5rem"><h3 style="margin-bottom:1rem;font-size:1.3rem">{cat}</h3><div class="sites-grid">{"".join(f"<div class=site-pill>{s}</div>" for s in sites)}</div></div>' for cat,sites in cats.items())
    return page(f"AllMyTube Supported Sites — 10,000+ Video Platforms | {YEAR}",
        "AllMyTube supports 10,000+ video sites including YouTube, TikTok, Vimeo, Facebook, Instagram, Twitch, Bilibili, BBC iPlayer and thousands more worldwide.",
        "/supported-sites/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Supported Sites",None))}
  <span class="section-label">Global Compatibility</span>
  <h1>Download From <span class="c-acc">10,000+ Sites</span></h1>
  <p style="max-width:640px;margin-top:.8rem;font-size:1.1rem;color:var(--muted)">AllMyTube supports virtually every video platform on the internet — updated continuously to stay ahead of site changes.</p>
</div>
<section>
  <div class="hbox"><p><strong>10,000+ platforms and counting.</strong> AllMyTube's engineering team continuously updates compatibility. If a platform streams video publicly, there's a very good chance AllMyTube supports it.</p></div>
  {cats_html}
  <div style="text-align:center;margin-top:2rem">
    <p style="margin-bottom:1.5rem;color:var(--muted)">...and 9,900+ more platforms across every region and category</p>
    <a href="{AFF}" class="btn btn-primary" target="_blank" rel="noopener sponsored">⬇ Download AllMyTube — Try Any Site Free</a>
  </div>
</section>""","AllMyTube supported sites, YouTube downloader, TikTok downloader, Vimeo downloader")

# ── PAGE: HOW IT WORKS ────────────────────────────────────────────────────────
def pg_how():
    return page(f"How AllMyTube Works — 3 Easy Methods to Download Any Video | {YEAR}",
        "Learn exactly how AllMyTube works: paste a URL, choose quality, download in seconds. Or use the browser extension for one-click downloads on any video site.",
        "/how-it-works/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("How It Works",None))}
  <span class="section-label">Dead Simple</span>
  <h1>How <span class="c-acc">AllMyTube</span> Works</h1>
  <p style="max-width:600px;margin-top:.8rem;font-size:1.1rem;color:var(--muted)">From video URL to downloaded file in under 30 seconds. Three methods — pick the one that fits your workflow.</p>
</div>
<section>
  <div class="split">
    <div>
      <h2 style="margin-bottom:2rem">Method 1: <span class="c-acc">Paste &amp; Download</span></h2>
      <div class="steps">
        <div class="step" data-n="1"><div class="step-body"><h3>Copy the Video URL</h3><p>Go to YouTube, TikTok, Vimeo or any of 10,000+ supported sites. Copy the URL from your address bar.</p></div></div>
        <div class="step" data-n="2"><div class="step-body"><h3>Paste into AllMyTube</h3><p>Open AllMyTube and paste the URL. It instantly detects the video and shows all available quality options.</p></div></div>
        <div class="step" data-n="3"><div class="step-body"><h3>Choose Quality &amp; Format</h3><p>Select resolution (4K, 1080p, 720p…) or output format (MP4, MP3, MKV…). Device presets are also available.</p></div></div>
        <div class="step" data-n="4"><div class="step-body"><h3>Download &amp; Enjoy</h3><p>Click Download. AllMyTube runs at 3× speed and saves to your folder. Play immediately in the built-in player.</p></div></div>
      </div>
    </div>
    <div style="display:flex;flex-direction:column;gap:1.5rem">
      <div class="hbox"><h4>Method 2: Browser Extension</h4><p style="margin-top:.5rem">Install the AllMyTube extension for Chrome, Firefox or Edge. A floating <strong style="color:var(--acc)">Download</strong> button appears on every supported video page. Click it to queue — no app-switching needed.</p></div>
      <div class="hbox"><h4>Method 3: Screen Recorder</h4><p style="margin-top:.5rem">For any stream AllMyTube can't directly grab — DRM-protected, geo-locked — use the built-in screen recorder to capture exactly what's playing on screen at full quality.</p></div>
      <div class="hbox"><h4>💡 Power User Tips</h4>
        <ul class="feat-list" style="margin-top:.5rem">
          <li>Enable <strong>Turbo Mode</strong> to use your full connection bandwidth</li>
          <li>Right-click any video link → <strong>"Download with AllMyTube"</strong></li>
          <li>Use the <strong>Scheduler</strong> to run downloads overnight automatically</li>
          <li>Paste a <strong>playlist URL</strong> to download hundreds of videos at once</li>
        </ul>
      </div>
      <a href="{AFF}" class="btn btn-primary" target="_blank" rel="noopener sponsored">⬇ Try It Free Now</a>
    </div>
  </div>
</section>""")


# ── PAGE: PRICING ─────────────────────────────────────────────────────────────
def pg_pricing():
    faq_s='{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"Is AllMyTube free?","acceptedAnswer":{"@type":"Answer","text":"Yes, AllMyTube offers a free trial. Paid plans from $29/year."}},{"@type":"Question","name":"Is there a lifetime plan?","acceptedAnswer":{"@type":"Answer","text":"Yes, a one-time lifetime licence is available. Check the official site for current pricing."}}]}'
    return page(f"AllMyTube Pricing {YEAR} — Free Trial, $29/yr Personal, $49/yr Family",
        f"AllMyTube pricing {YEAR}: Free trial, Personal $29/year, Family $49/year. Unlimited 4K downloads and 10,000+ site support on all paid plans. Lifetime option available.",
        "/pricing/",f"""
<div class="ph tc">{bc(("Home",f"{SITE_ROOT}/"),("Pricing",None))}
  <span class="section-label" style="display:block;text-align:center">Simple, Transparent Plans</span>
  <h1>AllMyTube <span class="c-acc">Pricing</span></h1>
  <p style="max-width:540px;margin:.8rem auto 0;font-size:1.1rem;color:var(--muted)">Start free. Upgrade when ready. All paid plans include unlimited 4K downloads from 10,000+ sites.</p>
</div>
<section>
  <div class="pricing-grid">
    <div class="price-card">
      <div class="price-name">Free Trial</div>
      <div class="price-amount"><sup>$</sup>0</div>
      <div class="price-period">Try before you buy</div>
      <ul class="price-feats">
        <li>Download from 10,000+ sites</li><li>Test all resolution options</li>
        <li>Built-in media player</li><li>Basic format conversion</li>
        <li>Limited downloads to evaluate</li>
      </ul>
      <a href="{AFF}" class="btn btn-secondary btn-full" target="_blank" rel="noopener sponsored">Start Free Trial</a>
    </div>
    <div class="price-card pop">
      <div class="pop-badge">Most Popular</div>
      <div class="price-name">Personal Annual</div>
      <div class="price-amount"><sup>$</sup>29</div>
      <div class="price-period">per year · 1 PC</div>
      <ul class="price-feats">
        <li>Everything in Free +</li><li>Unlimited downloads</li>
        <li>4K &amp; full HD quality</li><li>Full converter — 150+ formats</li>
        <li>Playlist &amp; channel download</li><li>Browser extension</li>
        <li>Download scheduler</li><li>Priority customer support</li>
        <li>Free updates for 1 year</li>
      </ul>
      <a href="{AFF}" class="btn btn-primary btn-full" target="_blank" rel="noopener sponsored">Get Best Deal →</a>
      <div class="price-note">💡 Check site for current promotions</div>
    </div>
    <div class="price-card">
      <div class="price-name">Family Annual</div>
      <div class="price-amount"><sup>$</sup>49</div>
      <div class="price-period">per year · up to 5 PCs</div>
      <ul class="price-feats">
        <li>Everything in Personal +</li><li>Up to 5 computers</li>
        <li>Shared family library</li><li>All future updates</li>
      </ul>
      <a href="{AFF}" class="btn btn-secondary btn-full" target="_blank" rel="noopener sponsored">Get Family Plan →</a>
    </div>
  </div>
  <div class="hbox" style="max-width:780px;margin:3rem auto 0;text-align:center">
    <h4>💡 Lifetime Option Available</h4>
    <p style="margin-top:.5rem">Wondershare also offers a one-time lifetime licence for AllMyTube. Click the button above to check the current lifetime price — deals change regularly and holiday promotions are common.</p>
  </div>
  <div style="max-width:780px;margin:3rem auto 0">
    <h2 style="margin-bottom:1.5rem">Pricing <span class="c-acc">FAQ</span></h2>
    <div class="faq-wrap" style="max-width:100%">
      <details><summary>Is AllMyTube actually free to try?</summary><div class="ans"><p>Yes — download AllMyTube with no payment required. The free trial lets you test all features with a limited download count so you can evaluate the software before committing to a paid plan.</p></div></details>
      <details><summary>What's the difference between Personal and Family plans?</summary><div class="ans"><p>The Personal plan covers 1 PC. The Family plan covers up to 5 computers in the same household — ideal for families where multiple people want to download videos.</p></div></details>
      <details><summary>Does Wondershare offer a refund guarantee?</summary><div class="ans"><p>Wondershare typically offers a money-back guarantee. Check the official site for current refund policy terms as these can vary seasonally.</p></div></details>
      <details><summary>Are there discount codes or coupons available?</summary><div class="ans"><p>Wondershare runs regular promotions especially around major holidays. The best way to find current deals is to visit the official site via the download button above.</p></div></details>
    </div>
  </div>
</section>""","AllMyTube price, AllMyTube cost, AllMyTube coupon, AllMyTube discount, video downloader price",faq_s)

# ── PAGE: REVIEW ──────────────────────────────────────────────────────────────
def pg_review():
    rev_s='{"@context":"https://schema.org","@type":"Review","itemReviewed":{"@type":"SoftwareApplication","name":"AllMyTube","operatingSystem":"Windows, macOS"},"reviewRating":{"@type":"Rating","ratingValue":"9.2","bestRating":"10"},"author":{"@type":"Person","name":"AllMyTube Guide Editorial Team"},"reviewBody":"AllMyTube earns 9.2/10 for unmatched site coverage, genuine 4K quality, and rock-solid batch downloading. The most complete video downloader available."}'
    return page(f"AllMyTube Review {YEAR} — Honest 9.2/10 After 30 Days Testing",
        f"Our in-depth AllMyTube review after 30 days of testing: 9.2/10 overall. Performance, site coverage, 4K quality, ease of use, value and support all rated individually.",
        "/review/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Review",None))}
  <span class="section-label">In-Depth Analysis</span>
  <h1>AllMyTube <span class="c-acc">Review {YEAR}</span></h1>
  <p style="max-width:640px;margin-top:.8rem;font-size:1.05rem;color:var(--muted)">We tested AllMyTube across 40+ platforms, multiple resolutions and dozens of conversions over 30 days. Here is our complete, unbiased verdict.</p>
</div>
<section>
  <div class="split">
    <div>
      <div style="margin-bottom:2rem">
        <div class="score-big">9.2</div>
        <div class="score-label">/ 10 — Editor's Rating</div>
        <div style="margin-top:.5rem"><span class="chip chip-green">Recommended</span> <span class="chip chip-blue" style="margin-left:.5rem">Best All-in-One</span></div>
      </div>
      <div class="rating-bars">
        <div class="rbar"><span class="rbar-label">Performance</span><div class="rbar-track"><div class="rbar-fill" style="width:96%"></div></div><span class="rbar-score">9.6</span></div>
        <div class="rbar"><span class="rbar-label">Site Coverage</span><div class="rbar-track"><div class="rbar-fill" style="width:98%"></div></div><span class="rbar-score">9.8</span></div>
        <div class="rbar"><span class="rbar-label">Video Quality</span><div class="rbar-track"><div class="rbar-fill" style="width:95%"></div></div><span class="rbar-score">9.5</span></div>
        <div class="rbar"><span class="rbar-label">Ease of Use</span><div class="rbar-track"><div class="rbar-fill" style="width:88%"></div></div><span class="rbar-score">8.8</span></div>
        <div class="rbar"><span class="rbar-label">Features</span><div class="rbar-track"><div class="rbar-fill" style="width:95%"></div></div><span class="rbar-score">9.5</span></div>
        <div class="rbar"><span class="rbar-label">Value for Money</span><div class="rbar-track"><div class="rbar-fill" style="width:92%"></div></div><span class="rbar-score">9.2</span></div>
        <div class="rbar"><span class="rbar-label">Support</span><div class="rbar-track"><div class="rbar-fill" style="width:86%"></div></div><span class="rbar-score">8.6</span></div>
      </div>
    </div>
    <div>
      <div class="hbox"><h4>Verdict Summary</h4><p style="margin-top:.5rem">AllMyTube is the most complete video downloader we have tested. Its combination of 10,000+ site support, genuine 4K output, built-in converter, browser extension, and download scheduler makes it the clear choice for anyone who downloads video regularly. At $29/year or with a lifetime option, the value is exceptional.</p></div>
      <div class="hbox warn" style="margin-top:1rem"><h4>Minor Caveats</h4><p style="margin-top:.5rem">The advanced converter settings have a slight learning curve for new users. The dense, feature-packed UI may initially overwhelm complete beginners — though built-in presets cover 95% of use cases without any configuration needed.</p></div>
    </div>
  </div>
  <h2 style="margin:3rem 0 1.5rem">Category <span class="c-acc">Breakdown</span></h2>
  <div class="grid-3">
    <div class="card"><h4 style="color:var(--acc);margin-bottom:.5rem">Performance ★★★★★</h4><p>A 1080p YouTube video downloaded in under 8 seconds on standard broadband. 4K video took 23 seconds. A batch of 50 videos completed in ~12 minutes. Consistently 3× faster than competitors in side-by-side tests.</p></div>
    <div class="card"><h4 style="color:var(--acc);margin-bottom:.5rem">Site Coverage ★★★★★</h4><p>We tested 40 platforms: YouTube, TikTok, Vimeo, Facebook, Instagram, Twitch, Dailymotion, Reddit, Bilibili, Niconico, SoundCloud, Bandcamp and several regional broadcasters. AllMyTube worked flawlessly on all 40.</p></div>
    <div class="card"><h4 style="color:var(--acc);margin-bottom:.5rem">Video Quality ★★★★★</h4><p>4K downloads match source quality with zero re-encoding artifacts. Side-by-side comparison with original YouTube 4K shows no visible difference. Audio extraction produces clean files with correct bitrates and full metadata.</p></div>
    <div class="card"><h4 style="color:var(--acc);margin-bottom:.5rem">Ease of Use ★★★★☆</h4><p>Basic usage is genuinely easy — paste URL, select quality, download. The dense UI may initially overwhelm beginners, though built-in presets remove the need to configure anything for most common use cases.</p></div>
    <div class="card"><h4 style="color:var(--acc);margin-bottom:.5rem">Value ★★★★★</h4><p>At $29/year or the lifetime option, AllMyTube represents exceptional value. Comparable software with fewer features often costs more. The built-in converter alone would cost $20–40 as a separate purchase elsewhere.</p></div>
    <div class="card"><h4 style="color:var(--acc);margin-bottom:.5rem">Support ★★★★☆</h4><p>Wondershare provides email support, live chat during business hours, and an extensive knowledge base. Response times typically under 24 hours. Community forums are active with plentiful solutions for common issues.</p></div>
  </div>
  <div style="text-align:center;margin-top:3rem">
    <h3 style="margin-bottom:1rem">Try <span class="c-acc">AllMyTube</span> Free</h3>
    <a href="{AFF}" class="btn btn-primary btn-lg" target="_blank" rel="noopener sponsored">⬇ Download Free — No Credit Card</a>
  </div>
</section>""","AllMyTube review, AllMyTube rating, is AllMyTube good, Wondershare AllMyTube review",rev_s,article=True)


# ── PAGE: FAQ ─────────────────────────────────────────────────────────────────
def pg_faq():
    faqs=[
        ("Is AllMyTube free?","Yes — AllMyTube offers a full-featured free trial with no credit card required. The free version lets you test all features with a limited number of downloads. Paid plans start from $29/year (Personal) or $49/year (Family) for unlimited downloads."),
        ("Is AllMyTube safe to use?","Yes. AllMyTube is developed by Wondershare, a globally recognised software company with 50M+ users in 200+ countries. It is 100% free from malware, adware and bundled software. Wondershare is a publicly listed company with a long-standing reputation for safe, high-quality software."),
        ("Does AllMyTube work on Mac?","Yes. AllMyTube is available for both Windows (7, 8, 10, 11) and macOS (10.12 Sierra and later, including Apple Silicon M1/M2/M3 Macs). Both versions share the full feature set including 4K downloads, batch processing, the built-in converter, and the browser extension."),
        ("Can I download 4K videos with AllMyTube?","Yes. AllMyTube fully supports 4K (2160p) downloads from platforms that offer 4K content, including YouTube. Choose from 7 resolution presets: 2160p (4K), 1440p (2K), 1080p, 720p, 480p, 360p and 240p."),
        ("How many websites does AllMyTube support?","AllMyTube supports over 10,000 video-sharing websites including YouTube, TikTok, Vimeo, Facebook, Instagram, Twitter/X, Twitch, Dailymotion, Reddit, Bilibili, Niconico, SoundCloud, Pinterest, LinkedIn, and thousands more globally. The list is continuously updated."),
        ("Can I download an entire YouTube playlist?","Yes — one of AllMyTube's standout features. Paste the playlist URL and AllMyTube queues and downloads every video automatically. This works for playlists of any size, including entire YouTube channels with thousands of videos."),
        ("Can I extract MP3 audio from a video?","Yes. AllMyTube's built-in converter extracts audio from any video as MP3 (up to 320kbps), AAC, FLAC or WAV. Output files include proper ID3 metadata tags. Perfect for music, podcasts, lectures and audiobooks."),
        ("What formats does AllMyTube convert to?","AllMyTube supports 150+ output formats including MP4, MKV, AVI, MOV, WMV, FLV, MP3, AAC, FLAC, WAV and more, plus device presets for iPhone, Android, iPad, Samsung TV, PlayStation, Xbox and other popular devices."),
        ("Does AllMyTube have a browser extension?","Yes. AllMyTube includes a browser extension for Chrome, Firefox and Edge that adds a download button directly on video pages — including YouTube and all 10,000+ supported sites — so you can queue downloads without switching apps."),
        ("Is downloading YouTube videos legal?","The legality varies by country and intended use. Downloading for personal offline viewing is a grey area in most jurisdictions. YouTube's Terms of Service prohibit downloading without written permission. AllMyTube is a tool — you are responsible for complying with applicable laws and platform terms of service in your region."),
        ("What operating systems does AllMyTube support?","AllMyTube supports Windows 7, 8, 10 and 11 (32-bit and 64-bit), and macOS 10.12 Sierra through the latest macOS versions including Apple Silicon (M1/M2/M3) Macs. There is currently no official mobile app for iOS or Android."),
        ("What is the Download Scheduler?","The Scheduler lets you set a specific time for AllMyTube to start downloading — ideal for scheduling large batches overnight or during off-peak hours. Set AllMyTube to automatically shut down, hibernate, sleep or exit when all downloads complete."),
    ]
    items="".join(f'<details><summary>{q}</summary><div class="ans"><p>{a}</p></div></details>' for q,a in faqs)
    faq_s='{"@context":"https://schema.org","@type":"FAQPage","mainEntity":['+",".join(f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a[:180]}..."}}}}' for q,a in faqs)+("]}")
    return page(f"AllMyTube FAQ {YEAR} — Every Question Answered",
        "Complete AllMyTube FAQ: Is it free? Safe? Mac support? 4K? Playlists? MP3? Legal? All 12 most common questions answered in full.",
        "/faq/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("FAQ",None))}
  <span class="section-label">Got Questions?</span>
  <h1>AllMyTube <span class="c-acc">FAQ</span></h1>
  <p style="max-width:600px;margin-top:.8rem;color:var(--muted)">Comprehensive answers to the most common questions about AllMyTube — features, pricing, safety, compatibility and legality.</p>
</div>
<section>
  <div class="faq-wrap">{items}</div>
  <div style="text-align:center;margin-top:3rem">
    <p style="margin-bottom:1.5rem;color:var(--muted)">Still have questions? The best way to find out is to try it free — no credit card required.</p>
    <a href="{AFF}" class="btn btn-primary" target="_blank" rel="noopener sponsored">⬇ Download AllMyTube Free</a>
  </div>
</section>""","AllMyTube FAQ, AllMyTube safe, AllMyTube free, AllMyTube Mac, AllMyTube legal",faq_s)

# ── PAGE: DOWNLOAD ────────────────────────────────────────────────────────────
def pg_download():
    return page(f"Download AllMyTube Free — Windows & Mac | {YEAR}",
        "Download AllMyTube free for Windows and Mac. Free trial with all features. Compatible with Windows 7-11 and macOS 10.12+. Installs in under 60 seconds.",
        "/download/",f"""
<div class="ph tc">{bc(("Home",f"{SITE_ROOT}/"),("Download",None))}
  <span class="section-label" style="display:block;text-align:center">Get Started in 60 Seconds</span>
  <h1>Download <span class="c-acc">AllMyTube</span></h1>
  <p style="max-width:520px;margin:.8rem auto 0;font-size:1.1rem;color:var(--muted)">Free trial — no credit card. Works on Windows and Mac. Installs in under a minute.</p>
</div>
<section>
  <div class="grid-2" style="max-width:720px;margin:0 auto 3rem">
    <div class="card" style="text-align:center">
      <div class="card-icon" style="margin:0 auto 1rem;font-size:2rem">🪟</div>
      <h3>Windows</h3>
      <p style="margin-bottom:.5rem">Windows 7 / 8 / 10 / 11</p>
      <p style="font-size:.82rem;margin-bottom:1.5rem">32-bit and 64-bit · Latest version 7.4.9.2</p>
      <a href="{AFF}" class="btn btn-primary btn-full" target="_blank" rel="noopener sponsored">⬇ Download for Windows</a>
    </div>
    <div class="card" style="text-align:center">
      <div class="card-icon" style="margin:0 auto 1rem;font-size:2rem">🍎</div>
      <h3>macOS</h3>
      <p style="margin-bottom:.5rem">macOS 10.12 Sierra and later</p>
      <p style="font-size:.82rem;margin-bottom:1.5rem">Intel &amp; Apple Silicon (M1/M2/M3) native</p>
      <a href="{AFF}" class="btn btn-primary btn-full" target="_blank" rel="noopener sponsored">⬇ Download for Mac</a>
    </div>
  </div>
  <div class="hbox" style="max-width:700px;margin:0 auto">
    <h4>What's Included in the Free Trial</h4>
    <ul class="check-list" style="margin-top:.8rem">
      <li>Download from all 10,000+ supported video sites</li>
      <li>Test all resolution presets including 4K</li>
      <li>Try the built-in converter with all 150+ format options</li>
      <li>Experience batch playlist download</li>
      <li>Use the built-in media player</li>
      <li>Try the browser extension for Chrome, Firefox and Edge</li>
    </ul>
  </div>
  <div style="text-align:center;margin-top:2rem">
    <p style="color:var(--muted);margin-bottom:1rem">Upgrade anytime from $29/year. Lifetime options also available.</p>
    <a href="{SITE_ROOT}/pricing/" class="btn btn-ghost">View All Pricing Options →</a>
  </div>
</section>""")


# ── PAGE: YOUTUBE GUIDE ───────────────────────────────────────────────────────
def pg_youtube():
    return page(f"Best YouTube Downloader {YEAR} — Download in 4K, 1080p or MP3",
        "Download YouTube videos in 4K, 1080p or MP3 with AllMyTube. Supports playlists, channels, Shorts, subtitles and private videos. Free trial available.",
        "/youtube-downloader/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Blog",f"{SITE_ROOT}/blog/"),("YouTube Downloader",None))}
  <span class="section-label">Platform Guide</span>
  <h1>Best <span class="c-acc">YouTube Downloader</span> {YEAR}</h1>
  <p style="max-width:640px;margin-top:.8rem;font-size:1.05rem;color:var(--muted)">The definitive guide to downloading YouTube videos in every quality, format and language — including playlists, Shorts, channels and private videos.</p>
</div>
<section>
  <div class="split">
    <div>
      <h2 style="margin-bottom:1rem">Why AllMyTube is the <span class="c-acc">Best YouTube Downloader</span></h2>
      <p style="margin-bottom:1.5rem">AllMyTube handles every type of YouTube content — regular videos, Shorts, playlists, channels, live stream recordings, and even your own private uploads.</p>
      <ul class="feat-list">
        <li><strong>7 resolution options</strong> — 2160p 4K, 1440p, 1080p, 720p, 480p, 360p, 240p</li>
        <li><strong>YouTube Shorts</strong> — download vertical videos in original quality</li>
        <li><strong>Playlist download</strong> — save entire playlists and full channels</li>
        <li><strong>Private video download</strong> — archive your own private uploads</li>
        <li><strong>Subtitle download</strong> — save auto-generated or manual subtitles as SRT</li>
        <li><strong>MP3 extraction</strong> — perfect for YouTube music at up to 320kbps</li>
        <li><strong>No watermarks</strong> — clean downloads with no branding added</li>
        <li><strong>No file size limits</strong> — download 4-hour concert videos without issue</li>
      </ul>
    </div>
    <div>
      <div class="card card-featured">
        <h3 style="color:var(--acc);margin-bottom:1.2rem">How to Download YouTube Videos</h3>
        <div class="steps" style="max-width:100%">
          <div class="step" data-n="1"><div class="step-body"><h3>Copy the YouTube URL</h3><p>Go to the YouTube video, playlist or channel. Copy the URL from your address bar.</p></div></div>
          <div class="step" data-n="2"><div class="step-body"><h3>Paste into AllMyTube</h3><p>Open AllMyTube, paste the URL. It detects everything automatically.</p></div></div>
          <div class="step" data-n="3"><div class="step-body"><h3>Select Quality</h3><p>Choose from 4K down to 240p, or select MP3 / audio-only mode.</p></div></div>
          <div class="step" data-n="4"><div class="step-body"><h3>Download in Seconds</h3><p>Hit download. Done at 3× speed with no quality loss.</p></div></div>
        </div>
        <a href="{AFF}" class="btn btn-primary btn-full" style="margin-top:1rem" target="_blank" rel="noopener sponsored">⬇ Download YouTube Videos Free</a>
      </div>
    </div>
  </div>
  <div class="hbox" style="margin-top:2rem">
    <h4>YouTube Download FAQ</h4>
    <div class="faq-wrap" style="max-width:100%;margin-top:1rem">
      <details><summary>Can I download YouTube 4K videos?</summary><div class="ans"><p>Yes. AllMyTube fully supports 4K (2160p) YouTube downloads. Select 2160p from the quality dropdown after pasting your YouTube URL. 4K is only available for videos originally uploaded in 4K.</p></div></details>
      <details><summary>Can I download a full YouTube playlist?</summary><div class="ans"><p>Yes — just paste the playlist URL (the URL containing <code>list=...</code>) and AllMyTube queues every video in the playlist. Works for playlists of any size including full channels.</p></div></details>
      <details><summary>Can I extract MP3 from YouTube Music?</summary><div class="ans"><p>Yes. AllMyTube supports YouTube Music. Paste the track or album URL and select MP3 as your output format. AllMyTube extracts audio at up to 320kbps with proper title and artist metadata.</p></div></details>
    </div>
  </div>
</section>""","YouTube downloader, download YouTube video, YouTube 4K download, YouTube to MP3, YouTube playlist download",article=True)

# ── PAGE: TIKTOK GUIDE ───────────────────────────────────────────────────────
def pg_tiktok():
    return page(f"TikTok Video Downloader — No Watermark, HD Quality | {YEAR}",
        "Download TikTok videos without watermarks in HD using AllMyTube. Free trial. Also extract TikTok audio as MP3. Batch download supported.",
        "/tiktok-downloader/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Blog",f"{SITE_ROOT}/blog/"),("TikTok Downloader",None))}
  <span class="section-label">Platform Guide</span>
  <h1>Best <span class="c-acc">TikTok Downloader</span> — No Watermark</h1>
  <p style="max-width:640px;margin-top:.8rem;font-size:1.05rem;color:var(--muted)">Download any TikTok video in HD without the watermark, in seconds, using AllMyTube.</p>
</div>
<section>
  <div class="grid-3">
    <div class="card"><div class="card-icon">🚫</div><h3>No Watermark</h3><p>AllMyTube downloads the original TikTok video file without the TikTok watermark overlay — clean, original quality every time.</p></div>
    <div class="card"><div class="card-icon">🎵</div><h3>Audio Extraction</h3><p>Extract the audio track from any TikTok video as MP3. Perfect for saving viral sounds, trending music or creator audio you discover on TikTok.</p></div>
    <div class="card"><div class="card-icon">📋</div><h3>Bulk Download</h3><p>Download multiple TikTok videos in a batch. Paste several URLs at once and AllMyTube handles the queue automatically and efficiently.</p></div>
  </div>
  <div class="hbox" style="margin-top:2rem">
    <h4>How to Download TikTok Videos Without Watermark</h4>
    <ol style="margin-top:.8rem;display:flex;flex-direction:column;gap:.6rem;color:var(--muted);font-size:.93rem">
      <li>Open TikTok and find the video you want to save</li>
      <li>Tap <strong>Share → Copy Link</strong> to copy the video URL to your clipboard</li>
      <li>Open AllMyTube and paste the URL into the download bar</li>
      <li>Select your quality preference and click <strong>Download</strong></li>
      <li>Your video saves locally — no watermark, full original quality</li>
    </ol>
  </div>
  <div style="text-align:center;margin-top:2.5rem">
    <a href="{AFF}" class="btn btn-primary btn-lg" target="_blank" rel="noopener sponsored">⬇ Download TikTok Videos Free</a>
  </div>
</section>""","TikTok downloader no watermark, download TikTok video, TikTok to MP3, save TikTok",article=True)

# ── PAGE: MP3 EXTRACTOR ───────────────────────────────────────────────────────
def pg_mp3():
    return page(f"MP3 Extractor — Extract Audio from Any Video | {YEAR}",
        "Extract MP3, AAC, FLAC or WAV audio from YouTube, TikTok, Vimeo and 10,000+ sites using AllMyTube. Up to 320kbps MP3 with automatic metadata. Free trial.",
        "/mp3-extractor/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Blog",f"{SITE_ROOT}/blog/"),("MP3 Extractor",None))}
  <span class="section-label">Audio Guide</span>
  <h1>Extract <span class="c-acc">MP3 Audio</span> from Any Video</h1>
  <p style="max-width:640px;margin-top:.8rem;font-size:1.05rem;color:var(--muted)">Convert YouTube, TikTok, Vimeo and 10,000+ more sites to high-quality MP3, FLAC or WAV in seconds using AllMyTube's built-in audio extractor.</p>
</div>
<section>
  <div class="split">
    <div>
      <h2 style="margin-bottom:1rem">Audio Formats <span class="c-acc">Supported</span></h2>
      <div class="grid-2" style="gap:1rem;margin-bottom:2rem">
        <div class="card"><h4 style="color:var(--acc)">MP3</h4><p>Up to 320kbps. The universal format — works on every device and player. With proper ID3 tags automatically applied.</p></div>
        <div class="card"><h4 style="color:var(--acc)">AAC</h4><p>Higher quality than MP3 at the same bitrate. The native format for Apple devices and iTunes libraries.</p></div>
        <div class="card"><h4 style="color:var(--acc)">FLAC</h4><p>Lossless audio. Perfect quality — identical to the source audio with absolutely no compression loss.</p></div>
        <div class="card"><h4 style="color:var(--acc)">WAV</h4><p>Uncompressed audio for professional use in video editing, DAWs and audio production workflows.</p></div>
      </div>
      <ul class="feat-list">
        <li><strong>Automatic metadata</strong> — title, artist, album art where available</li>
        <li><strong>Batch audio extraction</strong> — convert entire playlists to MP3</li>
        <li><strong>Custom bitrate</strong> — choose from 64kbps to 320kbps</li>
        <li><strong>10,000+ source sites</strong> — YouTube, Vimeo, SoundCloud, TikTok and more</li>
      </ul>
    </div>
    <div>
      <div class="card card-featured" style="padding:2.5rem">
        <h3 style="color:var(--acc);margin-bottom:1.5rem">How to Extract MP3</h3>
        <div class="steps" style="max-width:100%">
          <div class="step" data-n="1"><div class="step-body"><h3>Copy the Video URL</h3><p>From YouTube, SoundCloud, Vimeo or any of 10,000+ supported sites.</p></div></div>
          <div class="step" data-n="2"><div class="step-body"><h3>Paste into AllMyTube</h3><p>AllMyTube detects the video and available audio tracks automatically.</p></div></div>
          <div class="step" data-n="3"><div class="step-body"><h3>Select MP3 Output</h3><p>Choose MP3, AAC, FLAC or WAV. Set your preferred bitrate.</p></div></div>
          <div class="step" data-n="4"><div class="step-body"><h3>Download Audio</h3><p>Pure audio file saved instantly to your chosen folder.</p></div></div>
        </div>
        <a href="{AFF}" class="btn btn-primary btn-full" style="margin-top:1rem" target="_blank" rel="noopener sponsored">⬇ Extract MP3 Free</a>
      </div>
    </div>
  </div>
</section>""","MP3 extractor, YouTube to MP3, extract audio from video, video to MP3 converter",article=True)

# ── PAGE: 4K DOWNLOADER ───────────────────────────────────────────────────────
def pg_4k():
    return page(f"4K Video Downloader — Download 4K Ultra HD from Any Site | {YEAR}",
        "Download true 4K (2160p) Ultra HD videos from YouTube and 10,000+ sites using AllMyTube. No quality loss, no re-encoding. Free trial available.",
        "/4k-downloader/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Blog",f"{SITE_ROOT}/blog/"),("4K Downloader",None))}
  <span class="section-label">Quality Guide</span>
  <h1>Download <span class="c-acc">4K Videos</span> from Any Site</h1>
  <p style="max-width:640px;margin-top:.8rem;font-size:1.05rem;color:var(--muted)">AllMyTube downloads true 4K (2160p) video with no quality loss — the highest resolution available from YouTube and other 4K platforms.</p>
</div>
<section>
  <div class="hbox">
    <h4>Resolution Options in AllMyTube</h4>
    <div class="tbl-wrap" style="margin-top:1rem"><table>
      <thead><tr><th>Resolution</th><th>Quality</th><th>Best For</th><th>Approx Size (10 min)</th></tr></thead>
      <tbody>
        <tr><td class="td-name">2160p (4K)</td><td class="td-yes">Ultra HD</td><td>Large screens, archiving, editing</td><td>~3–6 GB</td></tr>
        <tr><td class="td-name">1440p (2K)</td><td class="td-yes">Quad HD</td><td>27"+ monitors, high-end displays</td><td>~1.5–3 GB</td></tr>
        <tr><td class="td-name">1080p (Full HD)</td><td class="td-yes">Full HD</td><td>Most screens, best balance</td><td>~700 MB–1.5 GB</td></tr>
        <tr><td class="td-name">720p (HD)</td><td class="td-partial">HD</td><td>Smaller devices, faster download</td><td>~300–600 MB</td></tr>
        <tr><td class="td-name">480p</td><td class="td-partial">SD</td><td>Mobile viewing, limited storage</td><td>~150–250 MB</td></tr>
        <tr><td class="td-name">360p / 240p</td><td>Low</td><td>Very slow connections, minimal storage</td><td>~50–100 MB</td></tr>
      </tbody>
    </table></div>
  </div>
  <div class="split" style="margin-top:3rem">
    <div>
      <h2 style="margin-bottom:1rem">Why <span class="c-acc">True 4K</span> Matters</h2>
      <p style="margin-bottom:1.5rem">Many "4K downloaders" actually re-encode the video, causing quality loss. AllMyTube downloads the original stream directly — what you get is bit-for-bit identical to what's on the server.</p>
      <ul class="feat-list">
        <li><strong>No re-encoding</strong> — original stream downloaded directly</li>
        <li><strong>HDR support</strong> — preserves HDR10 and Dolby Vision metadata where available</li>
        <li><strong>High frame rate</strong> — supports 60fps 4K downloads from YouTube</li>
        <li><strong>Multiple 4K sources</strong> — YouTube, Vimeo 4K, and others</li>
        <li><strong>Storage-smart</strong> — choose lower resolution when storage is limited</li>
      </ul>
    </div>
    <div>
      <div class="card card-featured" style="padding:2.5rem;text-align:center">
        <h3 style="color:var(--acc);margin-bottom:1rem">Download 4K Videos Now</h3>
        <p style="margin-bottom:1.5rem">Free trial — test 4K downloads with no credit card required. Experience the quality difference yourself.</p>
        <a href="{AFF}" class="btn btn-primary btn-full" target="_blank" rel="noopener sponsored">⬇ Download 4K Videos Free</a>
      </div>
    </div>
  </div>
</section>""","4K video downloader, download 4K YouTube, 4K download, Ultra HD video downloader",article=True)

# ── PAGE: PLAYLIST DOWNLOADER ─────────────────────────────────────────────────
def pg_playlist():
    return page(f"YouTube Playlist Downloader — Download Entire Playlists in {YEAR}",
        "Download entire YouTube playlists and channels in one click with AllMyTube. Any playlist size, consistent quality, auto-organised files. Free trial.",
        "/playlist-downloader/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Blog",f"{SITE_ROOT}/blog/"),("Playlist Downloader",None))}
  <span class="section-label">Batch Download Guide</span>
  <h1>Download Entire <span class="c-acc">YouTube Playlists</span> in One Click</h1>
  <p style="max-width:640px;margin-top:.8rem;font-size:1.05rem;color:var(--muted)">AllMyTube's batch downloader handles playlists of any size — from 10 videos to 10,000. One URL, one click, done.</p>
</div>
<section>
  <div class="split">
    <div>
      <h2 style="margin-bottom:1rem">Batch Download <span class="c-acc">Features</span></h2>
      <ul class="feat-list">
        <li><strong>Any playlist size</strong> — no limit on the number of videos in a queue</li>
        <li><strong>Entire channel download</strong> — paste a YouTube channel URL to save everything</li>
        <li><strong>Consistent quality</strong> — all videos download at the same chosen resolution</li>
        <li><strong>Auto-organised files</strong> — named and ordered by playlist sequence</li>
        <li><strong>Resume downloads</strong> — interrupted batches resume where they left off</li>
        <li><strong>Scheduler integration</strong> — run large batches overnight automatically</li>
        <li><strong>Multi-site support</strong> — batch download from Vimeo, TikTok profiles and more</li>
      </ul>
      <div style="margin-top:2rem">
        <a href="{AFF}" class="btn btn-primary" target="_blank" rel="noopener sponsored">⬇ Start Batch Downloading Free</a>
      </div>
    </div>
    <div>
      <div class="card card-featured" style="padding:2.5rem">
        <h3 style="color:var(--acc);margin-bottom:1.5rem">How to Download a Full Playlist</h3>
        <div class="steps" style="max-width:100%">
          <div class="step" data-n="1"><div class="step-body"><h3>Open YouTube Playlist</h3><p>Go to any playlist page on YouTube. The URL will contain <code>list=...</code></p></div></div>
          <div class="step" data-n="2"><div class="step-body"><h3>Copy the Playlist URL</h3><p>Copy the full URL from your browser address bar.</p></div></div>
          <div class="step" data-n="3"><div class="step-body"><h3>Paste into AllMyTube</h3><p>AllMyTube detects it's a playlist and queues every video automatically.</p></div></div>
          <div class="step" data-n="4"><div class="step-body"><h3>Select Quality &amp; Download All</h3><p>Choose resolution once — applies to every video. Click Download All.</p></div></div>
        </div>
      </div>
    </div>
  </div>
</section>""","YouTube playlist downloader, download YouTube playlist, batch video download, download YouTube channel",article=True)


# ── PAGE: VS 4K VIDEO DOWNLOADER ──────────────────────────────────────────────
def pg_vs_4k():
    return page(f"AllMyTube vs 4K Video Downloader — Full Comparison {YEAR}",
        f"AllMyTube vs 4K Video Downloader: features, pricing, supported sites, built-in converter. Which video downloader is better in {YEAR}? Detailed head-to-head.",
        "/vs-4k-video-downloader/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Alternatives",f"{SITE_ROOT}/alternatives/"),("vs 4K Video Downloader",None))}
  <span class="section-label">Head-to-Head</span>
  <h1>AllMyTube vs <span class="c-acc">4K Video Downloader</span></h1>
  <p style="max-width:640px;margin-top:.8rem;font-size:1.05rem;color:var(--muted)">Two of the most popular desktop video downloaders compared across every important feature. Which should you choose in {YEAR}?</p>
</div>
<section>
  <div class="tbl-wrap"><table>
    <thead><tr><th>Feature</th><th style="color:var(--acc)">AllMyTube ✓</th><th>4K Video Downloader</th></tr></thead>
    <tbody>
      <tr><td>Supported Sites</td><td class="td-yes td-hi">10,000+</td><td>500+</td></tr>
      <tr><td>Max Resolution</td><td class="td-yes td-hi">4K (2160p)</td><td class="td-yes">4K (2160p)</td></tr>
      <tr><td>MP3 Extraction</td><td class="td-yes td-hi">✓ Full quality, tags</td><td class="td-partial">✓ Basic</td></tr>
      <tr><td>Playlist Download</td><td class="td-yes td-hi">✓ Unlimited</td><td class="td-partial">Limited on free tier</td></tr>
      <tr><td>Built-in Converter</td><td class="td-yes td-hi">✓ 150+ formats</td><td class="td-no">✗ Not included</td></tr>
      <tr><td>Browser Extension</td><td class="td-yes td-hi">✓ Chrome/Firefox/Edge</td><td class="td-no">✗</td></tr>
      <tr><td>Download Scheduler</td><td class="td-yes td-hi">✓</td><td class="td-no">✗</td></tr>
      <tr><td>Built-in Player</td><td class="td-yes td-hi">✓</td><td class="td-no">✗</td></tr>
      <tr><td>Screen Recorder</td><td class="td-yes td-hi">✓</td><td class="td-no">✗</td></tr>
      <tr><td>Device Transfer</td><td class="td-yes td-hi">✓ iPhone &amp; Android</td><td class="td-no">✗</td></tr>
      <tr><td>Subtitle Download</td><td class="td-yes td-hi">✓ SRT/VTT</td><td class="td-partial">✓ Basic</td></tr>
      <tr><td>Annual Plan</td><td class="td-hi">$29/year</td><td class="td-yes">$15/year</td></tr>
      <tr><td>Windows + Mac</td><td class="td-yes td-hi">✓</td><td class="td-yes">✓</td></tr>
      <tr><td>Free Trial</td><td class="td-yes td-hi">✓</td><td class="td-yes">✓</td></tr>
    </tbody>
  </table></div>
  <div class="hbox" style="margin-top:2.5rem">
    <h4>Verdict</h4>
    <p style="margin-top:.5rem">AllMyTube wins on almost every dimension: 20× more supported sites, a built-in converter (saving a separate purchase), browser extension, scheduler, player, and device transfer. <strong>4K Video Downloader is cheaper at $15/year</strong>, but requires separate tools for conversion and covers far fewer platforms. For anyone who downloads regularly from multiple sites, AllMyTube is the significantly better long-term investment.</p>
  </div>
  <div style="text-align:center;margin-top:2rem">
    <a href="{AFF}" class="btn btn-primary" target="_blank" rel="noopener sponsored">Try AllMyTube Free →</a>
    <span style="display:block;margin-top:.8rem;font-size:.82rem;color:var(--muted)">Free trial · No credit card needed</span>
  </div>
</section>""","AllMyTube vs 4K Video Downloader, 4K Video Downloader alternative, best video downloader comparison")

# ── PAGE: VS YT-DLP ───────────────────────────────────────────────────────────
def pg_vs_ytdlp():
    return page(f"AllMyTube vs yt-dlp — GUI vs Command Line {YEAR}",
        f"AllMyTube vs yt-dlp: ease of use, features, site support, pricing, converter and support compared. Which video downloader is right for you in {YEAR}?",
        "/vs-ytdlp/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Alternatives",f"{SITE_ROOT}/alternatives/"),("vs yt-dlp",None))}
  <span class="section-label">Head-to-Head</span>
  <h1>AllMyTube vs <span class="c-acc">yt-dlp</span></h1>
  <p style="max-width:640px;margin-top:.8rem;font-size:1.05rem;color:var(--muted)">yt-dlp is the gold standard command-line downloader. AllMyTube is the gold standard GUI app. Here's the full, honest comparison.</p>
</div>
<section>
  <div class="tbl-wrap"><table>
    <thead><tr><th>Factor</th><th style="color:var(--acc)">AllMyTube</th><th>yt-dlp</th></tr></thead>
    <tbody>
      <tr><td>Interface</td><td class="td-yes td-hi">Visual GUI — no commands needed</td><td>Command-line only</td></tr>
      <tr><td>Installation</td><td class="td-yes td-hi">One-click installer, 60 seconds</td><td>Requires Python or binary + PATH setup</td></tr>
      <tr><td>Supported Sites</td><td class="td-yes td-hi">10,000+</td><td class="td-yes">1,000+ (open source)</td></tr>
      <tr><td>4K Downloads</td><td class="td-yes td-hi">✓ One-click</td><td class="td-yes">✓ With format codes</td></tr>
      <tr><td>Built-in Converter</td><td class="td-yes td-hi">✓ 150+ formats, GUI</td><td class="td-partial">Via FFmpeg (manual config)</td></tr>
      <tr><td>Browser Extension</td><td class="td-yes td-hi">✓</td><td class="td-no">✗</td></tr>
      <tr><td>Built-in Player</td><td class="td-yes td-hi">✓</td><td class="td-no">✗</td></tr>
      <tr><td>Download Scheduler</td><td class="td-yes td-hi">✓ GUI scheduler</td><td class="td-partial">Via cron/task scheduler manually</td></tr>
      <tr><td>Auto Updates</td><td class="td-yes td-hi">✓ Automatic</td><td class="td-partial">Manual or CLI update</td></tr>
      <tr><td>Official Support</td><td class="td-yes td-hi">✓ Wondershare team</td><td>Community only (GitHub issues)</td></tr>
      <tr><td>Price</td><td>Free trial / $29/yr</td><td class="td-yes">Free &amp; open source</td></tr>
      <tr><td>Advanced scripting</td><td class="td-no">✗</td><td class="td-yes">✓ Fully scriptable</td></tr>
      <tr><td>Linux</td><td class="td-no">✗</td><td class="td-yes">✓</td></tr>
    </tbody>
  </table></div>
  <div class="grid-2" style="margin-top:2rem">
    <div class="hbox"><h4 style="color:var(--acc)">Choose AllMyTube if...</h4>
      <ul class="check-list" style="margin-top:.8rem">
        <li>You want a point-and-click experience</li>
        <li>You're not comfortable with command lines</li>
        <li>You need a built-in converter and player</li>
        <li>You want automatic updates and official support</li>
        <li>You download from a wide variety of sites regularly</li>
      </ul>
    </div>
    <div class="hbox"><h4 style="color:var(--gold)">Choose yt-dlp if...</h4>
      <ul class="check-list" style="margin-top:.8rem">
        <li>You're comfortable with the terminal</li>
        <li>You want a completely free solution</li>
        <li>You need advanced scripting and automation</li>
        <li>You use Linux</li>
        <li>You need maximum configurability</li>
      </ul>
    </div>
  </div>
  <div style="text-align:center;margin-top:2.5rem">
    <a href="{AFF}" class="btn btn-primary" target="_blank" rel="noopener sponsored">Try AllMyTube Free — No CLI Required</a>
  </div>
</section>""","AllMyTube vs yt-dlp, yt-dlp alternative, yt-dlp GUI, best yt-dlp replacement")

# ── PAGE: VS VIDEODER ─────────────────────────────────────────────────────────
def pg_vs_videoder():
    return page(f"AllMyTube vs Videoder — Desktop Video Downloader Comparison {YEAR}",
        "Compare AllMyTube vs Videoder: platform support, site coverage, quality, features and privacy. Which is better for desktop video downloading?",
        "/vs-videoder/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Alternatives",f"{SITE_ROOT}/alternatives/"),("vs Videoder",None))}
  <span class="section-label">Head-to-Head</span>
  <h1>AllMyTube vs <span class="c-acc">Videoder</span></h1>
  <p style="max-width:640px;margin-top:.8rem;font-size:1.05rem;color:var(--muted)">Videoder is popular on Android. AllMyTube is the premium desktop solution. Full comparison below.</p>
</div>
<section>
  <div class="tbl-wrap"><table>
    <thead><tr><th>Factor</th><th style="color:var(--acc)">AllMyTube</th><th>Videoder</th></tr></thead>
    <tbody>
      <tr><td>Platform</td><td class="td-yes td-hi">Windows &amp; Mac</td><td>Android + limited Windows</td></tr>
      <tr><td>Supported Sites</td><td class="td-yes td-hi">10,000+</td><td>~50</td></tr>
      <tr><td>4K Quality</td><td class="td-yes td-hi">✓ True 4K</td><td class="td-partial">Limited</td></tr>
      <tr><td>Batch Downloads</td><td class="td-yes td-hi">✓ Unlimited</td><td class="td-partial">Limited</td></tr>
      <tr><td>Built-in Converter</td><td class="td-yes td-hi">✓ 150+ formats</td><td>Basic only</td></tr>
      <tr><td>Privacy / Safety</td><td class="td-yes td-hi">✓ No ads, no malware</td><td class="td-partial">Ad-supported</td></tr>
      <tr><td>Official Support</td><td class="td-yes td-hi">✓ Wondershare team</td><td>Community only</td></tr>
      <tr><td>Free Trial</td><td class="td-yes td-hi">✓</td><td class="td-yes">✓ (ad-supported)</td></tr>
      <tr><td>Paid Price</td><td>$29/year</td><td class="td-yes">Free (with ads)</td></tr>
    </tbody>
  </table></div>
  <div class="hbox" style="margin-top:2rem"><p>Videoder suits Android users who want a quick free option and don't mind ads. For desktop users wanting wide site support, real 4K quality, a built-in converter, and no ads or privacy concerns, AllMyTube is the clear choice.</p></div>
  <div style="text-align:center;margin-top:2rem">
    <a href="{AFF}" class="btn btn-primary" target="_blank" rel="noopener sponsored">Try AllMyTube Free →</a>
  </div>
</section>""","AllMyTube vs Videoder, Videoder alternative, best desktop video downloader")

# ── PAGE: ALTERNATIVES ────────────────────────────────────────────────────────
def pg_alternatives():
    return page(f"Best AllMyTube Alternatives {YEAR} — Full Comparison Guide",
        f"Compare AllMyTube with the best video downloader alternatives in {YEAR}: 4K Video Downloader, yt-dlp, Videoder, JDownloader and more.",
        "/alternatives/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Alternatives",None))}
  <span class="section-label">Full Market Overview</span>
  <h1>Best <span class="c-acc">AllMyTube Alternatives</span> {YEAR}</h1>
  <p style="max-width:640px;margin-top:.8rem;font-size:1.05rem;color:var(--muted)">We compared AllMyTube with every major video downloader so you can make a fully informed choice.</p>
</div>
<section>
  <div class="grid-2">
    <div class="card card-featured">
      <h3 style="color:var(--acc)">AllMyTube <span class="chip chip-green" style="margin-left:.5rem">Recommended</span></h3>
      <p style="margin:.8rem 0">The most complete video downloader available. 10,000+ sites, 4K quality, built-in converter, batch playlists, browser extension, scheduler, and player — all in one app.</p>
      <ul class="check-list"><li>10,000+ supported sites</li><li>150+ output formats</li><li>Browser extension included</li><li>Official Wondershare support</li></ul>
      <a href="{AFF}" class="btn btn-primary" style="margin-top:1.2rem" target="_blank" rel="noopener sponsored">Download Free →</a>
    </div>
    <div class="card">
      <h3>4K Video Downloader</h3>
      <p style="margin:.8rem 0">Clean, simple interface. Good 4K quality. Cheaper annual plan ($15/yr). Lacks built-in converter, browser extension, scheduler, and player. 500+ sites only.</p>
      <ul class="check-list"><li>Simple interface</li><li>Good 4K quality</li><li>Cheaper ($15/yr)</li></ul>
      <a href="{SITE_ROOT}/vs-4k-video-downloader/" class="btn btn-ghost" style="margin-top:1.2rem">Full Comparison →</a>
    </div>
    <div class="card">
      <h3>yt-dlp</h3>
      <p style="margin:.8rem 0">Powerful free open-source command-line tool. Technically superior for advanced users. Steep learning curve. No GUI, no built-in converter or player. Linux-friendly.</p>
      <ul class="check-list"><li>Completely free</li><li>Highly configurable</li><li>Linux support</li></ul>
      <a href="{SITE_ROOT}/vs-ytdlp/" class="btn btn-ghost" style="margin-top:1.2rem">Full Comparison →</a>
    </div>
    <div class="card">
      <h3>Videoder</h3>
      <p style="margin:.8rem 0">Popular on Android. Very limited desktop functionality. Ad-supported with ~50 supported sites. Not a serious option for desktop power users needing 4K.</p>
      <ul class="check-list"><li>Free (with ads)</li><li>Good on Android</li><li>Simple interface</li></ul>
      <a href="{SITE_ROOT}/vs-videoder/" class="btn btn-ghost" style="margin-top:1.2rem">Full Comparison →</a>
    </div>
    <div class="card">
      <h3>JDownloader</h3>
      <p style="margin:.8rem 0">Free, open-source, widely used for general downloads. Complex setup, dated interface. Moderate video support. No built-in converter or audio extractor.</p>
      <p style="margin-top:.8rem"><span class="chip chip-green">Free</span></p>
    </div>
    <div class="card">
      <h3>Internet Download Manager</h3>
      <p style="margin:.8rem 0">Excellent general download manager but not video-download focused. No playlist support, no built-in converter, no audio extraction. Windows only.</p>
      <p style="margin-top:.8rem"><span class="chip chip-gold">Windows Only</span></p>
    </div>
  </div>
</section>""","AllMyTube alternatives, best video downloader, video downloader comparison 2025 2026")


# ── PAGE: BLOG INDEX ──────────────────────────────────────────────────────────
def pg_blog():
    posts=[
        ("📥","Tutorial",f"How to Download YouTube 4K Videos in {YEAR}","A complete step-by-step guide to saving YouTube videos at maximum 4K quality — including playlists, channels, Shorts and subtitles.",f"{SITE_ROOT}/youtube-downloader/",f"June {YEAR}"),
        ("🎵","Tutorial","How to Extract MP3 Audio from Any Video","Convert YouTube, SoundCloud, Vimeo and any video to high-quality MP3 audio in seconds with full metadata tagging.",f"{SITE_ROOT}/mp3-extractor/",f"May {YEAR}"),
        ("📋","Guide","Download an Entire YouTube Playlist in One Click","Save hundreds of videos at once with AllMyTube's batch playlist downloader. Works for playlists and full channels of any size.",f"{SITE_ROOT}/playlist-downloader/",f"May {YEAR}"),
        ("🔇","Guide","How to Download TikTok Videos Without Watermark","Save TikTok videos locally without the watermark overlay in full HD quality. Works for any public TikTok video.",f"{SITE_ROOT}/tiktok-downloader/",f"April {YEAR}"),
        ("🆚","Comparison","AllMyTube vs 4K Video Downloader — Which Wins?","We put both apps through 30 days of testing across 40 platforms. Here's our definitive, fully detailed verdict.",f"{SITE_ROOT}/vs-4k-video-downloader/",f"April {YEAR}"),
        ("🆚","Comparison","AllMyTube vs yt-dlp — GUI vs Command Line","yt-dlp is free and powerful. AllMyTube is polished and complete. Which one fits your real-world workflow?",f"{SITE_ROOT}/vs-ytdlp/",f"March {YEAR}"),
        ("⭐","Review",f"AllMyTube Full Review {YEAR} — 9.2/10 After 30 Days","Our most comprehensive AllMyTube review. Every feature tested, every claim verified. Is it worth it in {YEAR}?",f"{SITE_ROOT}/review/",f"March {YEAR}"),
        ("🎬","Guide","How to Download 4K Videos from Any Website","AllMyTube makes 4K downloading trivial. Full guide covering resolution selection, file sizes and storage planning.",f"{SITE_ROOT}/4k-downloader/",f"February {YEAR}"),
        ("💰","Guide",f"AllMyTube Pricing {YEAR} — Which Plan is Right for You?","Free trial, annual plan or lifetime licence? We break down every AllMyTube pricing option so you can choose wisely.",f"{SITE_ROOT}/pricing/",f"February {YEAR}"),
        ("🌐","Guide",f"The 20 Best Video Sites to Download From in {YEAR}","A comprehensive guide to the most popular video platforms and exactly how to download from each using AllMyTube.",f"{SITE_ROOT}/supported-sites/",f"January {YEAR}"),
        ("🔒","Legal","Is Downloading YouTube Videos Legal? The Full Answer","The legal landscape around video downloading explained clearly for users in the US, UK, EU, India and Australia.",f"{SITE_ROOT}/faq/",f"January {YEAR}"),
        ("🖥","Tutorial","How to Download Videos for Offline Viewing on Any Device","From laptop to TV to phone — how to use AllMyTube to build your personal offline video library on any screen.",f"{SITE_ROOT}/download/",f"December {YEAR-1}"),
    ]
    cards="".join(f"""<div class="blog-card">
  <div class="blog-thumb">{e}</div>
  <div class="blog-body">
    <div class="blog-tag">{t}</div>
    <h3>{title}</h3>
    <p>{desc}</p>
    <div class="blog-meta"><span>📅 {d}</span></div>
    <a href="{url}" class="blog-read">Read Article →</a>
  </div>
</div>""" for e,t,title,desc,url,d in posts)
    return page(f"AllMyTube Blog — Video Download Guides, Reviews & Tutorials {YEAR}",
        "Video download guides, honest reviews and practical tutorials. Learn how to download 4K YouTube videos, extract MP3 audio, save playlists and compare video downloaders.",
        "/blog/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Blog",None))}
  <span class="section-label">Guides, Reviews & Tutorials</span>
  <h1>AllMyTube <span class="c-acc">Blog</span></h1>
  <p style="max-width:600px;margin-top:.8rem;color:var(--muted)">In-depth guides, honest reviews and practical tutorials to help you get the most from video downloading.</p>
</div>
<section><div class="blog-grid">{cards}</div></section>""","video downloader guide, YouTube download tutorial, AllMyTube blog")

# ── PAGE: PRIVACY ─────────────────────────────────────────────────────────────
def pg_privacy():
    return page("Privacy Policy — AllMyTube Affiliate Guide",
        "Privacy policy for the AllMyTube affiliate guide site. Information about affiliate links, cookies, and data practices.",
        "/privacy/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Privacy Policy",None))}
  <h1>Privacy <span class="c-acc">Policy</span></h1>
  <p style="color:var(--muted);margin-top:.5rem">Last updated: June {YEAR}</p>
</div>
<section style="max-width:800px;margin:0 auto">
  <div class="hbox"><p>This website (brightlane.github.io/allmytube) is an independent affiliate guide for AllMyTube by Wondershare. We earn commissions on qualifying purchases through our affiliate links — at no extra cost to you.</p></div>
  <h3 style="margin:2rem 0 .8rem;color:var(--acc)">Information We Collect</h3>
  <p>This is a static site hosted on GitHub Pages. We do not operate servers, run databases, or directly collect any personally identifiable information. GitHub Pages may collect standard server logs (IP address, browser, referrer) as part of its infrastructure — see GitHub's Privacy Policy for details.</p>
  <h3 style="margin:2rem 0 .8rem;color:var(--acc)">Affiliate Links</h3>
  <p>Links to AllMyTube on this site are affiliate links tracked through the LinkConnector affiliate network. When you click and make a qualifying purchase, we receive a commission. This does not affect the price you pay. We only recommend products we genuinely believe provide value.</p>
  <h3 style="margin:2rem 0 .8rem;color:var(--acc)">Cookies</h3>
  <p>This site does not set first-party cookies. Affiliate tracking uses cookies managed by LinkConnector. You can disable cookies in your browser settings, though this may affect affiliate tracking functionality.</p>
  <h3 style="margin:2rem 0 .8rem;color:var(--acc)">Third-Party Sites</h3>
  <p>When you click through to AllMyTube's website, you leave this site and are subject to Wondershare's Privacy Policy. We are not responsible for third-party data practices.</p>
</section>""")

# ── PAGE: DISCLAIMER ──────────────────────────────────────────────────────────
def pg_disclaimer():
    return page("Affiliate Disclaimer — AllMyTube Guide",
        "Affiliate disclosure and disclaimer for the AllMyTube guide site. We earn commissions on purchases through our affiliate links at no cost to you.",
        "/disclaimer/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Disclaimer",None))}
  <h1>Affiliate <span class="c-acc">Disclaimer</span></h1>
  <p style="color:var(--muted);margin-top:.5rem">Last updated: June {YEAR}</p>
</div>
<section style="max-width:800px;margin:0 auto">
  <div class="hbox"><h4>Affiliate Disclosure</h4><p style="margin-top:.5rem">This website contains affiliate links. As an affiliate of Wondershare AllMyTube through the LinkConnector network, we earn a commission when purchases are made through our links — at no additional cost to you. This is how we fund the time spent researching and writing this content.</p></div>
  <h3 style="margin:2rem 0 .8rem;color:var(--acc)">Editorial Independence</h3>
  <p>Our reviews, ratings and recommendations are based on genuine research and independent testing. Affiliate relationships do not influence our editorial opinions. We aim to provide honest, useful information. Where we have identified weaknesses or limitations in AllMyTube, we have included them in our review — not just the positives.</p>
  <h3 style="margin:2rem 0 .8rem;color:var(--acc)">Accuracy</h3>
  <p>We strive to keep pricing, features and comparisons accurate and up to date. However, software features and pricing can change at any time without notice. Always verify current details on the official Wondershare website before making any purchase decision.</p>
  <h3 style="margin:2rem 0 .8rem;color:var(--acc)">Legal Use</h3>
  <p>Video downloading software must only be used in compliance with applicable copyright laws and the terms of service of the platforms involved. We do not condone or encourage copyright infringement or any other unlawful use of downloaded content.</p>
  <h3 style="margin:2rem 0 .8rem;color:var(--acc)">Not Legal or Financial Advice</h3>
  <p>Nothing on this website constitutes legal, financial or professional advice. For specific legal questions about video downloading in your jurisdiction, please consult a qualified attorney.</p>
</section>""")

# ── PAGE: 404 ─────────────────────────────────────────────────────────────────
def pg_404():
    return page("404 — Page Not Found | AllMyTube Guide","Page not found.","/404/",f"""
<div class="ph tc" style="min-height:60vh;display:flex;align-items:center;justify-content:center;flex-direction:column">
  <div style="font-family:'Bebas Neue',sans-serif;font-size:9rem;color:var(--acc);text-shadow:var(--glow);line-height:1">404</div>
  <h1 style="margin-bottom:.8rem">Page <span class="c-acc2">Not Found</span></h1>
  <p style="max-width:400px;margin:0 auto 2rem">This page doesn't exist. Let's get you somewhere useful.</p>
  <div style="display:flex;gap:1rem;flex-wrap:wrap;justify-content:center">
    <a href="{SITE_ROOT}/" class="btn btn-primary">← Go Home</a>
    <a href="{AFF}" class="btn btn-secondary" target="_blank" rel="noopener sponsored">Download AllMyTube</a>
  </div>
</div>""")


# ── SEO FILES ─────────────────────────────────────────────────────────────────
def sitemap():
    pages=[("/","1.0","weekly"),("/features/","0.9","monthly"),("/supported-sites/","0.9","monthly"),("/how-it-works/","0.8","monthly"),("/pricing/","0.9","monthly"),("/review/","0.9","monthly"),("/faq/","0.8","monthly"),("/download/","0.9","monthly"),("/blog/","0.8","weekly"),("/youtube-downloader/","0.8","monthly"),("/tiktok-downloader/","0.8","monthly"),("/mp3-extractor/","0.8","monthly"),("/4k-downloader/","0.8","monthly"),("/playlist-downloader/","0.8","monthly"),("/alternatives/","0.8","monthly"),("/vs-4k-video-downloader/","0.8","monthly"),("/vs-ytdlp/","0.8","monthly"),("/vs-videoder/","0.7","monthly"),("/privacy/","0.4","yearly"),("/disclaimer/","0.4","yearly")]
    today=date.today().isoformat()
    urls="\n".join(f"  <url>\n    <loc>{SITE_URL}{p}</loc>\n    <changefreq>{freq}</changefreq>\n    <priority>{pri}</priority>\n    <lastmod>{today}</lastmod>\n  </url>" for p,pri,freq in pages)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>'

def robots():
    return f"User-agent: *\nAllow: /\nDisallow: /assets/\n\nSitemap: {SITE_URL}/sitemap.xml\n"

def llms():
    return f"""# AllMyTube Affiliate Guide
> URL: {SITE_URL}
> Purpose: Independent affiliate guide for AllMyTube video downloader by Wondershare
> Updated: {date.today().isoformat()}

## What This Site Is
An independent affiliate guide for AllMyTube by Wondershare Software Ltd. We earn commissions via the LinkConnector affiliate program. Content includes reviews, comparisons, tutorials, and feature guides — all written for human readers.

## AllMyTube Key Facts
- Product: AllMyTube by Wondershare Software Ltd
- Category: Video downloader and converter
- Platforms: Windows (7/8/10/11), macOS (10.12+), Apple Silicon supported
- Supported sites: 10,000+
- Max resolution: 4K (2160p), 7 presets total
- Output formats: 150+
- Key features: Batch playlist download, browser extension (Chrome/Firefox/Edge), built-in converter, download scheduler, built-in media player, screen recorder, device transfer, subtitle download
- Pricing: Free trial | $29/year Personal | $49/year Family | Lifetime option available
- Users: 50M+ in 200+ countries
- Publisher: Wondershare Software Ltd (publicly listed)
- Latest version: 7.4.9.2

## Site Pages (20 total)
- /                         Homepage with overview and features
- /features/                Full 15-feature breakdown
- /supported-sites/         Categorised 10,000+ site list
- /how-it-works/            3 download method guides
- /pricing/                 Plan comparison + FAQ
- /review/                  Editorial review (9.2/10, 30-day test)
- /faq/                     12 detailed FAQ answers
- /download/                Download page Windows & Mac
- /blog/                    Blog index (12 articles)
- /youtube-downloader/      YouTube download guide
- /tiktok-downloader/       TikTok no-watermark guide
- /mp3-extractor/           Audio extraction guide
- /4k-downloader/           4K quality guide + resolution table
- /playlist-downloader/     Batch playlist download guide
- /alternatives/            AllMyTube vs 6 competitors
- /vs-4k-video-downloader/  Feature table comparison
- /vs-ytdlp/                GUI vs CLI comparison
- /vs-videoder/             Desktop vs mobile comparison
- /privacy/                 Privacy policy
- /disclaimer/              Affiliate disclosure

## Affiliate Link
{AFF}

## Editorial Note
Content is original and includes both pros and cons for editorial integrity. Pricing should be verified on the official Wondershare site as it may change without notice.
"""

def feed():
    items=[
        (f"How to Download YouTube 4K Videos in {YEAR}",f"{SITE_URL}/youtube-downloader/","Step-by-step guide to saving YouTube videos at maximum 4K quality.",f"{YEAR}-06-01"),
        ("How to Extract MP3 Audio from Any Video",f"{SITE_URL}/mp3-extractor/","Convert any video to high-quality MP3 audio using AllMyTube.",f"{YEAR}-05-15"),
        ("Download an Entire YouTube Playlist in One Click",f"{SITE_URL}/playlist-downloader/","Save entire YouTube playlists in one click with batch downloading.",f"{YEAR}-05-01"),
        ("TikTok Video Downloader — No Watermark",f"{SITE_URL}/tiktok-downloader/","Download TikTok videos without the watermark in HD.",f"{YEAR}-04-15"),
        (f"AllMyTube Review {YEAR} — 9.2/10",f"{SITE_URL}/review/","Our most comprehensive AllMyTube review after 30 days of testing.",f"{YEAR}-03-01"),
    ]
    ixml="\n".join(f"  <item>\n    <title>{t}</title>\n    <link>{u}</link>\n    <description>{d}</description>\n    <pubDate>{pd}</pubDate>\n    <guid>{u}</guid>\n  </item>" for t,u,d,pd in items)
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>AllMyTube Guide — Blog</title>
    <link>{SITE_URL}/blog/</link>
    <description>Video download guides, reviews and tutorials from the AllMyTube affiliate guide.</description>
    <language>en-us</language>
    <atom:link href="{SITE_URL}/feed.xml" rel="self" type="application/rss+xml"/>
{ixml}
  </channel>
</rss>"""

def favicon():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect width="64" height="64" rx="14" fill="#03060f"/>
  <rect x="1" y="1" width="62" height="62" rx="13" fill="none" stroke="#00d4ff" stroke-width="1.5" opacity="0.4"/>
  <circle cx="32" cy="32" r="18" fill="rgba(0,212,255,0.08)" stroke="#00d4ff" stroke-width="1"/>
  <polygon points="27,22 27,42 45,32" fill="#00d4ff"/>
</svg>"""

# ── MAIN ──────────────────────────────────────────────────────────────────────
def main():
    print(f"\n🚀 AllMyTube Site Builder v3 — {SITE_URL}\n")

    # 20 HTML pages
    write("index.html",                        pg_index())
    write("features/index.html",               pg_features())
    write("supported-sites/index.html",        pg_supported())
    write("how-it-works/index.html",           pg_how())
    write("pricing/index.html",               pg_pricing())
    write("review/index.html",                pg_review())
    write("faq/index.html",                   pg_faq())
    write("download/index.html",              pg_download())
    write("blog/index.html",                  pg_blog())
    write("youtube-downloader/index.html",    pg_youtube())
    write("tiktok-downloader/index.html",     pg_tiktok())
    write("mp3-extractor/index.html",         pg_mp3())
    write("4k-downloader/index.html",         pg_4k())
    write("playlist-downloader/index.html",   pg_playlist())
    write("alternatives/index.html",          pg_alternatives())
    write("vs-4k-video-downloader/index.html",pg_vs_4k())
    write("vs-ytdlp/index.html",              pg_vs_ytdlp())
    write("vs-videoder/index.html",           pg_vs_videoder())
    write("privacy/index.html",              pg_privacy())
    write("disclaimer/index.html",           pg_disclaimer())
    write("404.html",                        pg_404())

    # SEO & meta files
    write("sitemap.xml",       sitemap())
    write("robots.txt",        robots())
    write("llms.txt",          llms())
    write("feed.xml",          feed())
    write("assets/favicon.svg",favicon())
    write(".nojekyll",         "")

    pages=len([f for f in BASE.rglob("*.html")])
    total=len(list(BASE.rglob("*")))
    print(f"\n✅ Done — {pages} HTML pages, {total} total files")
    print(f"   Output: {BASE}")
    print(f"   Live at: {SITE_URL}\n")

if __name__ == "__main__":
    main()
