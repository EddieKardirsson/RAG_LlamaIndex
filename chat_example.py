from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

# Load documents
documents = SimpleDirectoryReader("documents").load_data()

# Create index
index = VectorStoreIndex.from_documents(documents)

# Create chatbot
chat_engine = index.as_chat_engine(verbose=True, chat_mode="react")
chat_engine.chat_repl()
