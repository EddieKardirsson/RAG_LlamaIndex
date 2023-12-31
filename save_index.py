from llama_index import VectorStoreIndex, SimpleDirectoryReader

# Load documents
documents = SimpleDirectoryReader("documents").load_data()

# Create index
index = VectorStoreIndex.from_documents(documents)

# Save index
index.storage_context.persist("./tmp")
