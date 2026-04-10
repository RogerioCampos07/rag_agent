from langchain_chroma import Chroma
from rag_agent.rag.llm_service import model

def create_vector_store(collection_name: str, embedding_function):
    return Chroma(collection_name=collection_name, embedding_function=embedding_function, client_settings={"model": model}) 