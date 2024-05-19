from langchain_community.document_loaders import GitLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

def file_filter(file_path):
  return file_path.endswith(".mdx")

loader = GitLoader(
  clone_url="https://github.com/langchain-ai/langchain",
  repo_path="./langchain",
  branch="master",
  file_filter=file_filter,
)

print("Loading documents...")

raw_docs = loader.load()
print(len(raw_docs))

print("=========================================")

text_splitter = CharacterTextSplitter(
  chunk_size=1000,
  chunk_overlap=0,
)

docs = text_splitter.split_documents(raw_docs)
print(len(docs))

print("=========================================")

embeddings = OpenAIEmbeddings()
db = Chroma.from_documents(docs, embeddings)
retriever = db.as_retriever()

query = "AWSのS3からデータを読み込むためのDocumentLoaderはありますか？"

chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
qa_chain = RetrievalQA.from_chain_type(llm=chat, chain_type="stuff", retriever=retriever)

result = qa_chain.run(query)
print(result)
