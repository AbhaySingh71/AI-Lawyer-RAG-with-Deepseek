from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os

# Step 1: Upload & Load raw PDF(s)
import os

pdfs_directory = 'pdfs/'  # Folder to store PDFs

def upload_pdf(file):
    # Ensure the directory exists
    if not os.path.exists(pdfs_directory):
        os.makedirs(pdfs_directory)

    file_path = os.path.join(pdfs_directory, file.name)  # Construct file path
    with open(file_path, "wb") as f:
        f.write(file.getbuffer())
    
    return file_path  # Return the file path

def load_pdf(file_path):
    loader = PDFPlumberLoader(file_path)
    documents = loader.load()
    return documents

# Step 2: Create Chunks
def create_chunks(documents, file_name):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        add_start_index=True
    )
    text_chunks = text_splitter.split_documents(documents)
    
    # Add metadata (file name) to each chunk
    for chunk in text_chunks:
        chunk.metadata["source"] = file_name
    
    return text_chunks

# Step 3: Setup Embeddings Model
def get_embedding_model():
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embedding_model

embedding_model = get_embedding_model()

# Step 4: Index Documents with Metadata
FAISS_DB_PATH = "vectorstore/db_faiss"

def index_pdf(file_path):
    documents = load_pdf(file_path)
    file_name = file_path.split("/")[-1]  # Extract filename
    text_chunks = create_chunks(documents, file_name)
    faiss_db = FAISS.from_documents(text_chunks, embedding_model)
    faiss_db.save_local(FAISS_DB_PATH)
    return faiss_db

# Step 5: Retrieve Docs with Filtering
def retrieve_docs(query, file_name):
    faiss_db = FAISS.load_local(FAISS_DB_PATH, embedding_model, allow_dangerous_deserialization=True)
    retrieved_docs = faiss_db.similarity_search(query, k=5)
    
    filtered_docs = [doc for doc in retrieved_docs if doc.metadata.get("source") == file_name]

    return filtered_docs
