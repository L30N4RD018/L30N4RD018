<div align="center">

# Leonardo Mendoza

**Backend &amp; Data Engineer**

<sub>📍 Cartagena, Colombia</sub>

<a href="https://www.linkedin.com/in/leonardomendoza-dev"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"></a> <a href="mailto:leonardomendoza2003@gmail.com"><img alt="Email" src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white"></a> <a href="https://doi.org/10.1007/978-3-032-08206-0_19"><img alt="DOI" src="https://img.shields.io/badge/DOI-Springer%20WEA%202025-1F4B99?style=for-the-badge&logo=doi&logoColor=white"></a> <a href="https://orcid.org/0009-0005-0598-2239"><img alt="ORCID" src="https://img.shields.io/badge/ORCID-A6CE39?style=for-the-badge&logo=orcid&logoColor=white"></a>

<sub><a href="README.md">🇬🇧 English</a> · 🇪🇸 Español</sub>

</div>

---

Construyo servicios backend y flujos de datos en Python, sobre todo para el sector salud en
Colombia, donde la información rara vez llega limpia: registros públicos sin API, normas que solo
existen como PDF escaneados y formatos de archivo de hace más de veinte años.

La mayoría de los sistemas de abajo pertenecen a las organizaciones para las que los construí,
así que su código es privado. Cuando el código es público, está enlazado.

## Lo que he construido

### SEFP: plataforma de procesos de selección &nbsp;<img alt="en producción" src="https://img.shields.io/badge/en%20producci%C3%B3n-1a7f37?style=flat-square">

<img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-555?style=flat-square&logo=fastapi&logoColor=white"> <img alt="PostgreSQL" src="https://img.shields.io/badge/PostgreSQL-555?style=flat-square&logo=postgresql&logoColor=white"> <img alt="Docker" src="https://img.shields.io/badge/Docker-555?style=flat-square&logo=docker&logoColor=white"> <img alt="Next.js" src="https://img.shields.io/badge/Next.js-555?style=flat-square&logo=nextdotjs&logoColor=white">

La plataforma con la que FUNDASABERES adelanta procesos de selección para otras entidades, desde
la inscripción de los candidatos hasta los exámenes en línea y la evaluación. Está en producción
desde julio de 2026. Es un proyecto de equipo en el que estuve a cargo del backend y del modelo
de datos, y escribí la mayor parte de las pruebas automatizadas del backend. Con su primera
versión, COMPETEA, se adelantaron más de 20 procesos de selección reales; ahí desarrollé la
mayor parte del backend.

### Geovisor: la red de prestadores de salud de Colombia en un mapa

<img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-555?style=flat-square&logo=fastapi&logoColor=white"> <img alt="GeoPandas" src="https://img.shields.io/badge/GeoPandas-555?style=flat-square&logo=geopandas&logoColor=white"> <img alt="MapLibre" src="https://img.shields.io/badge/MapLibre-555?style=flat-square"> <img alt="OpenStreetMap" src="https://img.shields.io/badge/OpenStreetMap-555?style=flat-square&logo=openstreetmap&logoColor=white">

Visor geográfico para analizar las redes de referencia en salud del país, construido en
FUNDASABERES. Reúne las **19.447 sedes** del registro nacional de prestadores en los 33
departamentos y calcula rutas por carretera entre ellas en **menos de medio segundo**, sobre
redes viales de hasta 1,4 millones de nodos. Integra 6,8 GB de cartografía nacional del DANE y
de OpenStreetMap, y funciona sin conexión a internet.

### REPS Scraper &nbsp;<a href="https://github.com/L30N4RD018/reps-scraper"><img alt="code" src="https://img.shields.io/badge/c%C3%B3digo-181717?style=flat-square&logo=github&logoColor=white"></a>

<img alt="Python" src="https://img.shields.io/badge/Python-555?style=flat-square&logo=python&logoColor=white"> <img alt="Playwright" src="https://img.shields.io/badge/Playwright-555?style=flat-square&logo=playwright&logoColor=white"> <img alt="SQLite" src="https://img.shields.io/badge/SQLite-555?style=flat-square&logo=sqlite&logoColor=white">

El Registro Especial de Prestadores de Servicios de Salud (REPS) no tiene API. Este programa lo
extrae con Playwright: los **932 hospitales públicos** del país, con sus sedes, servicios y
capacidad instalada. Guarda su avance, retoma donde quedó si algo falla y puede reintentar solo
los registros que fallaron.

