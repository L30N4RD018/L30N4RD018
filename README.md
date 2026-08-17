<div align="center">

# Leonardo Mendoza

**Backend & Data Engineer** · Cartagena, Colombia

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/leonardomendoza-dev)
[![Email](https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:leonardomendoza2003@gmail.com)

🇬🇧 English · [🇪🇸 Español](README.es.md)

</div>

---

I build backend services and data pipelines that deal with messy, real-world sources:
government registries with no API, scanned regulatory documents, and legacy file formats that
were never meant to be parsed. Most of that work is in the Colombian public-health sector.

Most of my professional code lives in private organisational repositories, so what follows
describes what I built rather than linking to it. The public repositories on this profile are
academic and personal work.

## What I've built

**Candidate assessment platform — in production**
Designed and built the backend (FastAPI, PostgreSQL, Redis, S3-compatible storage) behind the
platform that runs my organisation's selection processes, which has carried 20+ real selection
rounds across two generations. The interesting parts: exam lifecycles modelled as state
machines, so invalid transitions fail in the domain instead of leaking into endpoints; an
Outbox table driving asynchronous notifications; and remote proctoring with chunked video
upload plus a WebSocket channel for attempt timers, designed so a dropped connection never
costs a candidate their progress. I rebuilt the data model for the second generation while the
first stayed live and untouched for audit.

**Geospatial viewer for a regional healthcare network**
A routing engine over a road network of 1.4 million nodes, returning referral routes between
healthcare facilities in under half a second. It consolidates 6.8 GB of national cartography
and OpenStreetMap extracts into a single queryable model, validated against a JSON Schema
contract so malformed data fails at ingestion rather than in the viewer. Built offline-first:
the whole thing runs on a disconnected institutional laptop from a single `uvicorn` command —
no Docker, no network, no Node runtime — with an automated check that the bundled front end
makes zero external requests.

**National health registry crawler**
Colombia's public healthcare provider registry has no API. I automated its extraction with
Playwright, collecting all 932 public hospitals in the country along with their facilities,
services and installed capacity. It persists progress so an interrupted run resumes instead of
restarting, partitions work across parallel workers, and can reprocess only the records that
failed.

**Regulatory ETL for healthcare billing**
Colombian health billing moved from a flat-file standard written in 2000 to the hierarchical
JSON format required by 2023 regulation. I built the ETL for that migration, isolating readers,
transformation and validated output so an amendment to the regulation touches a single layer.
Correctness is enforced by Pydantic schemas against official government reference tables, not
by convention.

**Document understanding for legal PDFs**
A pipeline that converts scanned resolutions and regulatory documents into machine-readable
form, preserving the original reading order and table structure. The decision that made it
work: detect page geometry with OpenCV *before* invoking the OCR model, so it only ever sees
pre-identified text regions and individual table cells rather than whole pages. PDFs with
embedded text skip OCR entirely.

## Research

**[VACS: A Modular Software System for Vehicular Access Control](https://doi.org/10.1007/978-3-032-08206-0_19)**
— Alvarino, Taboada, **Mendoza**, Montes & Martinez-Santos. Springer, *Communications in
Computer and Information Science* (WEA 2025), October 2025.
[`10.1007/978-3-032-08206-0_19`](https://doi.org/10.1007/978-3-032-08206-0_19) ·
[source code](https://github.com/ZenoexORG/vacs-backend)

A modular NestJS backend organised around isolated domain modules, with access modelled as
enforceable rules and third-party plate recognition as the event source. Capstone project, and
the code is public.

## Tools I actually use

**Languages** Python · TypeScript · JavaScript · SQL · R

**Backend** FastAPI · NestJS · REST API design · OpenAPI · Pydantic · SQLAlchemy · Alembic

**Data** ETL pipeline design · Playwright · pandas · NumPy · GeoPandas · Shapely · NetworkX

**Databases** PostgreSQL · SQLite · relational modelling · indexing · migrations

**Infrastructure** Docker · Docker Compose · Nginx · Redis · GitHub Actions · Linux

**Practices** Automated testing (pytest) · CI/CD · API contract design · technical writing

I've also built infrastructure prototypes with Terraform, Vault and Docker Swarm
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
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/L30N4RD018/L30N4RD018/output/snake-dark.svg">
  <img src="https://raw.githubusercontent.com/L30N4RD018/L30N4RD018/output/snake.svg" alt="Contribution snake">
</picture>

</div>
