from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

embedding = OpenAIEmbeddings(model='text-embedding-3-small')

def embed_and_store(chunks):

    vector_store = FAISS.from_documents(chunks, embedding)

    return vector_store

if __name__ == '__main__':
    from RAG_Components.chunking import get_chunks
    from RAG_Components.cap_loader import get_transcript
    text = get_transcript('https://www.youtube.com/watch?v=HAnw168huqA')
    chunk = get_chunks(text)
    data = embed_and_store(chunk)
    print(data.index_to_docstore_id)