from langchain_community.vectorstores import FAISS
from RAG_Components.embd_store import embed_and_store

def retriv_chunks(chunks, query):
    vector_store = embed_and_store(chunks)
    retriver = vector_store.as_retriever(search_type = "similarity", search_kwargs = {"K": 4})

    contexts = retriver.invoke(query)
    context = "\n\n".join(doc.page_content for doc in contexts)
    return context

if __name__ == "__main__":
    from RAG_Components.chunking import get_chunks
    from RAG_Components.cap_loader import get_transcript
    text = get_transcript('https://www.youtube.com/watch?v=HAnw168huqA')
    chunk = get_chunks(text)
    context = retriv_chunks(chunk, "Summarize the topic")
    print(context)