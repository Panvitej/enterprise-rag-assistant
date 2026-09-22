from app.ingestion.chunker import chunk_text


def test_chunk_text_returns_chunks():
    text = " ".join(["word"] * 1200)
    chunks = chunk_text(text, chunk_size=500, overlap=75)

    assert len(chunks) > 1
    assert all(chunk for chunk in chunks)