### Conversor de RIPS

<img alt="Python" src="https://img.shields.io/badge/Python-555?style=flat-square&logo=python&logoColor=white"> <img alt="Pydantic" src="https://img.shields.io/badge/Pydantic-555?style=flat-square&logo=pydantic&logoColor=white"> <img alt="pandas" src="https://img.shields.io/badge/pandas-555?style=flat-square&logo=pandas&logoColor=white">

La facturación en salud en Colombia pasó de un formato de archivos planos del año 2000 a la
estructura JSON que exige la normativa de 2023. Construí la herramienta que convierte los
archivos antiguos al formato nuevo y los valida contra las tablas de referencia oficiales.

### doc-ocr &nbsp;<a href="https://github.com/L30N4RD018/doc-ocr"><img alt="code" src="https://img.shields.io/badge/c%C3%B3digo-181717?style=flat-square&logo=github&logoColor=white"></a>

<img alt="Python" src="https://img.shields.io/badge/Python-555?style=flat-square&logo=python&logoColor=white"> <img alt="OpenCV" src="https://img.shields.io/badge/OpenCV-555?style=flat-square&logo=opencv&logoColor=white"> <img alt="OCR" src="https://img.shields.io/badge/OCR-555?style=flat-square">

Una herramienta que convierte normas y documentos legales escaneados en texto consultable.
Detecta las tablas antes de aplicar OCR, para que sus columnas no se mezclen.

### NASA Studies API &nbsp;<a href="https://github.com/L30N4RD018/nasa-studies-api"><img alt="code" src="https://img.shields.io/badge/c%C3%B3digo-181717?style=flat-square&logo=github&logoColor=white"></a>

<img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-555?style=flat-square&logo=fastapi&logoColor=white"> <img alt="llama.cpp" src="https://img.shields.io/badge/llama.cpp-555?style=flat-square"> <img alt="NASA Space Apps 2025" src="https://img.shields.io/badge/NASA%20Space%20Apps%202025-555?style=flat-square&logo=nasa&logoColor=white">

Proyecto del NASA Space Apps Challenge 2025. Una API para explorar 1.119 estudios de biología
espacial del repositorio de datos abiertos de la NASA. Redacta un título y un resumen para
cualquier grupo de estudios con un modelo de lenguaje que corre en local, en CPU, y sigue
funcionando con un método más simple cuando el modelo no está disponible.

## Investigación

Dos artículos publicados por Springer (CCIS, WEA 2025), escritos con el mismo equipo.

<img alt="Springer" src="https://img.shields.io/badge/Springer-CCIS%20%C2%B7%20WEA%202025-1F4B99?style=flat-square"> <img alt="revisado por pares" src="https://img.shields.io/badge/revisado%20por%20pares-1a7f37?style=flat-square"> <img alt="NestJS" src="https://img.shields.io/badge/NestJS-555?style=flat-square&logo=nestjs&logoColor=white"> <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-555?style=flat-square&logo=typescript&logoColor=white"> <a href="https://github.com/ZenoexORG/vacs-backend"><img alt="código fuente" src="https://img.shields.io/badge/c%C3%B3digo%20fuente-181717?style=flat-square&logo=github&logoColor=white"></a>

