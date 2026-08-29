#!/usr/bin/env python3
from build_pages import write_page
from content_home import HOME_BODY
from content_indicators import INDICATORS_BODY, INDICATORS
from content_blackbox import BLACKBOX_BODY
from content_uniqueperf import UNIQUEPERF_BODY
from content_harbornow import HARBORNOW_BODY
from content_dailyalerts import DAILYALERTS_BODY
from content_aboutlime import ABOUTLIME_BODY
from content_alignment import ALIGNMENT_BODY
from content_coherence import COHERENCE_BODY
from content_limeshop import LIMESHOP_BODY
from content_services import SERVICES_BODY
from content_stillskeptical import STILLSKEPTICAL_BODY
from content_privacypolicy import PRIVACYPOLICY_BODY
from content_termsofuse import TERMSOFUSE_BODY

assert len(INDICATORS) == 12

write_page(
    "index.html",
    "Home",
    "Lime Signalworks Classic: the Moneytree platform, loss-prevention-first AI trading assistance, and the 90-Day Promise.",
    HOME_BODY,
)
write_page(
    "technical-indicator-specs.html",
    "Technical Indicator Specs",
    "All 12 Lime indicator formulas and output states, transcribed faithfully from the original Lime Signalworks specs.",
    INDICATORS_BODY,
)
write_page(
    "not-a-black-box.html",
    "Not a Black Box",
    "The LIME Decision Blueprint, testing roadmap, and audit hooks that make LIME a transparent rules-based system, not a black box.",
    BLACKBOX_BODY,
)
write_page(
    "unique-high-performance.html",
    "Unique High-Performance",
    "The official Moneytree manual: top, mid, and lower pane Lime indicators, what each one does and when to use it.",
    UNIQUEPERF_BODY,
)
write_page(
    "harbor-now.html",
    "Harbor Now (Archive)",
    "Lime Classic's own archived Harbor Now explainer: a sample market weather read and the Rosie canon rules.",
    HARBORNOW_BODY,
)
write_page(
    "daily-alerts.html",
    "Daily Alerts",
    "Lime's Daily Alerts: a daily market-weather read, Buy/Exit/Trim follow-through, and the AI's plain-language guidance for the day.",
    DAILYALERTS_BODY,
)
write_page(
    "about-lime.html",
    "About Lime",
    "About Lime Signalworks: transforming financial signals with secure, real-time AI market insights.",
    ABOUTLIME_BODY,
)
write_page(
    "alignment.html",
    "Alignment",
    "Alignment: Lime's self-monitoring watchdog design, the Harbor Routine daily fill workflow, and the Source-first philosophy behind the platform.",
    ALIGNMENT_BODY,
)
write_page(
    "coherence.html",
    "Coherence",
    "Coherence: how money pressure, household stress, and nervous-system load connect, and why clearer decisions start with awareness and honest communication.",
    COHERENCE_BODY,
)
write_page(
    "lime-shop.html",
    "Lime Shop",
    "Lime Shop: charter membership and current promotions, archived as a static descriptive page.",
    LIMESHOP_BODY,
)
write_page(
    "services.html",
    "Services",
    "Lime Signalworks services: Real-Time Market Alerts and Trade Automation Tech, plus the plain-language refund terms and office contact details.",
    SERVICES_BODY,
)
write_page(
    "still-skeptical.html",
    "Still Skeptical",
    "Still Skeptical: Marty's letter to Grandma, a brother's honest business-minded look at LIME, in Noal's own voice.",
    STILLSKEPTICAL_BODY,
)
write_page(
    "privacy-policy.html",
    "Privacy Policy",
    "Lime Signalworks LLC's Privacy Policy: what information is collected, how it is used and shared, and your privacy rights.",
    PRIVACYPOLICY_BODY,
)
write_page(
    "terms-of-use.html",
    "Terms of Use",
    "Lime Signalworks LLC's Terms of Use: site access, account security, user content, content standards, governing law, and subscription terms.",
    TERMSOFUSE_BODY,
)

print("done")
