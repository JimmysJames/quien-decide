# Quién decide — brief del proyecto

Última actualización: 11 de noviembre de 2026. 

## Qué es

Herramienta web para las elecciones generales de España del 29 de noviembre de 2026 (convocadas en el BOE del 6 de octubre; campaña del 13 al 27 de noviembre; prohibido publicar sondeos desde el 24; jornada de reflexión el 28). Ayuda a una persona a ver **qué nivel de gobierno decide de verdad sobre lo que le preocupa** y **qué ha hecho ese gobierno**, con hechos verificables y sin pedir el voto para nadie.

Público objetivo: indecisos y gente que no sigue política. No está pensada para convencidos de ningún lado. Lo que circula es la pantalla de resultado, reenviada por WhatsApp; la web por sí sola no llega a nadie.

Tesis de fondo: mucha gente vota en las generales pensando en vivienda, sanidad o educación, que son en gran parte autonómicas o municipales. Hacer visible ese desajuste es el valor principal y, de paso, baja la temperatura sin decirlo.

## Reglas que no se negocian

1. **Solo hechos con fuente y fecha.** Cada dato enlaza a su fuente. Si no hay fuente, no se publica.
2. **Sin notas, sin ranking, sin culpas.** Las cifras se muestran a escala y sin atribuir causa. "El precio subió X" nunca va seguido de "por culpa de".
3. **Mismo formato para todos.** Mismos indicadores, mismo espacio, mismo orden (alfabético o cronológico) para cualquier partido, gobierno o nivel. Los indicadores se fijan **antes** de mirar los datos.
4. **Separar tres cosas:** lo aprobado y ejecutado, lo propuesto que no salió, y cómo evolucionó el indicador oficial.
5. **Lo que no se sabe, se dice.** Cada ficha lleva un bloque "Lo que esta página no sabe" y un pie con el estado de la verificación (qué está cotejado con dos fuentes y qué no).
6. **Nada de "qué partido encaja contigo"**, ni puntuar cumplimiento de promesas, ni resumir motivos de los grupos con palabras propias. Los motivos se dan como cita textual del Diario de Sesiones, con el mismo espacio para todos.
7. **Privacidad:** no se guarda ni se envía nada por usuario. No se pregunta por ingresos. La tarjeta para compartir no lleva municipio. En el lanzamiento no se mide nada; si se añade medición, solo tres contadores agregados sin cookies ni identificadores (ver "Medición y privacidad").
10. **Un hecho solo entra si cumple el criterio de inclusión** (ver más abajo). Lo que no cabe en el criterio no se cuela como hecho, por importante que parezca.
8. **Nada de bots ni cuentas coordinadas** para difundir. Difusión orgánica y por medios/verificadores.
9. **Antes de publicar nada:** pasarlo a dos personas de signo político opuesto y preguntarles si les parece una trampa. Si una dice que sí, revisar.

Decisión explícita: se descartó una versión con postura editorial. Motivos: (a) contradice el objetivo de llegar a indecisos, (b) una tesis no sale de los datos sin elegir qué mirar, y (c) si fuera cierta, el método neutral la mostraría solo. Si algún día se quiere una lectura con postura, va en una sección aparte, firmada y marcada como opinión, nunca mezclada con los hechos.

## Estructura del producto

**Demo (tres pantallas + tarjeta):**
1. Dónde vives: comunidad y municipio.
2. Qué te preocupa: hasta 3 de los 10 problemas, por orden. La lista de problemas sale de las categorías del CIS.
3. Quién tiene la llave: para cada preocupación, peso de Estado / comunidad / ayuntamiento (0–3), con referencia legal; quién gobierna en cada nivel; una pregunta neutra que sirve para cualquier partido; enlace a la ficha de hechos si existe. Arriba, el resumen compartible: "Para N de tus M preocupaciones, quien más decide no se elige en las generales", con la fecha de las próximas autonómicas/municipales (23 de mayo de 2027 donde toca).
4. Tarjeta para compartir: fondo oscuro, titular grande, las 3 preocupaciones con quién decide, leyenda. Pensada para captura de pantalla.

