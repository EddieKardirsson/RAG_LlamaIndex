from llama_index import VectorStoreIndex, SimpleDirectoryReader

# Load documents
docs1 = SimpleDirectoryReader(input_files=["./docs1/example - exported knowledge base.csv"]).load_data()
docs2 = SimpleDirectoryReader("docs2").load_data()

docs1[0].metadata["category"] = "customer support"

for doc in docs2:
    doc.metadata["category"] = "marketing"

all_docs = docs1 + docs2

# Create index
index = VectorStoreIndex.from_documents(all_docs)

# Save index
index.storage_context.persist("./tmp")

# Create chatbot
chat_engine = index.as_chat_engine(verbose=True, chat_mode="react")
chat_engine.chat_repl()
