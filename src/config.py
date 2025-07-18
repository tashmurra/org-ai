import os


PROJECT_ROOT_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# Default model for generating embeddings with the OpenAI API. This can be
# overridden with the ``OPENAI_EMBEDDING_MODEL`` environment variable if needed.
OPENAI_EMBEDDING_MODEL = os.getenv(
    "OPENAI_EMBEDDING_MODEL", "text-embedding-3-small"
)


SERP_API_KEY = os.getenv("SERP_API_KEY")
