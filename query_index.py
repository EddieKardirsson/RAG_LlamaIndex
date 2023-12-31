from llama_index import StorageContext, load_index_from_storage

# rebuilding storage context
storage_context = StorageContext.from_defaults(persist_dir="./tmp")

# Load index
index = load_index_from_storage(storage_context)

query_engine = index.as_query_engine(verbose=True)

response = query_engine.query(
    "give me the link to the article with instructions on how to create a new teacher account"
)
print(response)