**Fichas "qué ha hecho el Estado"** (hechas: vivienda, inmigración; periodo 2018–2026):
- Resumen en lenguaje llano con cuatro filas: lo que se aprobó, lo que no salió (o lo que se votó), lo que dicen las cifras, lo que esta página no sabe.
- Línea de tiempo (aprobado / no salió).
- "Qué ha aprobado": una tarjeta por medida con fecha, etiqueta de fuente (Oficial / Prensa · 2 fuentes / Resumen de terceros / una sola fuente), una frase llana, un esquema de quién hace qué cuando aplica, y detalle + fuentes plegados.
- "Qué intentó y no salió" o "Cómo votó el Congreso": barra de votos a escala, voto por grupo en tabla alfabética.
- "Qué dicen las cifras oficiales": series de 8 años en barras horizontales (se leen bien a 400 px), acumulados calculados por nosotros marcados como tal, fuentes plegadas por año.
- Pie: estado de la verificación y fecha de consulta.

**Pendiente:** fichas autonómicas con el mismo indicador en las 17 comunidades. Ahí es donde existe comparación entre partidos (Madrid PP, Castilla-La Mancha PSOE, Cataluña PSC…); a nivel estatal 2018–2026 es un solo presidente y no hay comparación posible. Para comparar partidos en el Estado habría que llegar a 2011.

## Pesos de competencias (orientativos, revisar con un jurista)

0 = no interviene, 1 = margen pequeño, 2 = tiene peso, 3 = decide la mayor parte. Formato Estado / Comunidad / Ayuntamiento.

| Problema | E | C | A | Base |
|---|---|---|---|---|
| Vivienda | 2 | 3 | 2 | CE 148.1.3; Ley 12/2023; Ley 7/1985 art. 25 (suelo y licencias) |
| Sanidad | 2 | 3 | 1 | Transferida 2002; Ley 16/2003. Ceuta y Melilla: INGESA (Estado) |
| Empleo y salarios | 3 | 2 | 1 | Estatuto de los Trabajadores, SMI; SEPE autonómicos |
| Economía y coste de vida | 3 | 1 | 1 | PGE; impuestos cedidos; IBI. Forales: hacienda propia |
| Inmigración | 3 | 2 | 1 | CE 149.1.2 (extranjería); integración y menores en comunidades |
| Pensiones | 3 | 0 | 0 | CE 149.1.17 |
| Educación | 2 | 3 | 1 | LOMLOE; transferida; 0–3 y mantenimiento de colegios municipal. Ceuta y Melilla: Ministerio |
| Corrupción | 2 | 2 | 2 | Código Penal; Ley 9/2017 de contratos |
| Seguridad ciudadana | 3 | 1 | 2 | CE 149.1.29; policía propia solo en Cataluña, País Vasco, Navarra y Canarias (Policía Canaria, Ley 2/2008); Policía Local |
| Clima y energía | 2 | 2 | 2 | Ley 7/2021; ordenación del territorio; residuos y movilidad municipal |

Partido que lidera cada gobierno autonómico (2026, verificar): PP en Andalucía, Aragón, Baleares, Cantabria, Castilla y León, C. Valenciana, Extremadura, Galicia, Madrid, Murcia, La Rioja, Ceuta y Melilla; PSOE en Asturias, Castilla-La Mancha y Navarra; PSC en Cataluña; PNV en País Vasco; Coalición Canaria en Canarias. Estado: PSOE. Gobiernos municipales: no incluidos (dato difícil de mantener; sale de resultados y pactos).

Votan en mayo de 2027: Asturias, Baleares, Canarias, Cantabria, Castilla-La Mancha, C. Valenciana, Madrid, Murcia, Navarra, La Rioja, Ceuta, Melilla y todos los ayuntamientos.

## Fuentes oficiales por tema

**Transversales**
- CIS, barómetros mensuales (lista de problemas): https://www.cis.es/
- Congreso, votaciones (datos abiertos) y Diario de Sesiones: https://www.congreso.es/
- BOE, API y buscador: https://www.boe.es/
- Constitución: https://www.boe.es/buscar/act.php?id=BOE-A-1978-31229
- INE, API JSON (tempus): https://www.ine.es/dyngs/DAB/index.htm?cid=1099

