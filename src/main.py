from langchain_community.document_loaders import GitLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

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

context_docs = retriever.get_relevant_documents(query)
print(f"len = {len(context_docs)}")

first_doc = context_docs[0]
print(f"metadata = {first_doc.metadata}")
print(first_doc.page_content)
