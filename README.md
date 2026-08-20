<div align="center">

# Leonardo Mendoza

**Backend &amp; Data Engineer**

<sub>📍 Cartagena, Colombia</sub>

<a href="https://www.linkedin.com/in/leonardomendoza-dev"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"></a> <a href="mailto:leonardomendoza2003@gmail.com"><img alt="Email" src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white"></a> <a href="https://doi.org/10.1007/978-3-032-08206-0_19"><img alt="DOI" src="https://img.shields.io/badge/DOI-Springer%20WEA%202025-1F4B99?style=for-the-badge&logo=doi&logoColor=white"></a> <a href="https://orcid.org/0009-0005-0598-2239"><img alt="ORCID" src="https://img.shields.io/badge/ORCID-A6CE39?style=for-the-badge&logo=orcid&logoColor=white"></a>

<sub>🇬🇧 English · <a href="README.es.md">🇪🇸 Español</a></sub>

</div>

---

I build backend services and data pipelines that deal with messy, real-world sources:
government registries with no API, scanned regulatory documents, and legacy file formats that
were never meant to be parsed. Most of that work is in the Colombian public-health sector.

Most of my professional code lives in private organisational repositories, so what follows
describes what I built rather than linking to it. The public repositories on this profile are
academic and personal work.

## What I've built

### Candidate assessment platform &nbsp;<img alt="in production" src="https://img.shields.io/badge/in%20production-1a7f37?style=flat-square">

<img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-555?style=flat-square&logo=fastapi&logoColor=white"> <img alt="PostgreSQL" src="https://img.shields.io/badge/PostgreSQL-555?style=flat-square&logo=postgresql&logoColor=white"> <img alt="Redis" src="https://img.shields.io/badge/Redis-555?style=flat-square&logo=redis&logoColor=white"> <img alt="WebSockets" src="https://img.shields.io/badge/WebSockets-555?style=flat-square&logo=socketdotio&logoColor=white"> <img alt="S3" src="https://img.shields.io/badge/S3--compatible-555?style=flat-square&logo=minio&logoColor=white">

Designed and built the backend behind the platform that runs my organisation's selection
processes, which has carried 20+ real selection rounds across two generations. The interesting
parts: exam lifecycles modelled as state machines, so invalid transitions fail in the domain
instead of leaking into endpoints; an Outbox table driving asynchronous notifications; and
remote proctoring with chunked video upload plus a WebSocket channel for attempt timers,
designed so a dropped connection never costs a candidate their progress. I rebuilt the data
model for the second generation while the first stayed live and untouched for audit.

### Geospatial viewer for a regional healthcare network

<img alt="NetworkX" src="https://img.shields.io/badge/NetworkX-555?style=flat-square&logo=python&logoColor=white"> <img alt="GeoPandas" src="https://img.shields.io/badge/GeoPandas-555?style=flat-square&logo=geopandas&logoColor=white"> <img alt="OpenStreetMap" src="https://img.shields.io/badge/OpenStreetMap-555?style=flat-square&logo=openstreetmap&logoColor=white"> <img alt="JSON Schema" src="https://img.shields.io/badge/JSON%20Schema-555?style=flat-square&logo=json&logoColor=white"> <img alt="offline-first" src="https://img.shields.io/badge/offline--first-555?style=flat-square&logo=linux&logoColor=white">

A routing engine over a road network of **1.4 million nodes**, returning referral routes between
healthcare facilities in **under half a second**. It consolidates 6.8 GB of national cartography
and OpenStreetMap extracts into a single queryable model, validated against a JSON Schema
contract so malformed data fails at ingestion rather than in the viewer. Built offline-first:
the whole thing runs on a disconnected institutional laptop from a single `uvicorn` command —
no Docker, no network, no Node runtime — with an automated check that the bundled front end
makes zero external requests.

### National health registry crawler

<img alt="Playwright" src="https://img.shields.io/badge/Playwright-555?style=flat-square&logo=playwright&logoColor=white"> <img alt="Python" src="https://img.shields.io/badge/Python-555?style=flat-square&logo=python&logoColor=white"> <img alt="SQLite" src="https://img.shields.io/badge/SQLite-555?style=flat-square&logo=sqlite&logoColor=white"> <img alt="resumable" src="https://img.shields.io/badge/resumable-555?style=flat-square">