**Vivienda**
- INE, Índice de Precios de Vivienda, notas trimestrales: https://www.ine.es/dyngs/Prensa/IPV2T26.htm (patrón IPV{T}T{YY}; anteriores a 2024 en /daco/daco42/ipv/ipv0{T}{YY}.pdf)
- INE, Índice de Precios de Vivienda en Alquiler, anual: https://ine.es/dyngs/Prensa/IPVA2024.htm (último dato: 2024, publicado mayo 2026)
- Ministerio de Vivienda / La Moncloa, notas de prensa (CASA 47, Plan Estatal)

**Inmigración**
- Interior, balances de inmigración irregular: https://www.interior.gob.es/opencms/es/prensa/balances-e-informes/
- INE, Estadística Continua de Población: https://www.ine.es/dyngs/Prensa/ECP4T25.htm (patrón ECP{T}T{YY})
- Seguridad Social, afiliados extranjeros: https://revista.seg-social.es/
- Ministerio de Inclusión, balance de la regularización: https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/inclusion/

**Sanidad (pendiente)**
- Ministerio de Sanidad, SISLE (listas de espera por comunidad): https://www.sanidad.gob.es/
- Estadística de Gasto Sanitario Público (gasto por habitante y comunidad)

## Datos recogidos y cosas a vigilar

- Precio de compra (IPV, 2.º trimestre, tasa anual): 2018 6,8 · 2019 5,3 · 2020 2,1 · 2021 3,3 · 2022 8,0 · 2023 3,6 · 2024 7,8 · 2025 12,7 · 2026 12,2. Acumulado 2018→2026: +69,4 % (cálculo propio); últimos 4 años: +41,2 %.
- Alquiler (IPVA, tasa anual): 2018 2,6 · 2019 3,5 · 2020 0,9 · 2021 1,6 · 2022 2,7 · 2023 2,6 · 2024 3,5. En 2024, contratos nuevos +8,8 %, existentes +2,8 %.
- Llegadas irregulares (Interior): 2018 64.298 · 2019 32.513 · 2020 41.861 · 2021 41.945 · 2022 31.219 · 2023 56.852 · 2024 64.019 · 2025 36.775. Primer semestre 2026: 12.138 (−32,5 %). **Interior revisa cifras después de publicarlas**: 2022 aparece también como 30.048 y 2024 como 63.970. Documentar siempre cuál se usa y por qué.
- Población con nacionalidad extranjera a 1 de enero (millones): 2018 4,73 · 2019 5,03 · 2020 5,42 · 2021 sin dato · 2022 5,51 · 2023 6,09 · 2024 6,49 · 2025 6,85 · 2026 7,24. **Cambio de método** del INE (Padrón → Censo → Estadística Continua): 2020→2022 no es comparable del todo.
- Afiliados extranjeros (media de diciembre, millones): 2018 1,99 · 2019 2,12 · 2020 2,08 · 2021 2,27* · 2022 2,46 · 2023 2,67 · 2024 2,88* · 2025 3,09. (*calculados restando la variación publicada).
- Votaciones: decretos de vivienda 2 oct 2026, 172–178 y 166–184 (dos fuentes); reparto de menores 10 abr 2025, 179–170–1; decreto vivienda 21/2018 derogado 22 ene 2019 (sin recuento en las fuentes); ILP regularización admitida 9 abr 2024, todos salvo Vox (sin recuento).
- Regularización extraordinaria 2026: 1.174.978 solicitudes (La Moncloa, solo titular visto). Cifras de tramitadas/concedidas difieren entre fuentes y fechas (609.737 el 10 jul; 822.000 "con permiso preliminar" el 23 jul). No mezclar.

Cotejo del 11 nov 2026 con fuente oficial: Plan Estatal (La Moncloa 21 y 28 abr: 7.000 M, el triple, 60 % Estado / 40 % CCAA, al menos 40 % a vivienda pública; el reparto 30/30 restante solo lo da la prensa), regularización (La Moncloa 2 jul: 1.174.978 solicitudes, cierre 30 jun), llegadas 2024 y 2025 (informe quincenal de Interior, copia en ARC Legal), precios y población (notas del INE). Pendiente: recuentos de votaciones en el registro del Congreso; uno de los decretos de vivienda tumbados el 2 oct es el RDL 26/2026, de 29 de septiembre.

