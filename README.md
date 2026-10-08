# AI-Based PDF Theory Generator

An experimental NLP pipeline for **extracting knowledge from PDFs, cleaning academic text, generating semantic embeddings, retrieving relevant passages, and generating theory-style text with a transformer model**.

## Overview

The repository explores multiple stages of an academic text-processing workflow:

```text
PDF documents
     │
     ▼
Text extraction
     │
     ▼
Text cleaning / paragraph structuring
     │
     ▼
Sentence embeddings
     │
     ├── Semantic retrieval
     │
     └── Saved embedding/model artifacts
     │
     ▼
Transformer-based theory generation
```

## Core Components

### PDF Ingestion

`src/ingest.py.py` uses **PyMuPDF** to extract text from PDFs in the `data/` directory and combine the content into a text file.

### Preprocessing

`src/preprocess.py` cleans spacing and restructures extracted text into paragraph-like chunks.

### Semantic Embeddings

`src/embed.py` uses `all-MiniLM-L6-v2` from Sentence Transformers to create paragraph embeddings and stores the embedding output for later retrieval.

### Semantic Retrieval

`src/infer.py` embeds a user question, computes cosine similarity against document paragraphs, and returns the most relevant passages.

### Theory Generation

`src/theory_genrator.py` uses GPT-2 through Hugging Face Transformers to generate theory-style text from a topic prompt.

## Tech Stack

- Python
- PyMuPDF
- PyTorch
- Hugging Face Transformers
- Sentence Transformers
- GPT-2
- NumPy / semantic similarity utilities

## Repository Structure

```text
Ai-based-theory-generator-AI-ML-DL-/
├── data/
├── docs/
├── model/
├── src/
│   ├── ingest.py.py
│   ├── preprocess.py
│   ├── embed.py
│   ├── infer.py
│   ├── theory_genrator.py
│   └── simulate.py
├── static/
├── templates/
├── time_machine_simulator.py
├── time_machine_simulator1.py
└── README.md
```

## Installation

Create a virtual environment and install the main dependencies:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS / Linux:

```bash
source .venv/bin/activate
```

Install packages:

```bash
pip install pymupdf torch transformers sentence-transformers
```

## Example Pipeline

Place one or more PDF files inside `data/`.

### 1. Extract PDF text

```bash
python src/ingest.py.py
```

### 2. Clean extracted text

```bash
python src/preprocess.py
```

### 3. Generate semantic embeddings

```bash
python src/embed.py
```

### 4. Ask semantic questions

```bash
python src/infer.py
```

### 5. Generate theory from a topic

```bash
python src/theory_genrator.py
```

## Notes

This repository is an experimental educational prototype. GPT-2 and semantic retrieval can produce incomplete or incorrect outputs, so generated academic content should be verified before use.

## Author

**Sankalp Gupta**

GitHub: https://github.com/Sankalp-gupta1
