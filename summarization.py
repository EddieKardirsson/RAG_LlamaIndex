from llama_index import VectorStoreIndex, SimpleDirectoryReader

# Load documents
docs = SimpleDirectoryReader(input_files=["./docs1/example - exported knowledge base.csv"]).load_data()
docs[0].metadata["category"] = "customer support"

# Create index
index = VectorStoreIndex.from_documents(docs)

# Save index
index.storage_context.persist("./tmp")

# Query
query_engine = index.as_query_engine(verbose=True, response_mode="tree_summarize", similarity_top_k=6)
response = query_engine.query("summarize our customer support content")
print("\n", response)

print("\n", response.get_formatted_sources())

# print(response.source_nodes)