Gobiernos autonómicos revisados el 11 nov 2026: Andalucía (Moreno, reelegido en julio de 2026 con Vox en el Gobierno), Aragón (Azcón, investido en abril), Castilla y León (Mañueco, junio, acuerdo de gobierno con Vox) y Extremadura (Guardiola, abril, pacto con Vox) siguen liderados por el PP.

## Huecos conocidos

- "Ejecutado" casi nunca consta: viviendas entregadas (CASA 47), menores trasladados, ayudas del Bono Joven concedidas. Decir que no se sabe en vez de rellenar.
- Motivos de cada grupo en las votaciones: no incluidos hasta que sean cita textual del Diario de Sesiones.
- Gobierno municipal del usuario: no incluido.
- No se ha revisado el registro completo de votaciones del Congreso; puede haber medidas rechazadas que no constan.

## Tareas pendientes, por prioridad

1. Probar la demo con cinco personas que no sigan política. Dónde se aburren, dónde desconfían, si reenviarían la tarjeta. No gasta modelo. Hacerlo **antes** de construir más.
2. Ficha autonómica de sanidad: fijar 3–4 indicadores (lista de espera media, gasto por habitante, plantilla de primaria), recogerlos para las 17 comunidades, mostrar la del usuario frente a las demás.
3. Pipeline de fuentes primarias: Congreso (votaciones), INE (API), BOE (API), Interior (PDF). Reutilizar la arquitectura de ingesta del observatorio (snapshots idempotentes, entity resolution). Cada dato enlaza a la fuente oficial y se actualiza solo.
4. Motivos de cada grupo con cita textual del Diario de Sesiones, mismo espacio para todos.
5. ~~Decidir qué hacer con el tramo de renta.~~ Quitado el 11 nov.
6. Cotejar con fuente primaria lo que sigue marcado como prensa o terceros (recuentos de votaciones, reglamentos, Bono Joven, tope del 2 %).
7. Revisar los pesos de competencias con un jurista. (Metodología publicada el 11 nov.)
8. Tarjeta como imagen real (ahora es captura de pantalla; una página no puede generar la descarga).
9. Pasar vivienda e inmigración por el criterio de inclusión: listar todas las normas y votaciones del periodo (BOE, Congreso) y ver cuáles faltan.
10. Esquema de datos: sacar los hechos de los HTML a registros y generar las fichas desde ahí.
11. Hosting y dominio (pendiente). Open Graph hecho (`assets/og.png`). Contadores agregados: no para el lanzamiento.
12. Canal de correcciones: falta la dirección de contacto en `config.json`. Registro de cambios: en la metodología.

Trabajo mecánico (recogida de 17 comunidades, ingesta, extracción del Diario de Sesiones): modelo barato. Trabajo de criterio (elegir indicadores, revisar resultados, decisiones de producto): modelo caro.

## Difusión

- Lo que se comparte es la tarjeta y el enlace con vista previa, por WhatsApp y Telegram.
- TikTok/Reels: vídeos de 15–30 s con una sola pregunta ("¿Quién decide el precio de tu alquiler?"), mejor desde cuentas de explicación que políticas.
- X sirve para periodistas y verificadores (Maldita, Newtral, Civio), no para público general. Que una de esas entidades revise la metodología vale más que cualquier campaña.
- Publicidad política de pago en Meta y Google: según lo que sabíamos, no se acepta en la UE desde octubre de 2025. Verificar.
- Medir por porcentaje de gente que termina y comparte, no por visitas.
- Riesgo legal: la LOREG limita la propaganda en campaña y jornada de reflexión. Una herramienta neutral que no pide el voto suele quedar fuera; consultar antes de lanzar cualquier versión con postura.

## Criterio de inclusión de hechos

Para que la selección no sea editorial, para cada tema y ámbito entran **todos** estos, sin excepción:

