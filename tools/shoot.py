"""Capturas de dist/ a 400 y 1100 px, claro y oscuro. Avisa si hay scroll horizontal."""
import os, sys
from playwright.sync_api import sync_playwright
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST=os.path.join(ROOT,"dist"); OUT=os.path.join(ROOT,"shots"); os.makedirs(OUT,exist_ok=True)
pages=sys.argv[1:] or [p for p in os.listdir(DIST) if p.endswith(".html")]
with sync_playwright() as p:
    b=p.chromium.launch()
    for name in pages:
        for label,w,dark in (("400",400,False),("400-oscuro",400,True),("1100",1100,False)):
            ctx=b.new_context(viewport={"width":w,"height":900},color_scheme="dark" if dark else "light")
            pg=ctx.new_page(); pg.goto("file://"+os.path.join(DIST,name)); pg.wait_for_timeout(500)
            pg.evaluate("document.querySelectorAll('details').forEach(d=>d.open=true)")
            sw=pg.evaluate("document.documentElement.scrollWidth")
            print(name,label,"OK" if sw<=w else "SCROLL HORIZONTAL %d"%sw)
            pg.screenshot(path=os.path.join(OUT,name.replace('.html','')+"-"+label+".png"),full_page=True); ctx.close()
    b.close()
