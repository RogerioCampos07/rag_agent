from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pprint import pprint as print

file_path = "knowledge/entrega_cervejas_sob_demanda.pdf"

def load_pdf(file_path: str):
    loader = PyPDFLoader(file_path)
    return loader.load()

def load_pdf_metadata(file_path: str, page_number: int = 0):
    loader = PyPDFLoader(file_path)
    doc = loader.load()
    if page_number < len(doc):
        return doc[page_number].metadata
    else:
        raise IndexError("Page number out of range")


def split_text(text: str, chunk_size: int = 100, chunk_overlap: int = 0):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return text_splitter.split_text(text)