Colombia's public healthcare provider registry has no API. I automated its extraction with
Playwright, collecting all **932 public hospitals** in the country along with their facilities,
services and installed capacity. It persists progress so an interrupted run resumes instead of
restarting, partitions work across parallel workers, and can reprocess only the records that
failed.

### Regulatory ETL for healthcare billing

<img alt="Pydantic" src="https://img.shields.io/badge/Pydantic-555?style=flat-square&logo=pydantic&logoColor=white"> <img alt="pandas" src="https://img.shields.io/badge/pandas-555?style=flat-square&logo=pandas&logoColor=white"> <img alt="ETL" src="https://img.shields.io/badge/ETL-555?style=flat-square">

Colombian health billing moved from a flat-file standard written in 2000 to the hierarchical
JSON format required by 2023 regulation. I built the ETL for that migration, isolating readers,
transformation and validated output so an amendment to the regulation touches a single layer.
Correctness is enforced by Pydantic schemas against official government reference tables, not
by convention.

### Document understanding for legal PDFs

<img alt="OpenCV" src="https://img.shields.io/badge/OpenCV-555?style=flat-square&logo=opencv&logoColor=white"> <img alt="OCR" src="https://img.shields.io/badge/OCR-555?style=flat-square"> <img alt="NumPy" src="https://img.shields.io/badge/NumPy-555?style=flat-square&logo=numpy&logoColor=white">

A pipeline that converts scanned resolutions and regulatory documents into machine-readable
form, preserving the original reading order and table structure. The decision that made it
work: detect page geometry with OpenCV *before* invoking the OCR model, so it only ever sees
pre-identified text regions and individual table cells rather than whole pages. PDFs with
embedded text skip OCR entirely.

## Research

Two chapters in the same Springer CCIS volume series from WEA 2025, written with the same team:
one on the access-control system, one on the plate-recognition pipeline that feeds it.

<img alt="Springer" src="https://img.shields.io/badge/Springer-CCIS%20%C2%B7%20WEA%202025-1F4B99?style=flat-square"> <img alt="peer reviewed" src="https://img.shields.io/badge/peer%20reviewed-1a7f37?style=flat-square"> <img alt="NestJS" src="https://img.shields.io/badge/NestJS-555?style=flat-square&logo=nestjs&logoColor=white"> <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-555?style=flat-square&logo=typescript&logoColor=white"> <a href="https://github.com/ZenoexORG/vacs-backend"><img alt="source code" src="https://img.shields.io/badge/source%20code-181717?style=flat-square&logo=github&logoColor=white"></a>

