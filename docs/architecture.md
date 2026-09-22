# Architecture Notes

## Version 1

The first implementation intentionally has only four major stages:

1. Ingestion
2. Embedding
3. Retrieval
4. Generation

Do not add agents, rerankers, BM25, PostgreSQL or a frontend until the basic RAG path works.

## Retrieval

The target Phase 2 retrieval architecture is:

```text
User Query
   |
   +----> Vector Search
   |
   +----> BM25
            |
            v
       Result Fusion
            |
            v
         Reranker
            |
            v
        Top Context
```

## Generation

```text
Question + Retrieved Evidence
              |
              v
        Grounded Prompt
              |
              v
             LLM
              |
              v
       Answer + Citations
```

## Design Principle

Every retrieved chunk should retain enough metadata to identify its original source. At minimum:

- document ID
- filename
- page
- chunk ID
- section when available
