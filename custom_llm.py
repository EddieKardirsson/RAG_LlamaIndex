from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings, ServiceContext, set_global_service_context
from llama_index.llms.openai import OpenAI
import openai

openai.log = "debug"

# Define LLM
llm = OpenAI(model="gpt-3.5-turbo", temperature=0, max_tokens=1000)

# Configure service context

Settings.llm = llm

# service_context = ServiceContext.from_defaults(llm=llm)
# set_global_service_context(service_context)

# Load documents
documents = SimpleDirectoryReader("documents").load_data()

# Create index
index = VectorStoreIndex.from_documents(documents)

# Create chatbot
chat_engine = index.as_chat_engine(verbose=True, chat_mode="react")
chat_engine.chat_repl()
