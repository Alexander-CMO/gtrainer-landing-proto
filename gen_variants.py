#!/usr/bin/env python3
"""Генерация дизайн-вариантов из index.html: вставка override-стилей перед </head>.

Варианты по рекомендациям скилла ui-ux-pro-max:
  A "ai-neon"  - AI purple #7C3AED + pink, лавандовый фон, Plus Jakarta Sans
  B "trust"    - Trust & Authority: navy + blue CTA, Lexend/Source Sans 3, WCAG AAA
  C "dark"     - Dark OLED premium: deep black, violet glow, Inter
"""
import pathlib

HERE = pathlib.Path(__file__).parent
base = (HERE / "index.html").read_text()

VARIANTS = {
    "variant-a-ai-neon.html": """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;700;800&display=swap" rel="stylesheet">
<style id="variant-a">
:root{
  --paper:#FAF5FF;--card:#ffffff;
  --indigo:#7C3AED;--indigo-deep:#6D28D9;--indigo-soft:#F3E8FF;
  --ink:#0F172A;--ink-soft:#475069;--ink-mute:#8B90A5;
  --line:#EFE7FC;--p-ground:#F7F3FD;
}
body,h1,h2,h3{font-family:'Plus Jakarta Sans','Montserrat',sans-serif;}
h1{font-weight:800;}
.pitch{background:linear-gradient(135deg,#7C3AED 0%,#EC4899 100%);}
.form .btn-send{background:linear-gradient(135deg,#7C3AED 0%,#EC4899 100%);}
.proof-num{background:linear-gradient(90deg,#7C3AED,#EC4899);-webkit-background-clip:text;background-clip:text;color:transparent;}
.stage::before{background:radial-gradient(closest-side,rgba(124,58,237,.18),transparent 70%);}
.hot-tag{background:linear-gradient(90deg,#7C3AED,#EC4899);}
.plan.hot{box-shadow:inset 0 0 0 2px #7C3AED;}
.cmp thead th.gt{background:#7C3AED;}
</style>
""",

    "variant-b-trust.html": """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lexend:wght@400;600;700&family=Source+Sans+3:wght@400;600&display=swap" rel="stylesheet">
<style id="variant-b">
:root{
  --paper:#F8FAFC;--card:#ffffff;
  --indigo:#0369A1;--indigo-deep:#075985;--indigo-soft:#E0F2FE;
  --ink:#0F172A;--ink-soft:#334155;--ink-mute:#64748B;
  --line:#E2E8F0;--p-ground:#EEF2F6;
  --speak:#059669;--speak-soft:#D1FAE5;
}
body{font-family:'Source Sans 3','Montserrat',sans-serif;}
h1,h2,h3,.logo,.plan h3,.case b,.step b,.cust b{font-family:'Lexend','Montserrat',sans-serif;}
h1{letter-spacing:-.015em;}
.pcard,.case,.step,.plan,.proof-card,.cust,details.qa{border-radius:14px;}
.phone{border-radius:40px;}
.screen{border-radius:31px;}
.btn,.talkbtn,.chip{border-radius:10px;}
.pstate,.case-tag,.hot-tag,.period,.period button{border-radius:8px;}
.stage::before{background:radial-gradient(closest-side,rgba(3,105,161,.14),transparent 70%);}
.pitch{background:linear-gradient(135deg,#075985 0%,#0F172A 100%);}
.cmp thead th.gt{background:#075985;}
</style>
""",

    "variant-c-dark.html": """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;800&display=swap" rel="stylesheet">
<style id="variant-c">
:root{
  --paper:#07070D;--card:#13131D;
  --indigo:#8B5CF6;--indigo-deep:#A78BFA;--indigo-soft:#241D3D;
  --ink:#F4F4F8;--ink-soft:#B6B8C8;--ink-mute:#7C7F92;
  --line:#23232F;--p-ground:#1B1B27;
  --speak:#34D399;--speak-soft:#0F3324;
  --good:#34D399;--good-bg:#0F2B1D;
  --warn:#F0B24E;--warn-bg:#2D2210;
  --bad:#F87171;--bad-bg:#2F1513;
}
body,h1,h2,h3{font-family:'Inter','Montserrat',sans-serif;}
h1{font-weight:800;letter-spacing:-.03em;}
h1 .accent{color:#A78BFA;text-shadow:0 0 24px rgba(139,92,246,.45);}
.top{background:rgba(7,7,13,.85);border-bottom:1px solid rgba(35,35,47,.7);}
.btn-dark{background:#F4F4F8;color:#0B0B12;}
.btn-dark:hover{box-shadow:0 8px 24px rgba(244,244,248,.18);}
.chip.on{background:#F4F4F8;color:#0B0B12;}
.talkbtn:hover{box-shadow:0 8px 22px rgba(139,92,246,.4);}
.talkbtn{background:var(--indigo);color:#fff;}
.phone:not(.live):not(.report) .talkbtn{animation-name:ctaPulseDark;}
@keyframes ctaPulseDark{
  0%{box-shadow:0 0 0 0 rgba(139,92,246,.5);}
  70%{box-shadow:0 0 0 15px rgba(139,92,246,0);}
  100%{box-shadow:0 0 0 0 rgba(139,92,246,0);}
}
.phone{background:#000;box-shadow:0 30px 70px -20px rgba(0,0,0,.9),0 0 0 1px #23232F,0 0 60px rgba(139,92,246,.12);}
.statusbar{color:#B6B8C8;}
.statusbar .sicons{color:#7C7F92;}
.stage::before{background:radial-gradient(closest-side,rgba(139,92,246,.22),transparent 70%);}
.custom{background:#101018;}
.cust{background:rgba(255,255,255,.04);border-color:rgba(255,255,255,.07);}
.final{background:#101018;}
.bub.ai{background:#1F1F2C;color:#F4F4F8;}
.aback{background:#1F1F2C;}
.aback svg path{stroke:#F4F4F8;}
.goal-head > svg circle{stroke:#F4F4F8;}
.goal-head > svg circle:last-child{fill:#F4F4F8;}
.aplay{background:#1F1F2C;}
.aplay svg path{fill:#F4F4F8;}
.vswitch{background:#2A2A38;}
.vswitch.on{background:var(--speak);}
.cmp thead th.gt{background:#8B5CF6;}
.cmp td.gt{background:#241D3D;}
footer,.foot-grid{border-color:rgba(255,255,255,.08);}
</style>
""",
}

for fname, inject in VARIANTS.items():
    html = base.replace("</head>", inject + "\n</head>")
    (HERE / fname).write_text(html)
    print("ok:", fname)
