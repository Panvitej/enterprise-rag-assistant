from pathlib import Path
import fitz


def load_pdf(path: str) -> list[dict]:
    """Extract text while preserving page-level metadata."""
    document = fitz.open(path)
    pages = []

    for page_number, page in enumerate(document, start=1):
        text = page.get_text("text").strip()

        if text:
            pages.append(
                {
                    "text": text,
                    "page": page_number,
                    "source": Path(path).name,
                }
            )

    document.close()
    return pages
