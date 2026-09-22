import fitz


def load_pdf(file_path: str) -> list[dict]:
    """
    Extract text from a PDF while keeping page numbers.
    """

    document = fitz.open(file_path)

    pages = []

    for page_number, page in enumerate(document, start=1):
        text = page.get_text("text").strip()

        if text:
            pages.append(
                {
                    "text": text,
                    "page": page_number,
                    "source": file_path,
                }
            )

    document.close()

    return pages