**[VACS: A Modular Software System for Vehicular Access Control](https://doi.org/10.1007/978-3-032-08206-0_19)**
— Alvarino, Taboada, **Mendoza**, Montes y Martinez-Santos. Springer, *Communications in
Computer and Information Science* (WEA 2025), pp. 222–232, octubre de 2025.
[`10.1007/978-3-032-08206-0_19`](https://doi.org/10.1007/978-3-032-08206-0_19)

El backend del sistema de control de acceso vehicular que desarrollamos como proyecto de
grado: una cámara lee cada placa y el sistema decide quién puede entrar, registra cada acceso y
señala los incidentes. El código es público.

<img alt="Springer" src="https://img.shields.io/badge/Springer-CCIS%20%C2%B7%20WEA%202025-1F4B99?style=flat-square"> <img alt="revisado por pares" src="https://img.shields.io/badge/revisado%20por%20pares-1a7f37?style=flat-square"> <img alt="YOLOv11" src="https://img.shields.io/badge/YOLOv11-555?style=flat-square"> <img alt="OpenCV" src="https://img.shields.io/badge/OpenCV-555?style=flat-square&logo=opencv&logoColor=white"> <img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-555?style=flat-square&logo=fastapi&logoColor=white"> <img alt="Redis" src="https://img.shields.io/badge/Redis-555?style=flat-square&logo=redis&logoColor=white">

**[An Optimized Approach for Automatic License Plate Recognition in Open-Access Environments](https://doi.org/10.1007/978-3-032-08203-9_19)**
— Alvarino, Taboada, **Mendoza** y Martinez-Santos. Springer, *Communications in Computer and
Information Science* (WEA 2025), pp. 223–233, octubre de 2025.
[`10.1007/978-3-032-08203-9_19`](https://doi.org/10.1007/978-3-032-08203-9_19)

El reconocimiento de placas que hay detrás de VACS, pensado para lugares donde las placas se
ven desde distintos ángulos, distancias e iluminación, y no frente a una talanquera.

## Herramientas que realmente uso

| | |
|:--|:--|
| **Lenguajes** | <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"> <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white"> <img alt="JavaScript" src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black"> <img alt="SQL" src="https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=postgresql&logoColor=white"> <img alt="R" src="https://img.shields.io/badge/R-276DC3?style=flat-square&logo=r&logoColor=white"> |
| **Backend** | <img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white"> <img alt="NestJS" src="https://img.shields.io/badge/NestJS-E0234E?style=flat-square&logo=nestjs&logoColor=white"> <img alt="OpenAPI" src="https://img.shields.io/badge/OpenAPI-6BA539?style=flat-square&logo=openapiinitiative&logoColor=white"> <img alt="Pydantic" src="https://img.shields.io/badge/Pydantic-E92063?style=flat-square&logo=pydantic&logoColor=white"> <img alt="SQLAlchemy" src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat-square&logo=sqlalchemy&logoColor=white"> <img alt="Alembic" src="https://img.shields.io/badge/Alembic-6E4C13?style=flat-square"> |
| **Datos** | <img alt="Playwright" src="https://img.shields.io/badge/Playwright-2EAD33?style=flat-square&logo=playwright&logoColor=white"> <img alt="pandas" src="https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white"> <img alt="NumPy" src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white"> <img alt="GeoPandas" src="https://img.shields.io/badge/GeoPandas-139C5A?style=flat-square&logo=geopandas&logoColor=white"> <img alt="Shapely" src="https://img.shields.io/badge/Shapely-4B8BBE?style=flat-square"> <img alt="NetworkX" src="https://img.shields.io/badge/NetworkX-2C5F2D?style=flat-square"> |
| **Bases de datos** | <img alt="PostgreSQL" src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white"> <img alt="SQLite" src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white"> <img alt="Redis" src="https://img.shields.io/badge/Redis-FF4438?style=flat-square&logo=redis&logoColor=white"> |
| **Infraestructura** | <img alt="Docker" src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white"> <img alt="Nginx" src="https://img.shields.io/badge/Nginx-009639?style=flat-square&logo=nginx&logoColor=white"> <img alt="GitHub Actions" src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white"> <img alt="Linux" src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black"> <img alt="Terraform" src="https://img.shields.io/badge/Terraform-7B42BC?style=flat-square&logo=terraform&logoColor=white"> <img alt="Vault" src="https://img.shields.io/badge/Vault-FFEC6E?style=flat-square&logo=vault&logoColor=black"> |
| **Prácticas** | <img alt="pytest" src="https://img.shields.io/badge/pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white"> <img alt="CI/CD" src="https://img.shields.io/badge/CI%2FCD-2088FF?style=flat-square&logo=githubactions&logoColor=white"> <img alt="Contratos de API" src="https://img.shields.io/badge/Contratos%20de%20API-6BA539?style=flat-square&logo=swagger&logoColor=white"> <img alt="Escritura técnica" src="https://img.shields.io/badge/Escritura%20t%C3%A9cnica-24292F?style=flat-square&logo=markdown&logoColor=white"> |

El modelado relacional, la indexación y las migraciones van bajo las insignias de bases de
datos. También he construido prototipos de infraestructura con Terraform, Vault y Docker Swarm,
aunque ninguno está en producción todavía.

## Ahora mismo

Estoy profundizando en dos temas: procesar datos en más de una máquina y desplegar en la nube
con infraestructura como código.

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