- Toda norma con rango de ley, real decreto-ley o real decreto publicada en el BOE (o en el boletín autonómico) cuya materia sea el tema, dentro del periodo.
- Toda votación en Pleno sobre esa materia (convalidaciones, tomas en consideración, enmiendas a la totalidad), salga o no.
- Los planes y partidas presupuestarias con nombre propio del tema (Plan Estatal de Vivienda, etc.).
- Los indicadores fijados de antemano para el tema, de fuente oficial, serie completa del periodo.

No entran: declaraciones, anuncios sin norma ni licitación detrás, propuestas de la oposición sin votación. Lo que no cabe y aun así parece relevante va a "Lo que esta página no sabe".

Atribución: cada hecho se atribuye al gobierno que estaba en el cargo en la fecha del hecho, y la línea de tiempo marca los cambios de legislatura y de gobierno. Imprescindible para las fichas autonómicas, donde los gobiernos cambian a mitad de periodo.

Las fichas de vivienda e inmigración se hicieron **antes** de fijar este criterio, con lo que apareció en las búsquedas. Hay que pasarlas por el criterio y ver qué normas y votaciones faltan.

## Esquema de datos

Hoy todo está inline en el HTML. Antes de la tercera ficha, separar datos de presentación. Un registro por hecho:

```yaml
id: viv-2023-ley-12              # tema-año-slug
tema: vivienda                   # uno de los 10
ambito: estado                   # estado | ccaa:MD | municipio:28065
tipo: aprobado                   # aprobado | no_salio | indicador
fecha: 2023-05-25                # fecha del hecho, no de la consulta
titulo: Ley 12/2023 por el derecho a la vivienda
frase_llana: El Estado crea la herramienta, pero la aplica cada comunidad.
detalle: ...
gobierno_en_el_cargo: PSOE       # quien gobernaba el ámbito en `fecha`
votacion:                        # solo si hubo votación
  a_favor: 172
  en_contra: 178
  abstenciones: 0
  por_grupo: {PP: en_contra, PSOE: a_favor, ...}
serie:                           # solo tipo indicador
  - {periodo: 2018, valor: 6.8, fuente: 0}
calculo_propio: false            # true si el valor lo derivamos nosotros
fuentes:
  - {url: ..., tipo: oficial, fecha_consulta: 2026-10-08, cita: "..."}
verificacion: dos_fuentes        # una_fuente | dos_fuentes | primaria
no_sabemos: Cuántas zonas tensionadas hay declaradas en total.
```

La ficha HTML se genera a partir de estos registros. Un hecho sin `fuentes` no se publica. Cuando una cifra cambia (Interior revisa sus balances), se guarda como nueva versión con fecha; no se sobrescribe.

## Medición y privacidad

"No se guarda nada" y "medir qué porcentaje comparte" chocan. Resolución: tres contadores agregados (empieza, termina, abre la tarjeta o copia), sin cookies, sin identificadores, sin IP, y se dice en la página. Plausible autoalojado o un contador propio.

**Nunca se publican agregados de qué preocupa a la gente ni de sus respuestas.** Parecería una encuesta electoral, y la LOREG prohíbe publicarlas en los cinco días anteriores a la votación. Los contadores sirven para saber si la herramienta funciona, no para contar nada hacia fuera.

## Publicación

- Hosting estático (GitHub Pages o Cloudflare Pages), dominio propio, HTTPS. Comprobar antes que "Quién decide" no lo usa ya otro proyecto como marca o dominio.
- Metadatos Open Graph (título, descripción, imagen) para que el enlace tenga vista previa en WhatsApp. Sin servidor no se puede personalizar la vista previa por resultado; imagen genérica más la captura de la tarjeta.
- Repositorio público con metodología y datos. La credibilidad depende de que cualquiera pueda rehacer las fichas.
- Canal de correcciones visible ("¿Un dato está mal? Escríbenos") y registro público de cambios con fecha. Derecho de réplica, con el mismo espacio, a cualquier partido o gobierno aludido.
- Lenguas cooficiales (catalán, euskera, gallego): en el backlog; importan para el alcance en esas comunidades.
- La fecha de las elecciones es configuración, no contenido. Si no hay generales el 29N, la herramienta sirve igual para las autonómicas y municipales de mayo de 2027 y para las generales de 2027.

