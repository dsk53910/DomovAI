# Domovai

PoC v0.1: index a Java backend repository, enable semantic search, and provide LLM answers over the codebase (RAG).

## Goals

- Quickly find code by semantic queries
- Get short explanations for components and symbols
- Keep the architecture clean: headless engine + clients

## Architecture

```
[ Java Repo ] -> [ Code Loader ] -> [ Chunker ] -> [ Embeddings ]
                             -> [ Vector Store ] -> [ Query Engine ] -> [ LLM ] -> [ CLI ]
```

## Project structure

```
.
├── docs/
├── src/
│   └── domovai/
│       ├── cli/
│       ├── core/
│       └── models/
├── pyproject.toml
└── uv.lock
```

## Quick start

### 1) Install dependencies

```
uv pip install -e .
```

### 2) Check the CLI

```
domovai -v
```

### 3) Example commands

```
domovai index ./my-java-repo
domovai search "transaction boundary"
domovai explain "PaymentService"
domovai stats
```

## Requirements

- Python >= 3.11
- uv

## Status

PoC v0.1: under development.

## License

TBD
