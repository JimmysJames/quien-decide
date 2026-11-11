"""Genera src/<tema>.html a partir de data/<tema>.json con el diseño de las fichas.

  python3 tools/render.py            -> todos los data/*.json
  python3 tools/render.py empleo     -> solo uno
"""
import json, os, sys, re
from html import escape as e

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS = open(os.path.join(ROOT, "tools", "ficha.css.html"), encoding="utf-8").read()
EXTRA_CSS = """<style>
.aviso{background:var(--accent-soft);border-left:4px solid var(--accent);border-radius:4px;padding:12px 14px;display:flex;flex-direction:column;gap:4px}
.aviso b{font-family:var(--f-display)}
.nada{color:var(--ink-2)}
.nolist{margin:0;padding-left:20px;display:flex;flex-direction:column;gap:4px}
.vote .lbl{font-family:var(--f-mono);font-size:.78rem;color:var(--ink-2)}
.bar .a{background:var(--alt2);color:var(--ink);justify-content:center;padding-inline:0}
details.yg{border-top:0;padding-top:0}
details.yg>summary{display:flex;align-items:baseline;gap:10px;border-bottom:2px solid var(--ink);padding-block:8px 4px;color:var(--ink);text-transform:none;letter-spacing:0;list-style-position:inside}
details.yg>summary .yy{font-family:var(--f-display);font-size:1.25rem;font-weight:800;font-variation-settings:"wdth" 108}
details.yg>summary .yn{font-family:var(--f-mono);font-size:.72rem;color:var(--ink-2);text-transform:uppercase;letter-spacing:.06em}
details.yg[open]>summary{margin-bottom:12px}
details.yg>summary{cursor:pointer;list-style:none}
details.yg>summary::-webkit-details-marker{display:none}
details.yg>summary::before{content:"+";font-family:var(--f-mono);font-size:1rem;color:var(--accent);width:14px;flex:none}
details.yg[open]>summary::before{content:"−"}
.ygi{display:flex;flex-direction:column;gap:14px}
.tl.compact li{padding-bottom:10px}
.tl.compact .t{font-weight:500;font-size:.95rem}
.keys{display:flex;flex-wrap:wrap;gap:4px 14px;font-size:.88rem;color:var(--ink-2)}
.keys i{display:inline-block;width:10px;height:10px;border-radius:2px;margin-right:5px}
.count{font-family:var(--f-mono);font-size:.74rem;font-weight:400;color:var(--ink-2);text-transform:uppercase;letter-spacing:.06em;margin-left:8px}
</style>"""
REVISION = "11 de noviembre de 2026"
MESES = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]
BADGE = {"oficial": ("Oficial", True), "dos_fuentes": ("Prensa · 2 fuentes", False),
         "terceros": ("Resumen de terceros", False), "una_fuente": ("Una sola fuente", False)}
RESULT = {"convalidado": "Convalidado", "derogado": "Derogado: no se convalidó",
          "tomado_en_consideracion": "Admitido a trámite", "rechazado": "Rechazado", "aprobado": "Aprobado",
          "enmienda_rechazada": "Votación sobre las enmiendas de totalidad: rechazadas, el texto sigue adelante",
          "devuelto": "Votación sobre las enmiendas de totalidad: aprobadas, el texto vuelve al Gobierno"}


def fecha(iso):
    if not iso: return ""
    p = iso.split("-")
    if len(p) == 3: return "%d %s %s" % (int(p[2]), MESES[int(p[1]) - 1], p[0])
    if len(p) == 2: return "%s %s" % (MESES[int(p[1]) - 1], p[0])
    return p[0]


def fuentes_html(fs):
    out = []
    for f in fs or []:
        tipo = {"oficial": "Oficial: ", "prensa": "", "terceros": ""}.get(f.get("tipo"), "")
        extra = (", " + fecha(f["fecha"])) if f.get("fecha") else ""
        out.append('<a class="src" href="%s" target="_blank" rel="noopener">%s%s%s</a>' % (
            e(f["url"], quote=True), tipo, e(f.get("nombre", f["url"])), e(extra)))
    return "\n          ".join(out)


