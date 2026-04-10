from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pprint import pprint as print



def load_pdf(file_path: str):
    loader = PyPDFLoader(file_path)
    return loader.load()

def split_text(text: str, chunk_size: int = 100, chunk_overlap: int = 20):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    all_splits = text_splitter.split_documents(text)
    return all_splits



