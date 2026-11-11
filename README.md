# Quién decide

Herramienta web para ver qué nivel de gobierno (Estado, comunidad autónoma o ayuntamiento) decide sobre lo que te preocupa, y qué ha hecho ese gobierno, con hechos verificables. Pensada para las elecciones generales del 29 de noviembre de 2026.

No recomienda voto, no recoge datos de quien la usa y no puntúa a ningún partido. Metodología completa en `src/metodologia.html`.

## Estructura

```
src/            Páginas fuente (fragmentos HTML autocontenidos: estilos, datos y script en cada archivo)
  index.html        Herramienta: dónde vives → qué te preocupa → quién decide → tarjeta para compartir
  vivienda.html     Hechos del Estado en vivienda, 2018–2026 (a mano)
  inmigracion.html  Hechos del Estado en inmigración, 2018–2026 (a mano)
  <tema>.html       Otras 8 fichas, generadas desde data/ con tools/render.py
  metodologia.html  Reglas, pesos, criterio de inclusión, verificación, privacidad, correcciones
data/           Hechos e indicadores por tema en JSON (esquema en data/ESQUEMA.md)
assets/og.png   Imagen para la vista previa de los enlaces (1200×630)
tools/
  render.py     Genera src/<tema>.html desde data/<tema>.json
  build.py      Genera dist/ (sitio) o dist-artifact/ (artefactos de Claude)
  shoot.py      Capturas a 400 y 1100 px, claro y oscuro; avisa si hay scroll horizontal
  og.html       Plantilla de la imagen og.png
config.json     URL del sitio, repositorio, contacto, texto de autoría
docs/mensajes.md  Mensajes para la prueba y el lanzamiento
CLAUDE.md       Brief del proyecto: reglas, decisiones, fuentes, tareas
```

Sin dependencias en tiempo de ejecución: HTML, CSS y JS sin librerías. Las tipografías se cargan de Google Fonts.

## Construir

```bash
python3 tools/render.py         # data/*.json -> src/<tema>.html
python3 tools/build.py          # -> dist/
python3 tools/shoot.py          # opcional: requiere playwright
```

Antes de publicar, rellena en `config.json`:

- `site_url`: URL final, sin barra al final (p. ej. `https://quiendecide.es`). Hace falta para que WhatsApp muestre la imagen.
- `repo_url`: URL del repositorio público.
- `contacto`: dirección para correcciones.
- `autor`: revisa el texto de autoría.

El script avisa de lo que falta.

## Publicar en GitHub Pages

1. Crea el repositorio público y sube todo.
2. Settings → Pages → Source: GitHub Actions, o publica la carpeta `dist/` en la rama `gh-pages`.
3. Dominio propio: Settings → Pages → Custom domain, y un registro CNAME en tu proveedor de DNS.

## Publicar en Cloudflare Pages

1. Conecta el repositorio.
2. Build command: `python3 tools/build.py` · Output directory: `dist`.
3. Añade el dominio en Custom domains.

## Antes de publicar

- [ ] `config.json` completo y `python3 tools/build.py` sin avisos
- [ ] `python3 tools/shoot.py` sin scroll horizontal
- [ ] Probado por 2 personas de signo político opuesto y 5 que no siguen política
- [ ] Enlace pegado en un chat de WhatsApp: se ve título, descripción e imagen
- [ ] Registro de cambios en la metodología actualizado

## Licencia

Código bajo licencia MIT (`LICENSE`). Textos y datos recopilados bajo CC BY 4.0: puedes reutilizarlos citando la fuente. Los datos de terceros (INE, BOE, Congreso, ministerios) mantienen sus condiciones de reutilización.
