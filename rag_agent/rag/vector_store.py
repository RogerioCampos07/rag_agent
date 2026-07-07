from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from rag_agent.settings import settings
from ingestion import load_pdf, split_my_documents


file_path = "rag_agent/rag/knowledge/Glossário LangChain e Docker 2026.pdf"
file_path2 = "rag_agent/rag/knowledge/entrega_cervejas_sob_demanda.pdf"

load_docs = load_pdf(file_path)
all_splits = split_my_documents(load_docs)

model_embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001",
                                          google_api_key=settings.GOOGLE_API_KEY,
                                          max_retries=3,
                                          version="v1")


vector_db = Chroma.from_documents(
    documents=all_splits, 
    embedding=model_embeddings,
    persist_directory="./meu_chroma_db"  
)


query = "qual o assunto do documento?"
docs_relacionados = vector_db.similarity_search(query, k=3)

# Exibindo o resultado e os metadados (importante para saber a página!)
for i, doc in enumerate(docs_relacionados):
    print(f"\n--- Trecho {i+1} (Página: {doc.metadata.get('page')}) ---")
    print(doc.page_content[:200] + "...")
