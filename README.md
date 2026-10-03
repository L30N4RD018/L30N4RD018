<div align="center">

# Leonardo Mendoza

**Backend &amp; Data Engineer**

<sub>📍 Cartagena, Colombia</sub>

<a href="https://www.linkedin.com/in/leonardomendoza-dev"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"></a> <a href="mailto:leonardomendoza2003@gmail.com"><img alt="Email" src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white"></a> <a href="https://doi.org/10.1007/978-3-032-08206-0_19"><img alt="DOI" src="https://img.shields.io/badge/DOI-Springer%20WEA%202025-1F4B99?style=for-the-badge&logo=doi&logoColor=white"></a> <a href="https://orcid.org/0009-0005-0598-2239"><img alt="ORCID" src="https://img.shields.io/badge/ORCID-A6CE39?style=for-the-badge&logo=orcid&logoColor=white"></a>

<sub>🇬🇧 English · <a href="README.es.md">🇪🇸 Español</a></sub>

</div>

---

I build backend services and data pipelines in Python, mostly for Colombia's public health
sector, where data rarely comes in a clean format: government registries without an API,
regulations that only exist as scanned PDFs, and file formats designed more than twenty years
ago.

Most of the systems below belong to the organizations I built them for, so their code is
private. Where the code is public, there is a link.

## What I've built

### SEFP: selection process platform &nbsp;<img alt="in production" src="https://img.shields.io/badge/in%20production-1a7f37?style=flat-square">

<img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-555?style=flat-square&logo=fastapi&logoColor=white"> <img alt="PostgreSQL" src="https://img.shields.io/badge/PostgreSQL-555?style=flat-square&logo=postgresql&logoColor=white"> <img alt="Docker" src="https://img.shields.io/badge/Docker-555?style=flat-square&logo=docker&logoColor=white"> <img alt="Next.js" src="https://img.shields.io/badge/Next.js-555?style=flat-square&logo=nextdotjs&logoColor=white">

The platform FUNDASABERES uses to run selection processes for other organizations, from
candidate registration to online exams and evaluation. In production since July 2026. A team
project in which I owned the backend and the data model, and wrote most of the backend's
automated tests. Its first version, COMPETEA, ran more than 20 real selection processes; there
I wrote most of the backend.

### Geovisor: Colombia's healthcare provider network on a map

<img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-555?style=flat-square&logo=fastapi&logoColor=white"> <img alt="GeoPandas" src="https://img.shields.io/badge/GeoPandas-555?style=flat-square&logo=geopandas&logoColor=white"> <img alt="MapLibre" src="https://img.shields.io/badge/MapLibre-555?style=flat-square"> <img alt="OpenStreetMap" src="https://img.shields.io/badge/OpenStreetMap-555?style=flat-square&logo=openstreetmap&logoColor=white">

A web map for analyzing healthcare referral networks across Colombia, built at FUNDASABERES. It
brings together all **19,447 facilities** in the national provider registry, across 33
departments, and calculates road routes between them in **under half a second** over road
networks of up to 1.4 million nodes. It combines 6.8 GB of national maps from DANE and
OpenStreetMap, and it works without an internet connection.

### REPS Scraper &nbsp;<a href="https://github.com/L30N4RD018/reps-scraper"><img alt="code" src="https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white"></a>

<img alt="Python" src="https://img.shields.io/badge/Python-555?style=flat-square&logo=python&logoColor=white"> <img alt="Playwright" src="https://img.shields.io/badge/Playwright-555?style=flat-square&logo=playwright&logoColor=white"> <img alt="SQLite" src="https://img.shields.io/badge/SQLite-555?style=flat-square&logo=sqlite&logoColor=white">

Colombia's national registry of healthcare providers has no API. This program extracts it with
Playwright: all **932 public hospitals** in the country, with their facilities, services, and
installed capacity. It saves its progress, resumes after a failure, and can retry only the
records that failed.

### RIPS Converter

<img alt="Python" src="https://img.shields.io/badge/Python-555?style=flat-square&logo=python&logoColor=white"> <img alt="Pydantic" src="https://img.shields.io/badge/Pydantic-555?style=flat-square&logo=pydantic&logoColor=white"> <img alt="pandas" src="https://img.shields.io/badge/pandas-555?style=flat-square&logo=pandas&logoColor=white">