## Para sesiones de Claude

- Leer este archivo entero antes de tocar nada. Las reglas no se cambian sin anotarlo en el registro de decisiones.
- No inventar cifras ni fuentes. Si no se encuentra la fuente, se deja "sin dato" y se anota en tareas.
- Toda cifra nueva lleva URL de la fuente y fecha de consulta. Marcar `calculo_propio` cuando lo sea.
- Antes de publicar: `node --check`, balance de etiquetas, capturas a 400 y 1100 px en claro y oscuro, sin scroll horizontal.
- Al terminar: actualizar "Estado actual", "Tareas pendientes" y el registro de decisiones.

## Registro de decisiones

- 2026-10-07 · Herramienta neutral, no de tesis. Motivo: llegar a indecisos; la tesis no sale de los datos sin elegir qué mirar; si es cierta, el método neutral la muestra solo.
- 2026-10-07 · No resumir programas con palabras propias; como mucho, citas literales con página y "sin mención". Motivo: elegir el fragmento ya es editorial.
- 2026-10-07 · Las fichas separan aprobado / no salió / indicador y no atribuyen causa. Motivo: hechos no son resultados; el BCE y el ciclo pesan más que una ley.
- 2026-10-08 · Periodo de las fichas: 8 años (2018–2026). Motivo: 4 era poco; 8 cubre un presidente en el Estado. Para comparar partidos en el Estado habría que ir a 2011.
- 2026-10-08 · Tarjeta como captura de pantalla, no como descarga. Motivo: la página no puede generar archivos en el visor de artefactos.
- 2026-10-08 · Sin bots ni cuentas coordinadas. Motivo: va contra las normas de las plataformas y destruye el único activo, la confianza.
- 2026-10-08 · Contadores agregados sí, datos por usuario no. Motivo: hay que saber si funciona sin romper la promesa de privacidad.
- 2026-11-11 · Lanzamiento con lo que hay (demo, vivienda, inmigración, metodología); sin fichas nuevas. Motivo: 18 días hasta el 29N.
- 2026-11-11 · Se quita la pregunta de ingresos. Motivo: aportaba una frase y generaba desconfianza.
- 2026-11-11 · Sin contadores en el lanzamiento. Motivo: cumplir la promesa de no recoger nada sin montar infraestructura con prisas.
- 2026-11-11 · Fichas de los 10 temas, con límite de 5 a 9 hechos por tema e indicadores fijados antes de buscar los datos. Sanidad y educación con aviso de competencia autonómica. Corrupción sin casos judiciales. Motivo: se prefirió cubrir los 10 temas antes del lanzamiento; riesgo asumido de más errores, mitigado con etiquetas de verificación por hecho.
- 2026-11-11 · Sin límite de hechos en las 8 fichas generadas (de 64 a 191). Reales decretos solo los que fijan el dato anual clave (SMI, revalorización, becas). Normas de varios temas aparecen en todas sus fichas, con el mismo recuento (acta oficial). Fichas largas: años plegados y línea de tiempo compacta. Motivo: aplicar el criterio de inclusión de verdad.
- 2026-11-11 · Seguridad: la tasa de criminalidad completa con cálculo propio (infracciones / población INE) en 2018-2020, 2023 y 2025, en otro color. Motivo: el indicador estaba fijado y faltaba la mitad.
- 2026-11-11 · Corrupción incluye la LO 1/2024 de amnistía porque su texto en el BOE comprende la malversación; texto estrictamente literal. PENDIENTE DE CONFIRMAR.
- 2026-11-11 · Sanidad incluye la LO 1/2023 (salud sexual y reproductiva y aborto) por ser materia sanitaria.
- 2026-11-11 · No promocionar el 28 de noviembre ni publicar agregados desde el 24. Motivo: jornada de reflexión y prohibición de sondeos (LOREG).
- 2026-11-11 · Revisión de neutralidad (A, B, C). A: las fichas dejan de mostrar los grupos «en contra» (solo constaban cuando la prensa lo decía; el campo se conserva en los datos); decretos ómnibus derogados con título y primera frase iguales en todas las fichas; «tumbar» sustituido; mismo recuento y mismo texto de fuente para una misma votación en varias fichas. B: encabezado con los tres gobiernos y separadores de gobierno en la línea de tiempo; la tarjeta usa la formulación del resumen; Ceuta y Melilla con sanidad y educación 3 Estado / 1 ciudad; Policía Canaria es cuerpo propio. C: cada votación lleva `fuente_recuento` (oficial / dos_fuentes / una_fuente / null) y `camara` si no es el Pleno del Congreso; siete recuentos cotejados en el Diario de Sesiones; los Presupuestos no presentados pasan a «Lo que esta página no sabe» (no es norma ni votación); la frase de la LO 14/2022 cita el preámbulo.

