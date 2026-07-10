import os

from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

from rag.embeddings import get_embeddings


PDF_DIRECTORY = "data/pdfs"
CHROMA_DIRECTORY = "vectordb"


def ingest_documents():
    print("Loading PDFs...")

    loader = PyPDFDirectoryLoader(PDF_DIRECTORY)
    documents = loader.load()

    print(f"Loaded {len(documents)} pages.")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )

    chunks = splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks.")

    embeddings = get_embeddings()

    print("Creating Chroma database...")

    Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DIRECTORY,
    )

    print("Knowledge Base Created Successfully!")


if __name__ == "__main__":
    ingest_documents()