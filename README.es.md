<div align="center">

# Leonardo Mendoza

**Backend &amp; Data Engineer**

<sub>📍 Cartagena, Colombia</sub>

<a href="https://www.linkedin.com/in/leonardomendoza-dev"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"></a> <a href="mailto:leonardomendoza2003@gmail.com"><img alt="Email" src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white"></a> <a href="https://doi.org/10.1007/978-3-032-08206-0_19"><img alt="DOI" src="https://img.shields.io/badge/DOI-Springer%20WEA%202025-1F4B99?style=for-the-badge&logo=doi&logoColor=white"></a> <a href="https://orcid.org/0009-0005-0598-2239"><img alt="ORCID" src="https://img.shields.io/badge/ORCID-A6CE39?style=for-the-badge&logo=orcid&logoColor=white"></a>

<sub><a href="README.md">🇬🇧 English</a> · 🇪🇸 Español</sub>

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

### Plataforma de evaluación de candidatos &nbsp;<img alt="en producción" src="https://img.shields.io/badge/en%20producci%C3%B3n-1a7f37?style=flat-square">

<img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-555?style=flat-square&logo=fastapi&logoColor=white"> <img alt="PostgreSQL" src="https://img.shields.io/badge/PostgreSQL-555?style=flat-square&logo=postgresql&logoColor=white"> <img alt="Redis" src="https://img.shields.io/badge/Redis-555?style=flat-square&logo=redis&logoColor=white"> <img alt="WebSockets" src="https://img.shields.io/badge/WebSockets-555?style=flat-square&logo=socketdotio&logoColor=white"> <img alt="S3" src="https://img.shields.io/badge/S3--compatible-555?style=flat-square&logo=minio&logoColor=white">

Diseñé y construí el backend detrás de la plataforma que ejecuta los procesos de selección de
mi organización, y que ya ha corrido más de 20 procesos reales a lo largo de dos generaciones.
Lo interesante: los ciclos de vida de examen modelados como máquinas de estado, de modo que una
transición inválida falla en el dominio en vez de filtrarse a los endpoints; una tabla Outbox
que dispara las notificaciones asíncronas; y proctoring remoto con subida de video por
fragmentos más un canal WebSocket para los temporizadores de intento, diseñado para que una
conexión caída nunca le cueste el avance a un candidato. Rehíce el modelo de datos para la
segunda generación sin tumbar la primera, que siguió viva e intacta para auditoría.

### Visor geoespacial de una red regional de salud

<img alt="NetworkX" src="https://img.shields.io/badge/NetworkX-555?style=flat-square&logo=python&logoColor=white"> <img alt="GeoPandas" src="https://img.shields.io/badge/GeoPandas-555?style=flat-square&logo=geopandas&logoColor=white"> <img alt="OpenStreetMap" src="https://img.shields.io/badge/OpenStreetMap-555?style=flat-square&logo=openstreetmap&logoColor=white"> <img alt="JSON Schema" src="https://img.shields.io/badge/JSON%20Schema-555?style=flat-square&logo=json&logoColor=white"> <img alt="offline-first" src="https://img.shields.io/badge/offline--first-555?style=flat-square&logo=linux&logoColor=white">

Un motor de ruteo sobre una red vial de **1,4 millones de nodos**, que devuelve rutas de
referencia entre prestadores de salud en **menos de medio segundo**. Consolida 6,8 GB de
cartografía nacional y extractos de OpenStreetMap en un único modelo consultable, validado
contra un contrato JSON Schema para que los datos malformados fallen en la ingesta y no dentro
del visor. Está construido offline-first: todo corre en un portátil institucional sin conexión
con un solo comando `uvicorn` —sin Docker, sin red, sin Node— y con una verificación automática
de que el frontend empaquetado no hace ninguna petición externa.

### Crawler del registro nacional de prestadores de salud

<img alt="Playwright" src="https://img.shields.io/badge/Playwright-555?style=flat-square&logo=playwright&logoColor=white"> <img alt="Python" src="https://img.shields.io/badge/Python-555?style=flat-square&logo=python&logoColor=white"> <img alt="SQLite" src="https://img.shields.io/badge/SQLite-555?style=flat-square&logo=sqlite&logoColor=white"> <img alt="reanudable" src="https://img.shields.io/badge/reanudable-555?style=flat-square">

El registro público de prestadores de salud de Colombia no tiene API. Automaticé su extracción
con Playwright, recolectando los **932 hospitales públicos** del país junto con sus sedes,
servicios y capacidad instalada. Persiste el progreso para que una corrida interrumpida se
reanude en lugar de empezar de cero, reparte el trabajo entre workers paralelos y puede
reprocesar únicamente los registros que fallaron.

