def chunk_text(
    text: str,
    chunk_size: int = 500,
    overlap: int = 75,
) -> list[str]:
    """
    Split text into overlapping word-based chunks.
    """

    words = text.split()

    chunks = []

    start = 0

    while start < len(words):

        end = min(start + chunk_size, len(words))

        chunk = " ".join(words[start:end])

        chunks.append(chunk)

        if end == len(words):
            break

        start = end - overlap

    return chunks