**[VACS: A Modular Software System for Vehicular Access Control](https://doi.org/10.1007/978-3-032-08206-0_19)**
— Alvarino, Taboada, **Mendoza**, Montes &amp; Martinez-Santos. Springer, *Communications in
Computer and Information Science* (WEA 2025), pp. 222–232, October 2025.
[`10.1007/978-3-032-08206-0_19`](https://doi.org/10.1007/978-3-032-08206-0_19)

A modular NestJS backend organised around isolated domain modules, with access modelled as
enforceable rules and plate recognition as the event source. Capstone project, and the code is
public.

<img alt="Springer" src="https://img.shields.io/badge/Springer-CCIS%20%C2%B7%20WEA%202025-1F4B99?style=flat-square"> <img alt="peer reviewed" src="https://img.shields.io/badge/peer%20reviewed-1a7f37?style=flat-square"> <img alt="YOLOv11" src="https://img.shields.io/badge/YOLOv11-555?style=flat-square"> <img alt="OpenCV" src="https://img.shields.io/badge/OpenCV-555?style=flat-square&logo=opencv&logoColor=white"> <img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-555?style=flat-square&logo=fastapi&logoColor=white"> <img alt="Redis" src="https://img.shields.io/badge/Redis-555?style=flat-square&logo=redis&logoColor=white">

**[An Optimized Approach for Automatic License Plate Recognition in Open-Access Environments](https://doi.org/10.1007/978-3-032-08203-9_19)**
— Alvarino, Taboada, **Mendoza** &amp; Martinez-Santos. Springer, *Communications in Computer
and Information Science* (WEA 2025), pp. 223–233, October 2025.
[`10.1007/978-3-032-08203-9_19`](https://doi.org/10.1007/978-3-032-08203-9_19)

The recognition pipeline behind VACS: detection and OCR tuned for open-access environments,
where plates arrive at unconstrained angles, distances and lighting rather than at a controlled
barrier. Served over FastAPI with Redis in front of it.

## Tools I actually use

| | |
|:--|:--|
| **Languages** | <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"> <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white"> <img alt="JavaScript" src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black"> <img alt="SQL" src="https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=postgresql&logoColor=white"> <img alt="R" src="https://img.shields.io/badge/R-276DC3?style=flat-square&logo=r&logoColor=white"> |
| **Backend** | <img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white"> <img alt="NestJS" src="https://img.shields.io/badge/NestJS-E0234E?style=flat-square&logo=nestjs&logoColor=white"> <img alt="OpenAPI" src="https://img.shields.io/badge/OpenAPI-6BA539?style=flat-square&logo=openapiinitiative&logoColor=white"> <img alt="Pydantic" src="https://img.shields.io/badge/Pydantic-E92063?style=flat-square&logo=pydantic&logoColor=white"> <img alt="SQLAlchemy" src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat-square&logo=sqlalchemy&logoColor=white"> <img alt="Alembic" src="https://img.shields.io/badge/Alembic-6E4C13?style=flat-square"> |
| **Data** | <img alt="Playwright" src="https://img.shields.io/badge/Playwright-2EAD33?style=flat-square&logo=playwright&logoColor=white"> <img alt="pandas" src="https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white"> <img alt="NumPy" src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white"> <img alt="GeoPandas" src="https://img.shields.io/badge/GeoPandas-139C5A?style=flat-square&logo=geopandas&logoColor=white"> <img alt="Shapely" src="https://img.shields.io/badge/Shapely-4B8BBE?style=flat-square"> <img alt="NetworkX" src="https://img.shields.io/badge/NetworkX-2C5F2D?style=flat-square"> |
| **Databases** | <img alt="PostgreSQL" src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white"> <img alt="SQLite" src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white"> <img alt="Redis" src="https://img.shields.io/badge/Redis-FF4438?style=flat-square&logo=redis&logoColor=white"> |
| **Infrastructure** | <img alt="Docker" src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white"> <img alt="Nginx" src="https://img.shields.io/badge/Nginx-009639?style=flat-square&logo=nginx&logoColor=white"> <img alt="GitHub Actions" src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white"> <img alt="Linux" src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black"> <img alt="Terraform" src="https://img.shields.io/badge/Terraform-7B42BC?style=flat-square&logo=terraform&logoColor=white"> <img alt="Vault" src="https://img.shields.io/badge/Vault-FFEC6E?style=flat-square&logo=vault&logoColor=black"> |
| **Practices** | <img alt="pytest" src="https://img.shields.io/badge/pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white"> <img alt="CI/CD" src="https://img.shields.io/badge/CI%2FCD-2088FF?style=flat-square&logo=githubactions&logoColor=white"> <img alt="API contract design" src="https://img.shields.io/badge/API%20contract%20design-6BA539?style=flat-square&logo=swagger&logoColor=white"> <img alt="Technical writing" src="https://img.shields.io/badge/Technical%20writing-24292F?style=flat-square&logo=markdown&logoColor=white"> |

Relational modelling, indexing and migrations sit under the database badges; ETL pipeline
design and API contract design are the parts I think about most and the parts no logo
represents. I've also built infrastructure prototypes with Terraform, Vault and Docker Swarm
(database-per-tenant provisioning), though not yet running in production.

## Currently

Going deep on two things rather than broad on many: distributed data processing beyond
single-node pipelines, and cloud deployment with real infrastructure-as-code. The gap between
"I containerised it" and "I operate it" is the one worth closing next.

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
