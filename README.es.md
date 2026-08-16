<div align="center">

# Leonardo Mendoza

**Backend & Data Engineer** · Cartagena, Colombia

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/leonardomendoza-dev)
[![Email](https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:leonardomendoza2003@gmail.com)

[🇬🇧 English](README.md) · 🇪🇸 Español

</div>

---

Construyo servicios backend y pipelines de datos que lidian con fuentes reales y desordenadas:
registros gubernamentales sin API, documentos normativos escaneados y formatos de archivo
heredados que nunca se pensaron para ser parseados. Casi todo ese trabajo ocurre en el sector
público de salud colombiano.

La mayor parte de mi código profesional vive en repositorios privados de la organización, así
que lo que sigue describe lo que construí en lugar de enlazarlo. Los repositorios públicos de
este perfil son trabajo académico y personal.

## Lo que he construido

**Plataforma de evaluación de candidatos — en producción**
Diseñé y construí el backend (FastAPI, PostgreSQL, Redis, almacenamiento compatible con S3)
detrás de la plataforma que ejecuta los procesos de selección de mi organización, y que ya ha
corrido más de 20 procesos reales a lo largo de dos generaciones. Lo interesante: los ciclos de
vida de examen modelados como máquinas de estado, de modo que una transición inválida falla en
el dominio en vez de filtrarse a los endpoints; una tabla Outbox que dispara las notificaciones
asíncronas; y proctoring remoto con subida de video por fragmentos más un canal WebSocket para
los temporizadores de intento, diseñado para que una conexión caída nunca le cueste el avance a
un candidato. Rehíce el modelo de datos para la segunda generación sin tumbar la primera, que
siguió viva e intacta para auditoría.

**Visor geoespacial de una red regional de salud**
Un motor de ruteo sobre una red vial de 1,4 millones de nodos, que devuelve rutas de referencia
entre prestadores de salud en menos de medio segundo. Consolida 6,8 GB de cartografía nacional
y extractos de OpenStreetMap en un único modelo consultable, validado contra un contrato JSON
Schema para que los datos malformados fallen en la ingesta y no dentro del visor. Está
construido offline-first: todo corre en un portátil institucional sin conexión con un solo
comando `uvicorn` —sin Docker, sin red, sin Node— y con una verificación automática de que el
frontend empaquetado no hace ninguna petición externa.

**Crawler del registro nacional de prestadores de salud**
El registro público de prestadores de salud de Colombia no tiene API. Automaticé su extracción
con Playwright, recolectando los 932 hospitales públicos del país junto con sus sedes,
servicios y capacidad instalada. Persiste el progreso para que una corrida interrumpida se
reanude en lugar de empezar de cero, reparte el trabajo entre workers paralelos y puede
reprocesar únicamente los registros que fallaron.

**ETL normativo de facturación en salud**
La facturación en salud en Colombia pasó de un estándar de archivos planos escrito en el año
2000 al formato JSON jerárquico que exige la normativa de 2023. Construí el ETL de esa
migración, aislando lectores, transformación y salida validada para que un cambio en la
normativa toque una sola capa. La corrección se impone con esquemas Pydantic contra las tablas
de referencia oficiales, no por convención.

**Extracción estructural de documentos legales**
Un pipeline que convierte resoluciones y documentos normativos escaneados en formato legible
por máquina, preservando el orden de lectura original y la estructura de las tablas. La
decisión que lo hizo funcionar: detectar la geometría de la página con OpenCV *antes* de
invocar el modelo de OCR, de manera que este solo ve regiones de texto y celdas de tabla ya
identificadas, nunca páginas completas. Los PDFs con texto embebido se saltan el OCR por
completo.

## Investigación

**[VACS: A Modular Software System for Vehicular Access Control](https://github.com/ZenoexORG/vacs-backend)**
— An Optimized Approach for Automatic License Plate Recognition in Open-Access Environments.
Publicado en Springer CCIS (WEA 2025). Un backend modular en NestJS organizado en módulos de
dominio aislados, con el acceso modelado como reglas aplicables y el reconocimiento de placas
de terceros como fuente de eventos. Proyecto de grado, y el código es público.

## Herramientas que realmente uso

**Lenguajes** Python · TypeScript · JavaScript · SQL · R

**Backend** FastAPI · NestJS · diseño de APIs REST · OpenAPI · Pydantic · SQLAlchemy · Alembic

**Datos** Diseño de pipelines ETL · Playwright · pandas · NumPy · GeoPandas · Shapely · NetworkX

**Bases de datos** PostgreSQL · SQLite · modelado relacional · indexación · migraciones

**Infraestructura** Docker · Docker Compose · Nginx · Redis · GitHub Actions · Linux

**Prácticas** Testing automatizado (pytest) · CI/CD · diseño de contratos de API · escritura técnica

También he construido prototipos de infraestructura con Terraform, Vault y Docker Swarm
(aprovisionamiento de base de datos por tenant), aunque todavía no en producción.

## Ahora mismo

Profundizando en dos cosas en lugar de abarcar muchas: procesamiento distribuido de datos más
allá de pipelines de un solo nodo, y despliegue en la nube con infraestructura como código de
verdad. La distancia entre "lo contenericé" y "lo opero" es la que vale la pena cerrar ahora.

---

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=L30N4RD018&show_icons=true&hide_border=true&hide_title=true&theme=transparent&hide=stars" alt="Estadísticas de GitHub" height="150" />

<img src="https://raw.githubusercontent.com/L30N4RD018/L30N4RD018/output/snake.svg" alt="Snake de contribuciones" />

</div>