## Estado actual (11 nov 2026)

Repositorio: `src/` (fuentes), `tools/build.py` (genera `dist/` para web y `dist-artifact/` para artefactos), `config.json` (falta `site_url`, `repo_url`, `contacto`), `docs/mensajes.md` (prueba y lanzamiento).

Artefactos de Claude (privados hasta que se compartan desde su menú):
- Herramienta: https://claude.ai/artifact/5Ctp8BZ1buXrddS8fiCg5g
- Vivienda: https://claude.ai/artifact/EH4FcAvBYnkumkXkDRof6j
- Inmigración: https://claude.ai/artifact/2zdR69cQ8bnti4YFV8MEno
- Metodología: https://claude.ai/artifact/CeV2pZKeeiB1QByzrdRrdM
- Sanidad: https://claude.ai/artifact/HGLD5HE8Pn2Mxyo8MV7FFT
- Empleo: https://claude.ai/artifact/KrtHFEwknHfpbhpmjwMfZg
- Economía: https://claude.ai/artifact/XW32G3kisSDeXi6h1BTM7t
- Pensiones: https://claude.ai/artifact/W4cH2C28Nshz1AfBZR5Zto
- Educación: https://claude.ai/artifact/366yRzeqwUQJWbXaiV3Djj
- Corrupción: https://claude.ai/artifact/XVZDbmiUSjqi9kT5UJiQP6
- Seguridad: https://claude.ai/artifact/J6kNzaYxpJH2JQMXfrp46B
- Clima: https://claude.ai/artifact/WizhkTY8R58q9Lj2BgkdQv

Copia de los datos antes de la ampliación en `data/v1/`. Instrucciones para ampliar en `data/AMPLIACION.md`.

Las 8 fichas nuevas se generan desde `data/<tema>.json` con `python3 tools/render.py` (esquema en `data/ESQUEMA.md`). Vivienda e inmigración siguen escritas a mano en `src/`; pasarlas a datos es la tarea 10.

## Convenciones técnicas

- Una página = un HTML autocontenido. Sin backend, sin login, sin almacenamiento. Los datos van inline en el JS.
- Tema claro y oscuro con tokens en `:root`, redefinidos en `@media (prefers-color-scheme: dark)` guardado con `:root:not([data-theme="light"])` y en `:root[data-theme="dark"]`. Fondo explícito en `body`.
- Tipografías: Archivo (titulares), Source Sans 3 (texto), IBM Plex Mono (cifras y etiquetas). Acento verde azulado; neutros con ligero sesgo frío.
- Gráficos en SVG inline generados por JS, a escala, con colores de los tokens. Series largas en barras horizontales (se leen a 400 px). Nada de librerías de gráficos.
- Comprobar antes de publicar: `node --check` del script, balance de etiquetas, `python3 tools/shoot.py` (400 y 1100 px, claro y oscuro, sin scroll horizontal).
- Enlaces entre páginas siempre relativos en `src/`; `build.py artifact` los cambia por las URL de los artefactos.
- Detalle técnico y fuentes siempre en `<details>` plegados; lo primero que se ve es la frase llana.
- Copia: frases cortas, sin "no es X sino Y", sin colon-y-revelación, sin valoraciones ("mucho", "poco", "récord") salvo que sean cita.
