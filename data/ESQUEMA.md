# Esquema de data/<tema>.json

{
  "tema": "empleo",                       // id del tema
  "nombre": "Empleo y salarios",          // como aparece en la demo
  "titulo": "Empleo y salarios: qué ha hecho el Estado",
  "aviso_competencia": "",                // solo si quien más decide NO es el Estado: frase corta
  "resumen": {
    "aprobado": "Frase llana con 3-5 medidas y su año.",
    "no_salio": "Frase llana con votaciones perdidas, o '' si no hay ninguna verificada.",
    "cifras": "Frase llana con 2-3 cifras de los indicadores, sin causas.",
    "no_sabe": "Qué no consta."
  },
  "hechos": [
    {
      "id": "emp-2021-reforma-laboral",
      "tipo": "aprobado",                 // aprobado | no_salio | votado (admitido a trámite, sin ley)
      "fecha": "2021-12-28",              // ISO
      "titulo": "Real Decreto-ley 32/2021, reforma laboral",
      "frase_llana": "Una o dos frases: qué cambia para la gente. Sin valorar.",
      "detalle": "Datos técnicos: número de norma, BOE, entrada en vigor, contenido.",
      "votacion": {                       // null si no hubo o no consta
        "fecha": "2022-02-03",
        "a_favor": 175, "en_contra": 174, "abstenciones": 0,   // null si no consta el recuento
        "grupos_en_contra": ["PP", "Vox"],                       // [] si no consta; orden alfabético. Se guarda pero NO se muestra en la ficha (solo constaba cuando la prensa lo decía)
        "resultado": "convalidado",       // convalidado | derogado | aprobado (ley aprobada) | tomado_en_consideracion | rechazado | devuelto (enmiendas de totalidad aprobadas: a_favor = votos a favor de las enmiendas) | enmienda_rechazada (enmiendas de totalidad rechazadas: a_favor = votos a favor de las enmiendas)
        "fuente_recuento": "oficial",      // oficial (Diario de Sesiones, acta o registro del Congreso) | dos_fuentes | una_fuente | null si no hay recuento. Decide la etiqueta «recuento oficial / según dos medios / según un medio»
        "camara": "congreso"               // opcional: congreso (Pleno, por defecto) | senado | comision | diputacion_permanente. Se muestra si no es el Pleno del Congreso
      },
      "fuentes": [
        {"nombre": "BOE-A-2021-21788", "url": "https://...", "tipo": "oficial", "fecha": "2021-12-30"}
      ],                                   // tipo: oficial | prensa | terceros
      "verificacion": "oficial",           // oficial | dos_fuentes | terceros | una_fuente
      "no_sabemos": ""                     // opcional
    }
  ],
  "indicadores": [
    {
      "id": "paro",
      "titulo": "Tasa de paro (EPA, 2.º trimestre)",
      "unidad": "%",                        // % | € | personas | días | millones | MtCO2eq | puntos
      "decimales": 1,
      "nota": "Qué mide exactamente. Cambios de método si los hay.",
      "calculo_propio": false,
      "serie": [{"periodo": "2018", "valor": 15.3}],   // null si no hay dato
      "fuentes": [{"nombre": "INE, EPA 2T 2018", "url": "https://...", "tipo": "oficial", "fecha": "2018-07-26"}]
    }
  ],
  "no_sabe": ["Lista corta de huecos."],
  "pie_verificacion": "Qué está con fuente oficial, qué con dos fuentes de prensa y qué con una."
}
