# Instrucciones comunes para ampliar una ficha

Contexto: "Quién decide" es una herramienta cívica NEUTRAL para las generales de España del 29 de noviembre de 2026. Hoy es 11 de noviembre de 2026. Las Cortes se disolvieron el 6 de octubre de 2026. Periodo: 1 de junio de 2018 a 6 de octubre de 2026. Ámbito: el ESTADO (Gobierno central y Cortes Generales), no comunidades.

Partes de un fichero ya existente, data/<tema>.json (esquema en data/ESQUEMA.md). NO borres hechos existentes salvo que sean erróneos (si corriges algo, explícalo en tu respuesta final). AÑADE lo que falte.

## Criterio de inclusión (ya no hay límite de número)
Entran TODOS estos, si su asunto principal es el tema:
1. Leyes y leyes orgánicas publicadas en el BOE en el periodo.
2. Reales decretos-leyes, convalidados o derogados (busca activamente los DEROGADOS: son clave para la neutralidad).
3. Los reales decretos que fijan cada año el parámetro clave del tema, uno por año (se indican en tu tarea, si aplica).
4. Proyectos y proposiciones de ley votados en el Pleno del Congreso (toma en consideración, enmiendas a la totalidad) aunque no salieran o decayeran.
5. Planes con nombre propio aprobados por el Consejo de Ministros.
Si una norma es de varios temas, inclúyela si este es uno de sus temas principales. Las prórrogas sucesivas de una misma medida pueden ir agrupadas en un único hecho, con todas las normas citadas en el detalle.

## Votaciones
- Prioriza el registro oficial del Congreso: actas del Pleno (https://www.congreso.es/docu/tramit/LegXV/AT/ATCD_15_PL_AAAAMMDD.pdf para la XV legislatura; ATCD_14_PL para la XIV), Diario de Sesiones (DSCD) y ficheros de votaciones (https://www.congreso.es/webpublica/opendata/votaciones/...). WebFetch puede leer PDFs del Congreso.
- Si el recuento oficial difiere de la prensa, manda el oficial.
- "grupos_en_contra" solo si una fuente lo dice, en orden alfabético. Para "devuelto" y "enmienda_rechazada", a_favor = votos a favor de las enmiendas y grupos_en_contra = [] (explica en "detalle" quién presentó las enmiendas).
- Para leyes aprobadas usa resultado "aprobado" con el recuento de la votación final en el Congreso si consta.

## Reglas
- Solo datos que hayas leído en una página abierta (WebFetch) o literalmente en un resultado de búsqueda. Nada de memoria. Si falta, null y anótalo en "no_sabe" o "no_sabemos".
- Fuente oficial primero (boe.es, congreso.es, lamoncloa.gob.es, ministerios, ine.es). Etiqueta "verificacion" honestamente.
- Neutral: frases cortas, sin valoraciones ("histórico", "récord", "polémico", "mucho"), sin atribuir causas, sin adjetivos sobre partidos.
- "frase_llana": qué cambia para la gente, 1-2 frases. "titulo": número y nombre corto de la norma.
- Actualiza "resumen" (4 frases llanas) y "pie_verificacion" para que reflejen la ficha ampliada. El resumen nombra lo principal, no todo.
- Valida el JSON con python3 al terminar.

Respuesta final (breve): número de hechos antes y después, lista de hechos añadidos (fecha, título, verificación), correcciones hechas, y lo que no pudiste confirmar.