Colombian health billing moved from a flat-file format defined in 2000 to the JSON structure
required by 2023 regulations. I built the tool that converts the old files to the new format and
checks them against the government's official reference tables.

### doc-ocr &nbsp;<a href="https://github.com/L30N4RD018/doc-ocr"><img alt="code" src="https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white"></a>

<img alt="Python" src="https://img.shields.io/badge/Python-555?style=flat-square&logo=python&logoColor=white"> <img alt="OpenCV" src="https://img.shields.io/badge/OpenCV-555?style=flat-square&logo=opencv&logoColor=white"> <img alt="OCR" src="https://img.shields.io/badge/OCR-555?style=flat-square">

A tool that turns scanned regulations and legal documents into searchable text. It finds the
tables before running OCR, so their columns don't get mixed together.

### NASA Studies API &nbsp;<a href="https://github.com/L30N4RD018/nasa-studies-api"><img alt="code" src="https://img.shields.io/badge/code-181717?style=flat-square&logo=github&logoColor=white"></a>

<img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-555?style=flat-square&logo=fastapi&logoColor=white"> <img alt="llama.cpp" src="https://img.shields.io/badge/llama.cpp-555?style=flat-square"> <img alt="NASA Space Apps 2025" src="https://img.shields.io/badge/NASA%20Space%20Apps%202025-555?style=flat-square&logo=nasa&logoColor=white">

Built at NASA Space Apps Challenge 2025. An API for exploring 1,119 space biology studies from
NASA's Open Science Data Repository. It writes a title and summary for any group of studies
using a language model that runs locally on CPU, and it keeps working with a simpler method when
the model isn't available.

## Research

Two papers published by Springer (CCIS, WEA 2025), written with the same team.

<img alt="Springer" src="https://img.shields.io/badge/Springer-CCIS%20%C2%B7%20WEA%202025-1F4B99?style=flat-square"> <img alt="peer reviewed" src="https://img.shields.io/badge/peer%20reviewed-1a7f37?style=flat-square"> <img alt="NestJS" src="https://img.shields.io/badge/NestJS-555?style=flat-square&logo=nestjs&logoColor=white"> <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-555?style=flat-square&logo=typescript&logoColor=white"> <a href="https://github.com/ZenoexORG/vacs-backend"><img alt="source code" src="https://img.shields.io/badge/source%20code-181717?style=flat-square&logo=github&logoColor=white"></a>

