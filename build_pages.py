#!/usr/bin/env python3
"""Generates the 5 Lime Classic pages with a shared header/footer/nav.
Run from repo root: python3 build_pages.py
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

PAGES = [
    ("index.html", "Home", "/"),
    ("technical-indicator-specs.html", "Technical Indicator Specs", "/technical-indicator-specs.html"),
    ("not-a-black-box.html", "Not a Black Box", "/not-a-black-box.html"),
    ("unique-high-performance.html", "Unique High-Performance", "/unique-high-performance.html"),
    ("harbor-now.html", "Harbor Now", "/harbor-now.html"),
    ("daily-alerts.html", "Daily Alerts", "/daily-alerts.html"),
    ("about-lime.html", "About Lime", "/about-lime.html"),
    ("alignment.html", "Alignment", "/alignment.html"),
    ("coherence.html", "Coherence", "/coherence.html"),
    ("lime-shop.html", "Lime Shop", "/lime-shop.html"),
    ("services.html", "Services", "/services.html"),
    ("still-skeptical.html", "Still Skeptical", "/still-skeptical.html"),
    ("privacy-policy.html", "Privacy Policy", "/privacy-policy.html"),
    ("terms-of-use.html", "Terms of Use", "/terms-of-use.html"),
]

LOGO_SVG = '''<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2 L14 8 L12 6 L10 8 Z"/><rect x="9" y="14" width="6" height="4" rx="1"/><circle cx="12" cy="9" r="2.2"/></svg>'''


def nav_links(active_file):
    items = [
        ("index.html", "Home"),
        ("technical-indicator-specs.html", "Technical Indicator Specs"),
        ("not-a-black-box.html", "Not a Black Box"),
        ("unique-high-performance.html", "Unique High-Performance"),
        ("harbor-now.html", "Harbor Now"),
        ("daily-alerts.html", "Daily Alerts"),
        ("about-lime.html", "About Lime"),
        ("alignment.html", "Alignment"),
        ("coherence.html", "Coherence"),
        ("lime-shop.html", "Lime Shop"),
        ("services.html", "Services"),
        ("still-skeptical.html", "Still Skeptical"),
        ("privacy-policy.html", "Privacy Policy"),
        ("terms-of-use.html", "Terms of Use"),
    ]
    out = []
    for href, label in items:
        current = ' aria-current="page"' if href == active_file else ""
        out.append(f'<a href="{href}"{current}>{label}</a>')
    return "\n      ".join(out)


def header(active_file):
    return f"""<header>
  <div class="wrap hdr">
    <a class="brand" href="index.html" aria-label="Lime Signalworks Classic home">
      <span class="brand-mark">{LOGO_SVG}</span>
      <span class="word">Lime&nbsp;<b>Signalworks</b> &mdash; Classic</span>
    </a>
    <div class="hdr-actions">
      <div class="hdr-tools">
        <button class="icon-btn" data-translate aria-label="Translate this page">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
        </button>
        <button class="icon-btn" data-theme-toggle aria-label="Switch theme">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>
        </button>
      </div>
    </div>
  </div>
  <nav class="site-nav wrap" aria-label="Lime Classic pages">
      {nav_links(active_file)}
  </nav>
  <div class="sibling-nav wrap" aria-label="Other Lime Signalworks sites">
    <span class="sibling-label">Also from Lime Signalworks</span>
    <a href="https://signals.limesignalworks.com" target="_blank" rel="noopener">Signals (Main Site) &#8599;</a>
    <a href="https://leadership.limesignalworks.com" target="_blank" rel="noopener">Leadership &#8599;</a>
    <a href="https://lime-enterprise-web.vercel.app" target="_blank" rel="noopener">Enterprise &#8599;</a>
  </div>
</header>"""


FOOTER = """<footer>
  <div class="wrap foot-wrap">
    <div class="foot">
      <p class="creed">Different worlds, same problem: how to face market chaos without handing your life to a guru.</p>
      <p class="meta">
        <a href="tel:+13802000288">+1 380-200-0288</a> &nbsp;&middot;&nbsp;
        <a href="mailto:contact@limesignalworks.com">contact@limesignalworks.com</a><br>
        2722 Erie Ave, Suite 219, Cincinnati, OH 45208<br>
        By appointment.
      </p>
      <p class="meta" aria-label="Other Lime Signalworks sites">
        <a href="https://signals.limesignalworks.com" target="_blank" rel="noopener">Lime Signalworks &mdash; Signals (Main Site) &#8599;</a> &nbsp;&middot;&nbsp;
        <a href="https://leadership.limesignalworks.com" target="_blank" rel="noopener">LIME Leadership &#8599;</a> &nbsp;&middot;&nbsp;
        <a href="https://lime-enterprise-web.vercel.app" target="_blank" rel="noopener">LIME Enterprise &#8599;</a>
      </p>
      <p class="copy">&copy; 2026 Lime Signalworks LLC. Loss prevention first. Always. &mdash; Lime Classic archive.</p>
    </div>
  </div>
</footer>"""


def page_shell(title, description, active_file, body_html):
    return f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} · Lime Signalworks Classic</title>
<meta name="description" content="{description}">
<link rel="canonical" href="https://classic.limesignalworks.com/{'' if active_file == 'index.html' else active_file}">
<link rel="stylesheet" href="assets/style.css">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
<link href="https://api.fontshare.com/v2/css?f[]=general-sans@300,400,500,600,700&display=swap" rel="stylesheet">
</head>
<body>
{header(active_file)}
<main>
{body_html}
</main>
{FOOTER}
<script src="assets/site.js"></script>
</body>
</html>
"""


def write_page(filename, title, description, body_html):
    html = page_shell(title, description, filename, body_html)
    path = os.path.join(ROOT, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"wrote {path} ({len(html)} bytes)")
