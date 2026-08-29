#!/usr/bin/env python3
from build_pages import write_page
from content_home import HOME_BODY
from content_indicators import INDICATORS_BODY, INDICATORS
from content_blackbox import BLACKBOX_BODY
from content_uniqueperf import UNIQUEPERF_BODY
from content_harbornow import HARBORNOW_BODY

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

print("done")