**[VACS: A Modular Software System for Vehicular Access Control](https://doi.org/10.1007/978-3-032-08206-0_19)**
— Alvarino, Taboada, **Mendoza**, Montes &amp; Martinez-Santos. Springer, *Communications in
Computer and Information Science* (WEA 2025), pp. 222–232, October 2025.
[`10.1007/978-3-032-08206-0_19`](https://doi.org/10.1007/978-3-032-08206-0_19)

The backend of the vehicle access control system my team built as our capstone project: a
camera reads each license plate, and the system decides who can enter, records every access,
and flags incidents. The code is public.

<img alt="Springer" src="https://img.shields.io/badge/Springer-CCIS%20%C2%B7%20WEA%202025-1F4B99?style=flat-square"> <img alt="peer reviewed" src="https://img.shields.io/badge/peer%20reviewed-1a7f37?style=flat-square"> <img alt="YOLOv11" src="https://img.shields.io/badge/YOLOv11-555?style=flat-square"> <img alt="OpenCV" src="https://img.shields.io/badge/OpenCV-555?style=flat-square&logo=opencv&logoColor=white"> <img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-555?style=flat-square&logo=fastapi&logoColor=white"> <img alt="Redis" src="https://img.shields.io/badge/Redis-555?style=flat-square&logo=redis&logoColor=white">

**[An Optimized Approach for Automatic License Plate Recognition in Open-Access Environments](https://doi.org/10.1007/978-3-032-08203-9_19)**
— Alvarino, Taboada, **Mendoza** &amp; Martinez-Santos. Springer, *Communications in Computer
and Information Science* (WEA 2025), pp. 223–233, October 2025.
[`10.1007/978-3-032-08203-9_19`](https://doi.org/10.1007/978-3-032-08203-9_19)

The license plate recognition behind VACS, designed for places where plates are seen at
varied angles, distances, and lighting instead of at a controlled gate.

## Tools I actually use

| | |
|:--|:--|
| **Languages** | <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"> <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white"> <img alt="JavaScript" src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black"> <img alt="SQL" src="https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=postgresql&logoColor=white"> <img alt="R" src="https://img.shields.io/badge/R-276DC3?style=flat-square&logo=r&logoColor=white"> |
| **Backend** | <img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white"> <img alt="NestJS" src="https://img.shields.io/badge/NestJS-E0234E?style=flat-square&logo=nestjs&logoColor=white"> <img alt="OpenAPI" src="https://img.shields.io/badge/OpenAPI-6BA539?style=flat-square&logo=openapiinitiative&logoColor=white"> <img alt="Pydantic" src="https://img.shields.io/badge/Pydantic-E92063?style=flat-square&logo=pydantic&logoColor=white"> <img alt="SQLAlchemy" src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat-square&logo=sqlalchemy&logoColor=white"> <img alt="Alembic" src="https://img.shields.io/badge/Alembic-6E4C13?style=flat-square"> |
| **Data** | <img alt="Playwright" src="https://img.shields.io/badge/Playwright-2EAD33?style=flat-square&logo=playwright&logoColor=white"> <img alt="pandas" src="https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white"> <img alt="NumPy" src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white"> <img alt="GeoPandas" src="https://img.shields.io/badge/GeoPandas-139C5A?style=flat-square&logo=geopandas&logoColor=white"> <img alt="Shapely" src="https://img.shields.io/badge/Shapely-4B8BBE?style=flat-square"> <img alt="NetworkX" src="https://img.shields.io/badge/NetworkX-2C5F2D?style=flat-square"> |
| **Databases** | <img alt="PostgreSQL" src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white"> <img alt="SQLite" src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white"> <img alt="Redis" src="https://img.shields.io/badge/Redis-FF4438?style=flat-square&logo=redis&logoColor=white"> |
| **Infrastructure** | <img alt="Docker" src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white"> <img alt="Nginx" src="https://img.shields.io/badge/Nginx-009639?style=flat-square&logo=nginx&logoColor=white"> <img alt="GitHub Actions" src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white"> <img alt="Linux" src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black"> <img alt="Terraform" src="https://img.shields.io/badge/Terraform-7B42BC?style=flat-square&logo=terraform&logoColor=white"> <img alt="Vault" src="https://img.shields.io/badge/Vault-FFEC6E?style=flat-square&logo=vault&logoColor=black"> |
| **Practices** | <img alt="pytest" src="https://img.shields.io/badge/pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white"> <img alt="CI/CD" src="https://img.shields.io/badge/CI%2FCD-2088FF?style=flat-square&logo=githubactions&logoColor=white"> <img alt="API contract design" src="https://img.shields.io/badge/API%20contract%20design-6BA539?style=flat-square&logo=swagger&logoColor=white"> <img alt="Technical writing" src="https://img.shields.io/badge/Technical%20writing-24292F?style=flat-square&logo=markdown&logoColor=white"> |

Relational modeling, indexing, and migrations sit under the database badges. I've also built
infrastructure prototypes with Terraform, Vault, and Docker Swarm, though none of them is in
production yet.

## Currently

Learning two things in depth: processing data across more than one machine, and deploying to
the cloud with infrastructure as code.

---

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/L30N4RD018/L30N4RD018/output/stats-dark.svg">
<img src="https://raw.githubusercontent.com/L30N4RD018/L30N4RD018/output/stats.svg" alt="GitHub stats" height="150">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/L30N4RD018/L30N4RD018/output/top-langs-dark.svg">
<img src="https://raw.githubusercontent.com/L30N4RD018/L30N4RD018/output/top-langs.svg" alt="Top languages" height="150">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/L30N4RD018/L30N4RD018/output/activity-dark.svg">
<img src="https://raw.githubusercontent.com/L30N4RD018/L30N4RD018/output/activity.svg" alt="Contribution activity over the last month">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/L30N4RD018/L30N4RD018/output/snake-dark.svg">
<img src="https://raw.githubusercontent.com/L30N4RD018/L30N4RD018/output/snake.svg" alt="Contribution snake">
</picture>

</div>
