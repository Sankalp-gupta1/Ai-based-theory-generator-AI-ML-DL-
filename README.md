# AI-Based Theory Generator

An experimental NLP project for extracting knowledge from source documents, retrieving relevant passages, and creating theory-style drafts.

## Live no-key demo

**https://theoryforge-sankalp.vercel.app/**

The repository includes two modes:

### Original experimental pipeline

- PDF/text ingestion
- text preprocessing
- sentence-transformer embeddings
- semantic retrieval
- GPT-2 theory generation
- PyTorch / Hugging Face

### Hosted TheoryForge mode

The `web/` app is intentionally lightweight and transparent.

It:
- accepts pasted notes or a text file,
- scores source sentences against a topic,
- retrieves the most relevant evidence,
- assembles a structured draft,
- shows the retrieved source evidence,
- needs no private API key.

The hosted mode is extractive/deterministic and does **not** pretend to run the heavier GPT-2 pipeline in Vercel.

## Run the hosted version locally

```bash
cd web
python -m http.server 8000
```

Open `http://localhost:8000`.

## Run the original Python work

Install the project dependencies used by the scripts in `src/` and run the ingestion / embedding / inference stages from there.

## Author

Sankalp Gupta  
GitHub: https://github.com/Sankalp-gupta1
