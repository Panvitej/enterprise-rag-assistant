def chunk_text(text: str, chunk_size: int = 500, overlap: int = 75) -> list[str]:
    """Simple word-based chunker for the first project version.

    Later versions can use a token-aware or semantic chunker.
    """
    words = text.split()
    chunks = []

    start = 0
    while start < len(words): 
        end = min(start + chunk_size, len(words))
        chunks.append(" ".join(words[start:end]))

        if end == len(words):
            break

        start = max(end - overlap, start + 1)

    return chunks
