from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    openai_api_key: str = ""
    qdrant_url: str = "http://localhost:6333"
    qdrant_collection: str = "enterprise_rag"
    llm_model: str = ""
    embedding_model: str = "BAAI/bge-small-en-v1.5"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()
