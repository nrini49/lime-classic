# -*- coding: utf-8 -*-
# Each tuple: (indicator name, symbol, formula RHS, description)
INDICATORS = [
    ("Lime Notify", "NT",
     "Alignment + Momentum \u2212 Exhaustion \u2212 Risk",
     "Buy when NT is strong, Trim when it softens, Exit when it breaks down."),
    ("Lime Leaders Squeezed", "LT",
     "Leader Strength + Squeeze Pressure + Breakout Momentum \u2212 Exhaustion \u2212 Risk",
     "Buy when leading names are tightly coiled and breaking out, Trim when the move is still alive but losing force, Exit when leadership fails or the squeeze release breaks down."),
    ("Lime Index Watcher", "IT",
     "Index Trend + Breadth Support + Participation \u2212 Exhaustion \u2212 Risk",
     "Buy when the major indexes are trending with broad support, Trim when the trend is still up but breadth weakens, Exit when index trend and participation break down."),
    ("Lime Intraday PowerScan", "PT",
     "Intraday Strength + Volume Confirmation + Relative Momentum \u2212 Exhaustion \u2212 Risk",
     "Buy when intraday strength and volume are expanding together, Trim when momentum is still positive but starts to fade, Exit when the move loses force or risk overtakes the setup."),
    ("Lime Multi-Sector Rebound Dashboard", "RT",
     "Sector Breadth + Rebound Strength + Rotation Support \u2212 Exhaustion \u2212 Risk",
     "Buy when multiple sectors rebound together with improving participation, Trim when the rebound continues but narrows, Exit when sector breadth fades and the rebound loses support."),
    ("Lime Not-Hot Scanner", "HT",
     "Quiet Relative Strength + Early Accumulation + Emerging Momentum \u2212 Exhaustion \u2212 Risk",
     "Buy when quiet names begin outperforming before they become obvious, Trim when the early move is still intact but losing freshness, Exit when the hidden strength fades or the setup breaks down."),
    ("Lime Exhaustion", "ET",
     "Stretch from Trend + Momentum Extremes + Volatility Expansion \u2212 Fresh Support",
     "Buy only when exhaustion resets and support returns, Trim when a move becomes extended but has not fully failed, Exit when price is overstretched and the move begins to break down."),
    ("Lime Losers", "LT",
     "Relative Weakness + Downtrend Pressure + Weak Participation \u2212 Recovery Strength",
     "Buy only when weakness meaningfully repairs, Trim when a weak move is still falling but begins to stabilize, Exit when relative weakness and downtrend pressure continue to dominate."),
    ("Lime Personal Heat Map", "HT",
     "Watchlist Strength + Relative Performance + Flow Alignment \u2212 Exhaustion \u2212 Risk",
     "Buy when names on your personal watchlist show broad strength and align with market flow, Trim when leadership remains but starts to cool, Exit when your watchlist weakens and falls out of alignment with the larger tape."),
    ("Lime Market Now", "MT",
     "Market Trend + Breadth Health + Participation Strength \u2212 Exhaustion \u2212 Risk",
     "Buy when the market is rising with broad internal support, Trim when the advance continues but participation weakens, Exit when market internals deteriorate and risk begins to outweigh trend support."),
    ("Lime Weatherstrip", "WT",
     "Timeframe Alignment + Trend Direction + Persistence \u2212 Exhaustion \u2212 Risk",
     "Buy when the 1-day, 6-hour, and 3-hour flows align in the same direction, Trim when alignment starts to loosen, Exit when the strip turns mixed or breaks against the larger trend."),
    ("Lime 7-color Weather Engine", "CT",
     "Trend State + Breadth State + Momentum State \u2212 Exhaustion \u2212 Risk",
     "Buy when the color engine shifts into favorable weather with strong trend and healthy internals, Trim when the weather remains positive but starts to deteriorate, Exit when the color state turns defensive and risk overtakes support."),
]