def votacion_html(v):
    if not v: return ""
    res = RESULT.get(v.get("resultado"), "")
    a, n, ab = v.get("a_favor"), v.get("en_contra"), v.get("abstenciones") or 0
    parts = []
    if a is not None and n is not None:
        tot = a + n + ab
        lab = "%d a favor, %d en contra%s" % (a, n, (", %d abstenciones" % ab) if ab else "")
        seg = '<span class="y" style="width:%.2f%%">%d a favor</span><span class="n" style="width:%.2f%%">%d en contra</span>' % (
            a * 100 / tot, a, n * 100 / tot, n)
        if ab: seg += '<span class="a" style="width:%.2f%%">%s</span>' % (ab * 100 / tot, ab if ab * 100 / tot > 6 else "")
        parts.append('<div class="vote" role="img" aria-label="%s"><span class="lbl">%s · %s</span><div class="bar">%s</div></div>' % (
            e(lab), e(fecha(v.get("fecha"))), e(res), seg))
    else:
        parts.append('<p class="vote"><span class="lbl">%s · %s · las fuentes no dan el recuento</span></p>' % (e(fecha(v.get("fecha"))), e(res)))
    g = v.get("grupos_en_contra") or []
    if g: parts.append("<p>En contra: %s.</p>" % e(", ".join(sorted(g, key=str.lower))))
    return "\n      ".join(parts)


def fact_html(h):
    lab, of = BADGE.get(h.get("verificacion"), ("Una sola fuente", False))
    badge = '<span class="badge%s">%s</span>' % (" of" if of else "", e(lab))
    limit = ('\n      <p class="limit">%s</p>' % e(h["no_sabemos"])) if h.get("no_sabemos") else ""
    det = ('<p>%s</p>\n          ' % e(h["detalle"])) if h.get("detalle") else ""
    return """    <article class="fact">
      <div class="meta"><time>%s</time>%s</div>
      <h3>%s</h3>
      <p class="plain">%s</p>
      %s%s
      <details>
        <summary>Detalle y fuentes</summary>
        <div class="in">
          %s%s
        </div>
      </details>
    </article>""" % (e(fecha(h["fecha"])), badge, e(h["titulo"]), e(h["frase_llana"]),
                     votacion_html(h.get("votacion")), limit, det, fuentes_html(h.get("fuentes")))


def by_year(hs):
    """Tarjetas agrupadas por año cuando hay muchas."""
    if len(hs) <= 8:
        return "\n".join(fact_html(h) for h in hs)
    years = sorted(set(h["fecha"][:4] for h in hs))
    out = []
    for y in years:
        grp = [h for h in hs if h["fecha"][:4] == y]
        out.append('    <details class="yg"%s>\n    <summary><span class="yy">%s</span><span class="yn">%d %s</span></summary>\n    <div class="ygi">\n%s\n    </div>\n    </details>' % (
            " open" if y == years[-1] else "", y, len(grp), "hecho" if len(grp) == 1 else "hechos", "\n".join(fact_html(h) for h in grp)))
    return "\n".join(out)


