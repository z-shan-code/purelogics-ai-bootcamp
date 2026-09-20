from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

embedding_model_bge = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")

vector_store = Chroma(
    collection_name='crime_and_punishment_bge',
    embedding_function=embedding_model_bge,
    persist_directory='./chroma_db'
)

print("Loaded vector store with", vector_store._collection.count(), "vectors")