from ingestion import split_text, load_pdf


file_path = "rag_agent/rag/knowledge/Glossário LangChain e Docker 2026.pdf"

load_docs = load_pdf(file_path)
text_splitted =split_text(load_docs)



