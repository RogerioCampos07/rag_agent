from rag_agent.settings import settings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from ingestion import split_text, load_pdf


file_path = "rag_agent/rag/knowledge/Glossário LangChain e Docker 2026.pdf"

load_docs = load_pdf(file_path)
text_splitted =split_text(load_docs)

model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001", google_api_key=settings.GOOGLE_API_KEY)

for text in text_splitted:
    n = 0
    embedding = model.embed_query(text)
    print(f"Vector {n}: {embedding[:10]}")

""" def get_model_embeddings(input_text: str):
    model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001", google_api_key=settings.GOOGLE_API_KEY)
    response = model.embed_query(input_text)
    return response
     """


