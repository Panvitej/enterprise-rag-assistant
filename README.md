# Enterprise Research & Decision Assistant

A beginner-friendly RAG (Retrieval-Augmented Generation) project built as a first serious AI/LLM portfolio project.

The goal is to build a system that can read company reports and technical documents, retrieve relevant information, and answer questions with source citations instead of relying only on the LLM's internal knowledge.


## Project Goal

Build a web application where a user can:

1. Upload PDF documents.
2. Extract and clean their text.
3. Split documents into smaller chunks.
4. Generate embeddings for those chunks.
5. Store embeddings in a vector database.
6. Ask questions about the uploaded documents.
7. Retrieve the most relevant chunks.
8. Give those chunks to an LLM.
9. Return an answer with document/page citations.
10. Evaluate whether retrieval and answers are actually good.

## Initial Tech Stack

- Python 3.11+
- FastAPI — backend API
- LlamaIndex — RAG orchestration
- Qdrant — vector database
- PostgreSQL — application metadata
- PyMuPDF — PDF text extraction
- Sentence Transformers / BGE-style embedding model — embeddings
- BM25 — keyword retrieval (Phase 2)
- Reranker — Phase 2
- OpenAI-compatible LLM API — generation
- Langfuse — observability/evaluation (Phase 3)
- Docker — deployment (Phase 4)
- React/Next.js — frontend (Phase 4)

## Architecture

### Version 1

```text
PDF
 ↓
Text extraction
 ↓
Chunking
 ↓
Embeddings
 ↓
Qdrant
 ↓
User question
 ↓
Vector retrieval
 ↓
LLM
 ↓
Answer + sources
```

### Final target architecture

```text
                         ┌──────────────┐
                         │    User      │
                         └──────┬───────┘
                                │
                         ┌──────▼───────┐
                         │ React / Web  │
                         └──────┬───────┘
                                │
                         ┌──────▼───────┐
                         │   FastAPI    │
                         └───┬──────┬───┘
                             │      │
                  upload     │      │ question
                             │      │
                    ┌────────▼─┐  ┌─▼────────────┐
                    │ Ingestion│  │Query Process │
                    └────┬─────┘  └──────┬───────┘
                         │               │
                    ┌────▼─────┐    ┌────▼────────┐
                    │ Chunking  │    │ Hybrid      │
                    │ + Metadata│    │ Retrieval   │
                    └────┬─────┘    └────┬────────┘
                         │               │
                    ┌────▼─────┐    ┌────▼────────┐
                    │ Embedding│    │  Reranker   │
                    └────┬─────┘    └────┬────────┘
                         │               │
                    ┌────▼─────┐         │
                    │  Qdrant  │◄────────┘
                    └──────────┘
                                        │
                                 ┌──────▼──────┐
                                 │ Context     │
                                 │ Builder     │
                                 └──────┬──────┘
                                        │
                                 ┌──────▼──────┐
                                 │     LLM     │
                                 └──────┬──────┘
                                        │
                                 ┌──────▼──────┐
                                 │ Answer +    │
                                 │ Citations   │
                                 └─────────────┘

                   Langfuse observes the pipeline
```

## Folder Structure

```text
enterprise-rag-project/
│
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── docker-compose.yml
│
├── app/
│   ├── main.py
│   ├── config.py
│   │
│   ├── ingestion/
│   │   ├── loader.py
│   │   ├── chunker.py
│   │   └── embeddings.py
│   │
│   ├── retrieval/
│   │   ├── vector_search.py
│   │   ├── bm25_search.py
│   │   └── reranker.py
│   │
│   ├── generation/
│   │   └── answer.py
│   │
│   └── evaluation/
│       └── evaluate.py
│
├── data/
│   ├── documents/
│   └── evaluation/
│       └── questions.json
│
├── tests/
│   ├── test_chunking.py
│   └── test_api.py
│
└── docs/
    ├── architecture.md
    └── experiments.md
```

## Development Roadmap

### Phase 1 — Make RAG work

- [ ] Set up Python project
- [ ] Load PDFs
- [ ] Extract text
- [ ] Add page metadata
- [ ] Chunk text
- [ ] Generate embeddings
- [ ] Store vectors in Qdrant
- [ ] Implement similarity search
- [ ] Connect an LLM
- [ ] Return an answer
- [ ] Return page citations

### Phase 2 — Improve retrieval

- [ ] Add BM25
- [ ] Combine vector + keyword retrieval
- [ ] Add metadata filters
- [ ] Add reranking
- [ ] Compare retrieval methods

### Phase 3 — Evaluation

- [ ] Create 50+ test questions
- [ ] Measure retrieval hit rate
- [ ] Measure MRR
- [ ] Measure answer relevance
- [ ] Measure faithfulness
- [ ] Measure citation correctness
- [ ] Track latency and token usage

### Phase 4 — Productize

- [ ] Build FastAPI endpoints
- [ ] Add PostgreSQL
- [ ] Build React/Next.js UI
- [ ] Add document management
- [ ] Add conversation history
- [ ] Add Langfuse tracing
- [ ] Dockerize the application

### Phase 5 — Advanced features

- [ ] Query rewriting
- [ ] Local LLM with Ollama
- [ ] Compare API vs local model
- [ ] Add agentic research mode
- [ ] Add calculator/tool use
- [ ] Add automated regression tests for RAG quality

## Why This Project?

A basic "chat with PDF" application is a common beginner project.

This project is intentionally different in its learning goals:

- It treats retrieval as an engineering problem.
- It measures whether retrieval works.
- It measures whether generated answers are supported.
- It keeps source metadata so answers can be traced back to documents.
- It compares different RAG strategies instead of assuming one strategy is best.
- It grows from a simple implementation into a production-style system.

## Example Questions

After adding company reports, the system should support questions such as:

- What was the company's revenue in 2025?
- What caused the revenue change?
- What were the largest operating expenses?
- Compare revenue between two years.
- Which document supports this answer?
- What information is missing from the documents?

## Important Design Rule

The system should not invent an answer when the documents do not contain enough evidence.

Expected behavior:

```text
Question
   ↓
Retrieve evidence
   ↓
Enough evidence?
   ├── YES → Generate answer + citations
   └── NO  → Say that the available documents
             do not contain enough information
```

## First Milestone

Do not start by building the complete architecture.

The first milestone is only:

```text
PDF → chunks → embeddings → Qdrant → retrieval → LLM → answer
```

Once that works, add one feature at a time.

## Learning Topics

While building this project, learn these concepts in order:

1. Python fundamentals
2. REST APIs
3. FastAPI
4. JSON and HTTP
5. PDF/text processing
6. Embeddings
7. Vector databases
8. Similarity search
9. RAG
10. Prompt design
11. LLM APIs
12. BM25
13. Reranking
14. RAG evaluation
15. Docker
16. PostgreSQL
17. Basic cloud deployment


Only add performance numbers after measuring them yourself.

## Project Status

**Current status:** Planning / Phase 1

This README is the project blueprint. Implementation should be committed incrementally so the GitHub history shows the development process.