assert len(INDICATORS) == 12, "must preserve exactly 12 indicators"


def render_indicators_html():
    blocks = []
    for name, symbol, formula, desc in INDICATORS:
        blocks.append(f"""
      <div class="indicator">
        <h3>{name}</h3>
        <p class="ind-states">Output states: Buy, Trim, and Exit only &mdash; each evaluated on the 1-day, 6-hour, and 3-hour frames.</p>
        <p class="ind-formula">{symbol} = {formula}</p>
        <p>{desc}</p>
      </div>""")
    return "\n".join(blocks)


INDICATORS_BODY = """
  <section class="hero sec-plain">
    <div class="wrap">
      <div class="kicker">Signal Structure Analysis</div>
      <h1>Technical Indicator Specs</h1>
      <p class="lede">These specs are here so a serious reader can see the structure behind the signals. Lime is built as a rules-based decision-support system &mdash; <strong>not a black box and not a mystery.</strong></p>
    </div>
  </section>

  <section class="sec-plain">
    <div class="wrap">
      <div class="sec-bar"><h2>Data Integrity Levels</h2></div>
      <div class="sec-body">
        <p>Trust does not mean pretending the market is certain. It means showing the logic, the limits, and the operating states clearly enough that someone can judge the work for themselves.</p>
      </div>
    </div>
  </section>

  <section class="sec-plain">
    <div class="wrap">
      <div class="sec-bar"><h2>Deep Dive: Signal Specs</h2></div>
      <div class="sec-body">
        <p>Each indicator reduces market noise into three outputs only: Buy, Trim, and Exit. Each one is evaluated across the 1-day, 6-hour, and 3-hour frames so the reader can see the same decision structure repeated consistently.</p>
      </div>
    </div>
  </section>

  <section class="sec-plain">
    <div class="wrap">
      <div class="sec-bar"><h2>Core Signal Principles</h2></div>
      <div class="sec-body">
        <p>The short formulas are not meant to hide complexity behind symbols. They are meant to reveal the logic spine in a compact form: alignment, momentum, breadth, exhaustion, and risk working together as one disciplined read.</p>
      </div>
    </div>
  </section>

  <section class="sec-plain">
    <div class="wrap">
      <div class="sec-bar"><h2>Transparent System Design</h2></div>
      <div class="sec-body">
        <p>These tools are designed to be understood before they are trusted. If a reader disagrees with the logic, that is fair; what matters is that the logic is visible.</p>
      </div>
    </div>
  </section>

  <section class="sec-plain">
    <div class="wrap">
      <div class="sec-bar"><h2>Lime Signal Insights</h2></div>
      <p class="sec-sub">Twelve indicators, each with its output states, its short formula, and its buy/trim/exit description.</p>
      <div class="sec-body wide">
__INDICATOR_BLOCKS__
      </div>
    </div>
  </section>

  <section class="sec-plain">
    <div class="wrap">
      <div class="sec-bar"><h2>Smart Signal Insights</h2></div>
      <div class="sec-body">
        <h3>Market &amp; Weather Data</h3>
        <p><em>Lime Market Now &middot; Lime Weatherstrip &middot; Lime Index Watcher</em> &mdash; helps you size today's risk and pace your trading day in under five minutes.</p>
        <h3>Market Trends</h3>
        <p><em>Lime Leaders Squeezed &middot; Lime Multi-Sector Rebound Dashboard &middot; Lime Not-Hot Scanner</em> &mdash; shows where money is really flowing, not just what is loud on financial TV.</p>
        <h3>Risk &amp; Workflow</h3>
        <p><em>Lime Intraday PowerScan &middot; Lime Personal Heat Map &middot; Lime Notify</em> &mdash; keeps your own watchlist, alerts, and intraday plan aligned with the bigger weather, and warns you when the tape is tired so you can trim, protect, or simply do less.</p>
      </div>
    </div>
  </section>
""".replace("__INDICATOR_BLOCKS__", render_indicators_html())
