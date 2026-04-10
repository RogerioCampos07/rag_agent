from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pprint import pprint as print



def load_pdf(file_path: str):
    loader = PyMuPDFLoader(file_path)
    return loader.load()

def split_my_documents(documents, chunk_size: int = 1000, chunk_overlap: int = 200):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, 
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", " ", ""] # Garante a hierarquia de quebra
    )
    all_splits = text_splitter.split_documents(documents)
    return all_splits
    
    



