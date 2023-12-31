from llama_index import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("documents").load_data()
index = VectorStoreIndex.from_documents(documents)

chat_engine = index.as_chat_engine(verbose=True, chat_mode="react")
chat_engine.chat_repl()
