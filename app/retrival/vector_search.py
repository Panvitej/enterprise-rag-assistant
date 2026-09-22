from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams


class VectorStore:

    def __init__(
        self,
        url: str = "http://localhost:6333",
        collection_name: str = "enterprise_rag",
        vector_size: int = 384,
    ):
        self.client = QdrantClient(url=url)
        self.collection_name = collection_name

        collections = self.client.get_collections().collections

        collection_exists = any(
            collection.name == collection_name
            for collection in collections
        )

        if not collection_exists:
            self.client.create_collection(
                collection_name=collection_name,
                vectors_config=VectorParams(
                    size=vector_size,
                    distance=Distance.COSINE,
                ),
            )
