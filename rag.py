import os
import chromadb
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def setup_vector_store(
    pdf_path: str = "data/your_file.pdf", db_path: str = "./chroma_db"
):
    """Loads a PDF, splits it into chunks, and persists them into ChromaDB."""
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF not found at path: {pdf_path}")

    # Load & split document
    loader = PyPDFLoader(pdf_path)
    data = loader.load()

    text_splitter = RecursiveCharacterTextSplitter()
    all_splits = text_splitter.split_documents(data)

    # Initialize Chroma client
    client = chromadb.PersistentClient(path=db_path)

    # Get or create collection to prevent errors on re-runs
    collection = client.get_or_create_collection(name="Resume")

    # Add items if collection is empty
    if collection.count() == 0:
        documents_text = [doc.page_content for doc in all_splits]
        ids = [f"id_{i}" for i in range(len(all_splits))]
        collection.add(documents=documents_text, ids=ids)

    return collection


def query_vector_store(collection, query: str, n_results: int = 3) -> str:
    """Queries ChromaDB and returns joined document strings."""
    results = collection.query(query_texts=[query], n_results=n_results)
    retrieved_docs = results["documents"][0]
    return "\n".join(retrieved_docs)
