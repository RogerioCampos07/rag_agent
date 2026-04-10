from vector_store import vector_db



query = "qual o assunto do documento?"
docs_relacionados = vector_db.similarity_search(query, k=3)


for i, doc in enumerate(docs_relacionados):
    print(f"\n--- Trecho {i+1} (Página: {doc.metadata.get('page')}) ---")
    print(doc.page_content[:200] + "...")