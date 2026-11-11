"""Construye el sitio a partir de src/.

  python3 tools/build.py            -> dist/  (sitio estático listo para GitHub Pages o Cloudflare Pages)
  python3 tools/build.py artifact   -> dist-artifact/  (fragmentos para publicar como artefactos de Claude)

Los textos pendientes (contacto, URL) se rellenan desde config.json.
"""
import json, os, re, shutil, sys
from html import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cfg = json.load(open(os.path.join(ROOT, "config.json"), encoding="utf-8"))
mode = sys.argv[1] if len(sys.argv) > 1 else "site"
src = os.path.join(ROOT, "src")
out = os.path.join(ROOT, "dist" if mode == "site" else "dist-artifact")
os.makedirs(out, exist_ok=True)
warnings = []

FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
           "%3Crect width='32' height='32' rx='6' fill='%23121B23'/%3E"
           "%3Crect x='7' y='9' width='18' height='4' rx='1' fill='%234DC2B1'/%3E"
           "%3Crect x='7' y='15' width='12' height='4' rx='1' fill='%23E7EDF1'/%3E"
           "%3Crect x='7' y='21' width='8' height='4' rx='1' fill='%23E7EDF1'/%3E%3C/svg%3E")

def fill(s):
    site = cfg["site_url"].rstrip("/")
    repo = cfg["repo_url"]
    contacto = cfg["contacto"] or "Dirección de contacto pendiente de publicar"
    if not cfg["contacto"]: warnings.append("config.json: falta 'contacto'")
    if not site: warnings.append("config.json: falta 'site_url' (la vista previa en WhatsApp necesita la URL absoluta de og.png)")
    s = s.replace("{{CONTACTO}}", escape(contacto))
    s = s.replace("{{AUTOR}}", escape(cfg["autor"]))
    s = s.replace("{{REPO_FRASE}}", (' en <a href="%s" target="_blank" rel="noopener">%s</a>' % (repo, escape(repo.replace("https://", "")))) if repo else "")
    s = s.replace("{{SITE_URL}}", site)
    return s

for name in sorted(os.listdir(src)):
    if not name.endswith(".html"): continue
    frag = fill(open(os.path.join(src, name), encoding="utf-8").read())
    if mode == "artifact":
        for page, url in cfg["artifact_urls"].items():
            if url:
                frag = re.sub(r'href="%s(#[\w-]+)?"' % re.escape(page), lambda m: 'href="%s%s" target="_blank" rel="noopener"' % (url, m.group(1) or ""), frag)
                frag = frag.replace("estado:'%s'" % page, "estado:'%s'" % url)
        open(os.path.join(out, name), "w", encoding="utf-8").write(frag)
        continue
    m = re.match(r"\s*<title>(.*?)</title>\s*", frag, re.S)
    title = m.group(1) if m else "Quién decide"
    body = frag[m.end():] if m else frag
    site = cfg["site_url"].rstrip("/")
    url = site + "/" + ("" if name == "index.html" else name)
    og_img = (site + "/og.png") if site else "og.png"
    head = f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{escape(title)}</title>
<meta name="description" content="{escape(cfg['descripcion'])}">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_ES">
<meta property="og:site_name" content="Quién decide">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(cfg['descripcion'])}">
<meta property="og:image" content="{og_img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
{'<meta property="og:url" content="%s">' % url if site else ''}
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{FAVICON}">
<style>:root{{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}body{{margin:0}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
</head>
<body>
"""
    open(os.path.join(out, name), "w", encoding="utf-8").write(head + body + "</body>\n</html>\n")

if mode == "site":
    shutil.copy(os.path.join(ROOT, "assets", "og.png"), os.path.join(out, "og.png"))
    open(os.path.join(out, ".nojekyll"), "w").close()

for w in sorted(set(warnings)): print("AVISO:", w)
print("Hecho:", out)