def render(tema):
    d = json.load(open(os.path.join(ROOT, "data", tema + ".json"), encoding="utf-8"))
    hechos = sorted(d["hechos"], key=lambda h: h["fecha"])
    aprob = [h for h in hechos if h["tipo"] == "aprobado"]
    nosal = [h for h in hechos if h["tipo"] in ("no_salio", "votado")]
    r = d["resumen"]
    rows = [("Lo que se aprobó", r.get("aprobado"))]
    if r.get("no_salio"): rows.append(("Lo que no salió" if any(h["tipo"] == "no_salio" for h in hechos) else "Lo que se votó", r["no_salio"]))
    rows += [("Lo que dicen las cifras", r.get("cifras")), ("Lo que esta página no sabe", r.get("no_sabe"))]
    sum_html = "\n".join('    <div class="row%s">\n      <span class="k">%s</span>\n      <p>%s</p>\n    </div>' % (
        " gap" if k.startswith("Lo que esta") else "", e(k), e(v)) for k, v in rows if v)

    compact = len(hechos) > 12
    tl = "\n".join('      <li><time>%s</time><span class="mk"><i class="dot%s"></i></span><div><p class="t">%s</p><p class="s">%s</p></div></li>' % (
        e(fecha(h["fecha"])), "" if h["tipo"] == "aprobado" else " no", e(h["titulo"]),
        "" if compact and h["tipo"] == "aprobado" else e(RESULT.get((h.get("votacion") or {}).get("resultado"), "") if h["tipo"] != "aprobado" else (h["frase_llana"].split(". ")[0].rstrip(".") + "."))) for h in hechos)

    aviso = ""
    if d.get("aviso_competencia"):
        aviso = '\n  <div class="aviso"><b>Aquí quien más decide es tu comunidad</b><p>%s</p></div>\n' % e(d["aviso_competencia"])

    if nosal:
        ns = by_year(nosal)
    else:
        ns = '    <p class="limit">En esta versión no consta ninguna norma de este tema rechazada o derogada. No hemos revisado el registro completo de votaciones del Congreso.</p>'

    charts, specs = [], []
    for i, ind in enumerate(d.get("indicadores", [])):
        cid = "c%d" % (i + 1)
        nota = e(ind.get("nota", ""))
        if ind.get("calculo_propio"): nota += " Algunos valores los calculamos nosotros a partir de la fuente."
        charts.append("""    <div class="chart">
      <h3>%s</h3>
      <div id="%s"></div>%s
      <p class="cap">%s</p>
      <details>
        <summary>Fuentes</summary>
        <div class="in">
          %s
        </div>
      </details>
    </div>""" % (e(ind["titulo"]), cid,
            '\n      <div class="keys"><span><i style="background:var(--accent)"></i>Dato publicado</span><span><i style="background:var(--alt)"></i>Cálculo propio</span></div>' if any(p.get("calculado") for p in ind["serie"]) else "",
            nota, fuentes_html(ind.get("fuentes"))))
        specs.append({"id": cid, "u": ind.get("unidad", ""), "dec": ind.get("decimales", 0), "t": ind["titulo"],
                      "s": [{"l": str(p["periodo"]), "v": p["valor"], "c": bool(p.get("calculado"))} for p in ind["serie"]]})

    nolist = "".join("<li>%s</li>" % e(x) for x in d.get("no_sabe", []))
    nombre = d["nombre"]
    lower = nombre[0].lower() + nombre[1:]
    has_nosal = any(h["tipo"] == "no_salio" for h in hechos)

    html = """<title>%(nombre)s, hechos del Estado</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@75..125,500..800&family=IBM+Plex+Mono:wght@400;500&family=Source+Sans+3:wght@400;600;700&display=swap">
%(css)s
%(extra)s

<main class="app">
  <header class="top">
    <a class="brand" href="index.html">Quién decide</a>
    <span class="tag">Beta</span>
  </header>

  <div class="head">
    <p class="kicker">Gobierno central y Cortes · 2018 a 2026</p>
    <h1>%(titulo)s</h1>
    <p class="lede">Ocho años con Pedro Sánchez como presidente del Gobierno, desde junio de 2018.</p>
  </div>
%(aviso)s
  <div class="sum" aria-label="Resumen">
%(sum)s
  </div>

  <section aria-labelledby="h-tl">
    <h2 id="h-tl">Qué pasó y cuándo</h2>
    <div class="legend"><span><i class="dot"></i>Aprobado</span><span><i class="dot no"></i>%(nolab)s</span></div>
    <ol class="tl%(tlc)s">
%(tl)s
    </ol>
  </section>

  <section aria-labelledby="h-a">
    <h2 id="h-a">Qué ha aprobado el Estado<span class="count">%(naprob)d</span></h2>
%(aprob)s
  </section>

  <section aria-labelledby="h-b">
    <h2 id="h-b">%(nstit)s<span class="count">%(nnosal)d</span></h2>
    <p class="lede">Solo se cuenta lo que pasó, sin juzgar a nadie. Los motivos de cada grupo se añadirán como cita literal del Diario de Sesiones.</p>
%(ns)s
  </section>

  <section aria-labelledby="h-c">
    <h2 id="h-c">Qué dicen las cifras oficiales</h2>
    <p class="lede">Se enseñan para ver la escala, no para repartir culpas.</p>
%(charts)s
    <div class="limit"><p>Qué no dicen estas cifras: qué las causó ni qué parte corresponde al Estado, a las comunidades o a los ayuntamientos.</p>%(nolist)s</div>
  </section>

  <footer class="foot">
    <p><b>Estado de la verificación.</b> %(pie)s Que Pedro Sánchez preside el Gobierno desde junio de 2018 es de dominio público.</p>
    <p>Última revisión: %(rev)s. ¿Un dato está mal? <a href="metodologia.html#correcciones">Dínoslo</a>. Cómo se ha hecho: <a href="metodologia.html">metodología</a>.</p>
  </footer>
</main>

<script>
(function(){
  var SPECS=%(specs)s;
  function num(v,dec){var s=Math.abs(v).toFixed(dec).split('.');s[0]=s[0].replace(/\\B(?=(\\d{3})+(?!\\d))/g,'.');return (v<0?'−':'')+s.join(',')}
  function fmt(v,u,dec){var n=num(v,dec);if(!u)return n;return u==='%%'?n+' %%':n+' '+u}
  SPECS.forEach(function(sp){
    var vals=sp.s.filter(function(d){return d.v!=null}).map(function(d){return d.v});
    var mn=Math.min(0,Math.min.apply(null,vals)), mx=Math.max(0,Math.max.apply(null,vals));
    var W=360,LB=58,VL=86,RH=25,BH=15,pw=W-LB-VL-(mn<0?VL*0.6:0),H=sp.s.length*RH+2;
    var span=(mx-mn)||1, x0=LB+(mn<0?VL*0.6:0)+(-mn/span)*pw;
    var s='<svg viewBox="0 0 '+W+' '+H+'" role="img" aria-label="'+sp.t+': '+sp.s.map(function(d){return d.l+' '+(d.v==null?'sin dato':fmt(d.v,sp.u,sp.dec))}).join(', ')+'">';
    sp.s.forEach(function(d,i){
      var y=i*RH+2;
      s+='<text x="0" y="'+(y+12)+'" font-size="12" font-family="IBM Plex Mono, monospace" fill="var(--ink-2)">'+d.l+'</text>';
      if(d.v==null){s+='<text x="'+(x0+4)+'" y="'+(y+12)+'" font-size="12" font-style="italic" font-family="Source Sans 3, system-ui, sans-serif" fill="var(--ink-2)">sin dato</text>';return}
      var w=Math.max(2,Math.abs(d.v)/span*pw), x=d.v<0?x0-w:x0;
      s+='<rect x="'+x+'" y="'+y+'" width="'+w+'" height="'+BH+'" fill="'+(d.c?'var(--alt)':'var(--accent)')+'" rx="2"/>';
      var tx=d.v<0?x-6:x+w+6, an=d.v<0?'end':'start';
      s+='<text x="'+tx+'" y="'+(y+12)+'" text-anchor="'+an+'" font-size="12" font-weight="600" font-family="IBM Plex Mono, monospace" fill="var(--ink)">'+fmt(d.v,sp.u,sp.dec)+'</text>';
    });
    s+='<line x1="'+x0+'" x2="'+x0+'" y1="0" y2="'+H+'" stroke="var(--ink-2)" stroke-width="1"/></svg>';
    document.getElementById(sp.id).innerHTML=s;
  });
})();
</script>
""" % {"nombre": e(nombre), "css": CSS, "extra": EXTRA_CSS, "titulo": e(d["titulo"]), "aviso": aviso, "sum": sum_html,
       "nolab": "No salió" if has_nosal else "Votado, sin ley", "tl": tl, "tlc": " compact" if compact else "",
       "naprob": len(aprob), "nnosal": len(nosal),
       "aprob": by_year(aprob) or '    <p class="nada">No consta ninguna norma aprobada en esta versión.</p>',
       "nstit": "Qué intentó y no salió" if has_nosal else "Otras votaciones", "ns": ns,
       "charts": "\n".join(charts), "nolist": ('<ul class="nolist">%s</ul>' % nolist) if nolist else "",
       "pie": e(d.get("pie_verificacion", "")), "rev": REVISION, "specs": json.dumps(specs, ensure_ascii=False)}
    open(os.path.join(ROOT, "src", tema + ".html"), "w", encoding="utf-8").write(html)
    return tema


if __name__ == "__main__":
    temas = sys.argv[1:] or [f[:-5] for f in sorted(os.listdir(os.path.join(ROOT, "data"))) if f.endswith(".json")]
    for t in temas: print("ok", render(t))
