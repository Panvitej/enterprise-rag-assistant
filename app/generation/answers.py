def build_prompt(question: str, contexts: list[dict]) -> str:
    """Build a grounded prompt for the LLM."""
    evidence = []

    for index, item in enumerate(contexts, start=1):
        evidence.append(
            f"[Source {index}] "
            f"{item.get('source', 'unknown')} "
            f"page {item.get('page', 'unknown')}\n"
            f"{item.get('text', '')}"
        )

    joined = "\n\n".join(evidence)

    return f"""You are a document-grounded research assistant.

Answer the user's question using ONLY the evidence below.

Rules:
- Do not invent facts.
- If the evidence is insufficient, say so.
- Cite the relevant source and page for important claims.

Evidence:
{joined}

Question:
{question}
"""