### ETL normativo de facturación en salud

<img alt="Pydantic" src="https://img.shields.io/badge/Pydantic-555?style=flat-square&logo=pydantic&logoColor=white"> <img alt="pandas" src="https://img.shields.io/badge/pandas-555?style=flat-square&logo=pandas&logoColor=white"> <img alt="ETL" src="https://img.shields.io/badge/ETL-555?style=flat-square">

La facturación en salud en Colombia pasó de un estándar de archivos planos escrito en el año
2000 al formato JSON jerárquico que exige la normativa de 2023. Construí el ETL de esa
migración, aislando lectores, transformación y salida validada para que un cambio en la
normativa toque una sola capa. La corrección se impone con esquemas Pydantic contra las tablas
de referencia oficiales, no por convención.

### Extracción estructural de documentos legales

<img alt="OpenCV" src="https://img.shields.io/badge/OpenCV-555?style=flat-square&logo=opencv&logoColor=white"> <img alt="OCR" src="https://img.shields.io/badge/OCR-555?style=flat-square"> <img alt="NumPy" src="https://img.shields.io/badge/NumPy-555?style=flat-square&logo=numpy&logoColor=white">

Un pipeline que convierte resoluciones y documentos normativos escaneados en formato legible
por máquina, preservando el orden de lectura original y la estructura de las tablas. La
decisión que lo hizo funcionar: detectar la geometría de la página con OpenCV *antes* de
invocar el modelo de OCR, de manera que este solo ve regiones de texto y celdas de tabla ya
identificadas, nunca páginas completas. Los PDFs con texto embebido se saltan el OCR por
completo.

## Investigación

Dos capítulos de la misma serie de volúmenes Springer CCIS de WEA 2025, escritos con el mismo
equipo: uno sobre el sistema de control de acceso y otro sobre el pipeline de reconocimiento de
placas que lo alimenta.

<img alt="Springer" src="https://img.shields.io/badge/Springer-CCIS%20%C2%B7%20WEA%202025-1F4B99?style=flat-square"> <img alt="revisado por pares" src="https://img.shields.io/badge/revisado%20por%20pares-1a7f37?style=flat-square"> <img alt="NestJS" src="https://img.shields.io/badge/NestJS-555?style=flat-square&logo=nestjs&logoColor=white"> <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-555?style=flat-square&logo=typescript&logoColor=white"> <a href="https://github.com/ZenoexORG/vacs-backend"><img alt="código fuente" src="https://img.shields.io/badge/c%C3%B3digo%20fuente-181717?style=flat-square&logo=github&logoColor=white"></a>

