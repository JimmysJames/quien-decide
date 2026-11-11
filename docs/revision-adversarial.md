# Revisión adversarial de Quién decide

Pega todo lo que hay debajo de la línea en un chat nuevo y adjunta `quien-decide.zip` (o, como mínimo, la carpeta `dist/`, la carpeta `data/` y `CLAUDE.md`).

---

Vas a hacer una revisión adversarial de "Quién decide", una web para las elecciones generales de España del 29 de noviembre de 2026. Te adjunto el proyecto completo. Lee primero `CLAUDE.md`: ahí están las reglas que la web dice cumplir. Las páginas publicadas están en `dist/`, y los datos de ocho de las diez fichas en `data/*.json`.

La web dice ser neutral: solo hechos con fuente, sin valoraciones, el mismo trato para todos los partidos. Tu trabajo es intentar demostrar que no lo es, o que se equivoca. No me interesa una valoración general ni elogios: solo problemas concretos, con su ubicación y una corrección propuesta. Si no encuentras nada en un apartado, dilo en una línea y sigue.

Revisa desde cinco papeles, uno detrás de otro:

1. **Votante de derechas desconfiado.** Busca dónde la web favorece al Gobierno o a la izquierda: hechos que la favorecen y faltan los que la perjudican, palabras que suavizan, orden de presentación, qué votaciones perdidas se muestran y cuáles no, indicadores elegidos que salen bien parados.
2. **Votante de izquierdas desconfiado.** Lo mismo en sentido contrario: dónde favorece al PP, a Vox o a Junts, o deja peor al Gobierno de lo que los hechos justifican.
3. **Verificador de datos.** Elige al menos 25 cifras al azar repartidas entre todas las fichas (recuentos de votos, fechas, números de norma, valores de indicadores) y compruébalas en la fuente que cita cada una, buscando en la web. Para cada una: correcta, incorrecta (con el valor bueno y la fuente) o no comprobable. Comprueba también que las etiquetas de verificación (Oficial, Prensa · 2 fuentes, etc.) son honestas.
4. **Jurista electoral.** Revisa si algo puede chocar con la Ley Orgánica del Régimen Electoral General en campaña (del 13 al 27 de noviembre), en la prohibición de publicar sondeos desde el 24 o en la jornada de reflexión del 28. Revisa también si los pesos de competencias (tabla en la metodología) tienen algún error jurídico.
5. **Persona indecisa que no sigue la política.** Recorre la herramienta (`dist/index.html`) como lo haría alguien con prisa en el móvil. Dónde no entiendes algo, dónde te aburres, qué te haría desconfiar, si reenviarías la tarjeta del final.

Presta especial atención a:
- La ley de amnistía en la ficha de corrupción y la ley del aborto en la de sanidad: ¿entrar es correcto según el criterio de inclusión? ¿La descripción es neutral?
- Asimetrías: ¿se nombran los grupos que votaron en contra con la misma frecuencia para todos? ¿Hay normas que aparecen en una ficha y faltan en otra donde también encajan?
- El encabezado "Ocho años con Pedro Sánchez como presidente del Gobierno": ¿encuadra la lectura?
- Frases del resumen de cada ficha: ¿algún verbo o selección implica causa o juicio?

Formato de la respuesta:
1. Una tabla con todos los hallazgos: gravedad (alta, media, baja), papel que lo detecta, página y lugar exacto, problema, corrección propuesta.
2. La tabla del verificador con las 25 cifras o más.
3. Los tres cambios que harías antes de enseñárselo a nadie más.

No reescribas las páginas. Solo señala.
