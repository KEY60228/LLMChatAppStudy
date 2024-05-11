from langchain_community.document_loaders import GitLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings

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

text_splitter = CharacterTextSplitter(
  chunk_size=1000,
  chunk_overlap=0,
)

docs = text_splitter.split_documents(raw_docs)
print(len(docs))

embeddings = OpenAIEmbeddings()

query = "AWSのS3からデータを読み込むためのDocumentLoaderはありますか？"

verctor = embeddings.embed_query(query)
print(len(vector))
print(vector)