**[VACS: A Modular Software System for Vehicular Access Control](https://doi.org/10.1007/978-3-032-08206-0_19)**
— Alvarino, Taboada, **Mendoza**, Montes y Martinez-Santos. Springer, *Communications in
Computer and Information Science* (WEA 2025), pp. 222–232, octubre de 2025.
[`10.1007/978-3-032-08206-0_19`](https://doi.org/10.1007/978-3-032-08206-0_19)

Un backend modular en NestJS organizado en módulos de dominio aislados, con el acceso modelado
como reglas aplicables y el reconocimiento de placas como fuente de eventos. Proyecto de grado,
y el código es público.

<img alt="Springer" src="https://img.shields.io/badge/Springer-CCIS%20%C2%B7%20WEA%202025-1F4B99?style=flat-square"> <img alt="revisado por pares" src="https://img.shields.io/badge/revisado%20por%20pares-1a7f37?style=flat-square"> <img alt="YOLOv11" src="https://img.shields.io/badge/YOLOv11-555?style=flat-square"> <img alt="OpenCV" src="https://img.shields.io/badge/OpenCV-555?style=flat-square&logo=opencv&logoColor=white"> <img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-555?style=flat-square&logo=fastapi&logoColor=white"> <img alt="Redis" src="https://img.shields.io/badge/Redis-555?style=flat-square&logo=redis&logoColor=white">

**[An Optimized Approach for Automatic License Plate Recognition in Open-Access Environments](https://doi.org/10.1007/978-3-032-08203-9_19)**
— Alvarino, Taboada, **Mendoza** y Martinez-Santos. Springer, *Communications in Computer and
Information Science* (WEA 2025), pp. 223–233, octubre de 2025.
[`10.1007/978-3-032-08203-9_19`](https://doi.org/10.1007/978-3-032-08203-9_19)

El pipeline de reconocimiento que hay detrás de VACS: detección y OCR ajustados a entornos de
acceso abierto, donde las placas llegan en ángulos, distancias e iluminación sin controlar en
vez de en una talanquera. Se sirve sobre FastAPI con Redis por delante.

## Herramientas que realmente uso

| | |
|:--|:--|
| **Lenguajes** | <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"> <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white"> <img alt="JavaScript" src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black"> <img alt="SQL" src="https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=postgresql&logoColor=white"> <img alt="R" src="https://img.shields.io/badge/R-276DC3?style=flat-square&logo=r&logoColor=white"> |
| **Backend** | <img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white"> <img alt="NestJS" src="https://img.shields.io/badge/NestJS-E0234E?style=flat-square&logo=nestjs&logoColor=white"> <img alt="OpenAPI" src="https://img.shields.io/badge/OpenAPI-6BA539?style=flat-square&logo=openapiinitiative&logoColor=white"> <img alt="Pydantic" src="https://img.shields.io/badge/Pydantic-E92063?style=flat-square&logo=pydantic&logoColor=white"> <img alt="SQLAlchemy" src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat-square&logo=sqlalchemy&logoColor=white"> <img alt="Alembic" src="https://img.shields.io/badge/Alembic-6E4C13?style=flat-square"> |
| **Datos** | <img alt="Playwright" src="https://img.shields.io/badge/Playwright-2EAD33?style=flat-square&logo=playwright&logoColor=white"> <img alt="pandas" src="https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white"> <img alt="NumPy" src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white"> <img alt="GeoPandas" src="https://img.shields.io/badge/GeoPandas-139C5A?style=flat-square&logo=geopandas&logoColor=white"> <img alt="Shapely" src="https://img.shields.io/badge/Shapely-4B8BBE?style=flat-square"> <img alt="NetworkX" src="https://img.shields.io/badge/NetworkX-2C5F2D?style=flat-square"> |
| **Bases de datos** | <img alt="PostgreSQL" src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white"> <img alt="SQLite" src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white"> <img alt="Redis" src="https://img.shields.io/badge/Redis-FF4438?style=flat-square&logo=redis&logoColor=white"> |
| **Infraestructura** | <img alt="Docker" src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white"> <img alt="Nginx" src="https://img.shields.io/badge/Nginx-009639?style=flat-square&logo=nginx&logoColor=white"> <img alt="GitHub Actions" src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white"> <img alt="Linux" src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black"> <img alt="Terraform" src="https://img.shields.io/badge/Terraform-7B42BC?style=flat-square&logo=terraform&logoColor=white"> <img alt="Vault" src="https://img.shields.io/badge/Vault-FFEC6E?style=flat-square&logo=vault&logoColor=black"> |
| **Prácticas** | <img alt="pytest" src="https://img.shields.io/badge/pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white"> <img alt="CI/CD" src="https://img.shields.io/badge/CI%2FCD-2088FF?style=flat-square&logo=githubactions&logoColor=white"> <img alt="Contratos de API" src="https://img.shields.io/badge/Contratos%20de%20API-6BA539?style=flat-square&logo=swagger&logoColor=white"> <img alt="Escritura técnica" src="https://img.shields.io/badge/Escritura%20t%C3%A9cnica-24292F?style=flat-square&logo=markdown&logoColor=white"> |

El modelado relacional, la indexación y las migraciones viven bajo los badges de bases de
datos; el diseño de pipelines ETL y el diseño de contratos de API son las partes en las que más
pienso y las que ningún logo representa. También he construido prototipos de infraestructura
con Terraform, Vault y Docker Swarm (aprovisionamiento de base de datos por tenant), aunque
todavía no en producción.

## Ahora mismo

Profundizando en dos cosas en lugar de abarcar muchas: procesamiento distribuido de datos más
allá de pipelines de un solo nodo, y despliegue en la nube con infraestructura como código de
verdad. La distancia entre "lo contenericé" y "lo opero" es la que vale la pena cerrar ahora.

---

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/L30N4RD018/L30N4RD018/output/stats-dark.svg">
<img src="https://raw.githubusercontent.com/L30N4RD018/L30N4RD018/output/stats.svg" alt="Estadísticas de GitHub" height="150">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/L30N4RD018/L30N4RD018/output/top-langs-dark.svg">
<img src="https://raw.githubusercontent.com/L30N4RD018/L30N4RD018/output/top-langs.svg" alt="Lenguajes más usados" height="150">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/L30N4RD018/L30N4RD018/output/activity-dark.svg">
<img src="https://raw.githubusercontent.com/L30N4RD018/L30N4RD018/output/activity.svg" alt="Actividad de contribuciones del último mes">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/L30N4RD018/L30N4RD018/output/snake-dark.svg">
<img src="https://raw.githubusercontent.com/L30N4RD018/L30N4RD018/output/snake.svg" alt="Snake de contribuciones">
</picture>

</div>
