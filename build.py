#!/usr/bin/env python3
"""Сборка index.html: инлайн Montserrat woff2 (base64) в template.html."""
import base64
import pathlib

HERE = pathlib.Path(__file__).parent
FONTS = HERE / "fonts"

TOKENS = {
    "__M400L__": "montserrat-400-lat.woff2",
    "__M400C__": "montserrat-400-cyr.woff2",
    "__M500L__": "montserrat-500-lat.woff2",
    "__M500C__": "montserrat-500-cyr.woff2",
    "__M700L__": "montserrat-700-lat.woff2",
    "__M700C__": "montserrat-700-cyr.woff2",
}

html = (HERE / "template.html").read_text()
for token, fname in TOKENS.items():
    b64 = base64.b64encode((FONTS / fname).read_bytes()).decode()
    html = html.replace(token, b64)

out = HERE / "index.html"
out.write_text(html)
assert "__M" not in html, "остались незаменённые токены шрифтов"
print(f"ok: {out} ({out.stat().st_size / 1024:.0f} KB)")
