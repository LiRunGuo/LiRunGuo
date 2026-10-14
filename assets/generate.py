"""Generate the animated header and typing SVGs for the GitHub profile README."""
import os
import sys
from xml.sax.saxutils import escape

out = sys.argv[1]
os.makedirs(out, exist_ok=True)

SANS = "'Segoe UI', -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif"
MONO = "SFMono-Regular, Consolas, 'Liberation Mono', Menlo, monospace"

# ---------------------------------------------------------------- header
W, H = 1200, 300


def wave(y, amp, period=300):
    # two screen-widths of wave so a -W translate loops seamlessly
    d = f"M0 {y} "
    for x in range(0, 2 * W, period):
        d += f"Q{x + period / 4} {y - amp} {x + period / 2} {y} T{x + period} {y} "
    return d + f"V{H} H0 Z"


waves = [
    (wave(232, 18), "#3b82f6", 0.25, "14s"),
    (wave(246, 14, 400), "#8b5cf6", 0.30, "10s"),
    (wave(262, 10, 240), "#22d3ee", 0.35, "7s"),
]
wave_svg = "\n".join(
    f'''  <path d="{d}" fill="{c}" fill-opacity="{o}">
    <animateTransform attributeName="transform" type="translate" from="0 0" to="-{W} 0" dur="{dur}" repeatCount="indefinite"/>
  </path>'''
    for d, c, o, dur in waves
)

# a faint grid of "GPU tiles" in the background
tiles = []
for row in range(5):
    for col in range(24):
        x, y = 30 + col * 48, 20 + row * 40
        delay = (row * 7 + col * 3) % 23 / 4
        tiles.append(
            f'<rect x="{x}" y="{y}" width="40" height="32" rx="4" fill="#38bdf8" fill-opacity="0">'
            f'<animate attributeName="fill-opacity" values="0;0.10;0" dur="6s" begin="{delay:.2f}s" repeatCount="indefinite"/></rect>'
        )

header = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Runguo Li — ML Systems for Large Models">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#0b1020"/>
      <stop offset="0.55" stop-color="#151a3a"/>
      <stop offset="1" stop-color="#1e1b4b"/>
    </linearGradient>
    <linearGradient id="title" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#93c5fd"/>
      <stop offset="0.5" stop-color="#c4b5fd"/>
      <stop offset="1" stop-color="#67e8f9"/>
    </linearGradient>
    <clipPath id="frame"><rect width="{W}" height="{H}" rx="18"/></clipPath>
  </defs>
  <g clip-path="url(#frame)">
  <rect width="{W}" height="{H}" fill="url(#bg)"/>
  {"".join(tiles)}
{wave_svg}
  </g>
  <g font-family="{SANS}" text-anchor="middle">
    <text x="{W / 2}" y="112" font-size="68" font-weight="700" fill="url(#title)" opacity="0">Runguo Li
      <animate attributeName="opacity" from="0" to="1" dur="1.2s" fill="freeze"/>
    </text>
    <text x="{W / 2}" y="158" font-size="26" fill="#e2e8f0" opacity="0">ML Systems for Large Models
      <animate attributeName="opacity" from="0" to="1" begin="0.5s" dur="1.2s" fill="freeze"/>
    </text>
    <text x="{W / 2}" y="196" font-size="17" font-family="{MONO}" fill="#94a3b8" opacity="0">M.S. @ UIUC  ·  20 merged upstream PRs  ·  Ph.D. applicant, Fall 2028
      <animate attributeName="opacity" from="0" to="1" begin="1s" dur="1.2s" fill="freeze"/>
    </text>
  </g>
</svg>
'''
open(os.path.join(out, "header.svg"), "w").write(header)

# ---------------------------------------------------------------- typing
LINES = [
    "Streaming MoE experts from disk to GPU",
    "Compressing KV caches for long chain-of-thought",
    "Fixing kernels in PyTorch, vLLM, Triton and LLVM",
    "Applying to Ph.D. programs for Fall 2028",
]
FS, CW = 20, 12.0          # font size and forced advance per character
TYPE, HOLD, ERASE = 0.065, 1.8, 0.025   # seconds per char / hold / per char erased
X0, TH = 64, 52            # text start x, box height
TW = X0 + max(map(len, LINES)) * CW + 40

slots, t = [], 0.0
for line in LINES:
    n = len(line)
    slots.append((t, n))
    t += n * TYPE + HOLD + n * ERASE + 0.3
TOTAL = t

parts = []
for i, ((start, n), line) in enumerate(zip(slots, LINES)):
    # discrete keyframes: width in whole characters over the full cycle
    times, widths = [0.0], [0]
    for k in range(1, n + 1):
        times.append(start + k * TYPE)
        widths.append(k)
    hold_end = start + n * TYPE + HOLD
    for k in range(n - 1, -1, -1):
        times.append(hold_end + (n - k) * ERASE)
        widths.append(k)
    if times[-1] < TOTAL:
        times.append(TOTAL)
        widths.append(0)
    erase_end = hold_end + n * ERASE
    kt = ";".join(f"{x / TOTAL:.5f}" for x in times)
    w_vals = ";".join(f"{w * CW:.1f}" for w in widths)
    x_vals = ";".join(f"{X0 + w * CW:.1f}" for w in widths)
    vis = ";".join("1" if start <= x < erase_end else "0" for x in times)
    parts.append(f'''  <clipPath id="c{i}"><rect x="{X0}" y="0" width="0" height="{TH}">
    <animate attributeName="width" values="{w_vals}" keyTimes="{kt}" dur="{TOTAL:.3f}s" calcMode="discrete" repeatCount="indefinite"/>
  </rect></clipPath>
  <text x="{X0}" y="{TH / 2 + 7}" textLength="{n * CW}" lengthAdjust="spacingAndGlyphs" clip-path="url(#c{i})">{escape(line)}</text>
  <rect class="cursor" x="{X0}" y="{TH / 2 - 11}" width="10" height="22" opacity="0">
    <animate attributeName="x" values="{x_vals}" keyTimes="{kt}" dur="{TOTAL:.3f}s" calcMode="discrete" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="{vis}" keyTimes="{kt}" dur="{TOTAL:.3f}s" calcMode="discrete" repeatCount="indefinite"/>
  </rect>''')

typing = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {TW:.0f} {TH}" width="{TW:.0f}" height="{TH}" role="img" aria-label="{escape(' / '.join(LINES))}">
  <style>
    text {{ font-family: {MONO}; font-size: {FS}px; fill: #e6edf3; }}
    .cursor {{ fill: #58a6ff; }}
  </style>
  <rect width="{TW:.0f}" height="{TH}" rx="10" fill="#0d1117" stroke="#30363d"/>
  <text x="24" y="{TH / 2 + 7}" style="fill:#3fb950;font-weight:700">❯</text>
{chr(10).join(parts)}
</svg>
'''
open(os.path.join(out, "typing.svg"), "w").write(typing)
print(f"typing cycle {TOTAL:.1f}s, width {TW:.0f}")
