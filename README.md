# ATLAS — Multilingual Customer Intelligence

> **Production-minded NLP / MLOps system for multilingual telecom support triage.**

ATLAS is an end-to-end research and engineering project for classifying Moroccan telecom support messages across Arabic script, Arabizi, and mixed-script text.

It combines **data contracts, reproducible evaluation, classical NLP, neural models, multilingual Transformers, calibration, uncertainty analysis, FastAPI serving, monitoring, Docker, and automated tests**.

## What ATLAS does

**Message → validation → preprocessing → intent model → confidence / abstention → API → telemetry → monitoring**

The current benchmark compares three model generations on the same 75-label source-intent task:

| Model | Test macro F1 | Warm batch-one p95 | Peak RSS |
|---|---:|---:|---:|
| TF-IDF + Logistic Regression | **0.8522** | **1.31 ms** | **193 MiB** |
| BiLSTM | 0.6608 | 2.00 ms | 718 MiB |
| Frozen MiniLM + Logistic Regression | 0.4509 | 36.17 ms | 1.09 GiB |

The results are deliberately reported with their limitations: the benchmark is based on a synthetic Darija telecom source dataset, the Transformer encoder is frozen, and no model is presented as production-approved.

## Engineering highlights

- Versioned annotation, prediction, and dataset contracts
- Unicode-aware validation and script/source analysis
- Reproducible train/validation/test splits
- TF-IDF + Logistic Regression baseline
- TensorFlow BiLSTM experiment
- Frozen multilingual MiniLM + supervised head
- Calibration and paired statistical comparison
- Conditional stratified bootstrap confidence intervals
- Model/resource benchmarking in fresh processes
- FastAPI inference with health/readiness endpoints
- Input validation and abstention behavior
- Prometheus metrics and persistent monitoring
- Local MLflow experiment tracking
- Docker / Compose deployment configuration
- Automated Python and dashboard tests
- Model cards, evaluation protocol, source review, and experiment history

## Architecture

```text
                     ┌─────────────────────┐
                     │   Telecom message   │
                     └──────────┬──────────┘
                                │
                       validation / contracts
                                │
                                ▼
                     ┌─────────────────────┐
                     │   preprocessing     │
                     └──────────┬──────────┘
                                │
              ┌─────────────────┼─────────────────┐
              ▼                 ▼                 ▼
        TF-IDF + LR          BiLSTM        MiniLM + LR
              └─────────────────┼─────────────────┘
                                ▼
                     confidence / abstention
                                │
                                ▼
                    ┌──────────────────────┐
                    │     FastAPI API       │
                    └──────────┬───────────┘
                               │
                 ┌─────────────┴─────────────┐
                 ▼                           ▼
           prediction logs              Prometheus
                                             │
                                             ▼
                                      monitoring store
                                             │
                                             ▼
                                         dashboard
```

## Quick start

Python 3.11/3.12 and [uv](https://docs.astral.sh/uv/) are recommended.

```bash
uv sync --locked --group serving
uv run --locked --group serving uvicorn api.main:app --host 127.0.0.1 --port 8000 --workers 1
```

Then open:

- `/docs` — interactive OpenAPI documentation
- `/health` — process health
- `/ready` — model readiness
- `/model` — loaded model metadata
- `/metrics` — Prometheus metrics
- `/dashboard` — monitoring dashboard

Docker:

```bash
docker compose up --build
```

## Reproducibility

The project keeps training, evaluation, serving, and monitoring logic separate. Experiments record dataset/source hashes, split identities, configuration, versions, and generated artifacts.

The repository intentionally excludes raw datasets, local environments, MLflow state, caches, and other machine-local artifacts.

## Repository structure

```text
api/          FastAPI entrypoint
configs/      versioned experiment and serving configuration
data/         manifests and annotation workflows
docs/         evaluation, governance, model cards, runbooks
reports/      measured experiment outputs
scripts/      reproducible CLI workflows
src/atlas/    reusable application and ML code
tests/        unit, integration, serving, and monitoring tests
training/     model-training entrypoints
```

## Evaluation philosophy

ATLAS treats model quality as more than a single accuracy number.

The evaluation stack includes:

- macro F1 and per-class analysis
- script/source breakdowns
- calibration diagnostics
- paired model comparison
- stratified bootstrap uncertainty
- inference latency and memory measurements
- explicit dataset/evidence limitations
- independent-review gates before any production promotion

**No model is promoted automatically.**

## Documentation

- [Architecture](ARCHITECTURE.md)
- [Evaluation protocol](docs/evaluation_protocol.md)
- [API runbook](docs/api/README.md)
- [Monitoring runbook](docs/monitoring/README.md)
- [Transformer reproduction](docs/transformer_reproduction.md)
- [Model cards](docs/model_cards/)
- [Project start guide](START_HERE.md)

## Status

**Research / engineering prototype — actively developed.**

The repository is designed to demonstrate how an NLP model can be taken beyond a notebook into a reproducible, testable, observable serving system while keeping experimental claims and production claims clearly separated.
