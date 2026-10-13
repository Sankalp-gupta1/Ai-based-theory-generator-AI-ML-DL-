# AI-Based Theory Generator — TheoryForge

An experimental NLP project for extracting useful evidence from source notes and creating theory-style drafts.

## Live demo

**https://theoryforge-sankalp.vercel.app/**

The repository contains two modes:

1. the original Python / transformer experiment,
2. a lightweight public TheoryForge demo.

## Live TheoryForge mode

The deployed app lets you:

1. paste source notes or load a text file,
2. enter a topic,
3. split the source into sentences,
4. rank sentences for relevance,
5. retrieve the strongest evidence,
6. assemble a structured theory-style draft,
7. inspect the evidence used in the draft.

The hosted mode is deterministic and extractive.

It does **not** pretend that a heavyweight GPT-2 model is running on a static server.

## Original experimental pipeline

The original project explores:

- PDF/text ingestion,
- text cleaning,
- sentence-transformer embeddings,
- semantic retrieval,
- GPT-2 text generation,
- PyTorch,
- Hugging Face Transformers.

That code remains in the repository for local experimentation.

## Run the live-style demo locally

```bash
cd web
python -m http.server 8000
```

Open:

```text
http://localhost:8000
```

## Run the Python work

Install the dependencies used by the scripts in `src/`.

Typical packages include:

- PyMuPDF
- PyTorch
- Transformers
- Sentence Transformers

Then run the ingestion, embedding and generation scripts from the source folders.

## Why the hosted mode is lighter

Transformer models can require large downloads and substantial memory.

The public demo is designed to:

- open quickly,
- need no secret key,
- show the retrieval workflow clearly,
- avoid pretending a large local model is running when it is not.

## Author

**Sankalp Gupta**

- GitHub: https://github.com/Sankalp-gupta1
- LinkedIn: https://www.linkedin.com/in/sankalp-gupta-rishi-8617302b0/


## Run the web demo locally

The hosted portfolio version is a static web demo, so it does not need an API key or database for local preview.

### Step 1 — clone the repository

```bash
git clone https://github.com/Sankalp-gupta1/Ai-based-theory-generator-AI-ML-DL-.git
cd Ai-based-theory-generator-AI-ML-DL-
```

### Step 2 — open the deployable web folder

```bash
cd web
```

### Step 3 — start a small local server

```bash
python -m http.server 8000
```

### Step 4 — open the app

```text
http://localhost:8000
```

Production demo: **https://theoryforge-sankalp.vercel.app/**

The original project files are kept in the repository. The `web/` version is the browser-friendly deployment made for easy review.
