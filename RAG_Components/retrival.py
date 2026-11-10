from langchain_community.vectorstores import FAISS
from RAG_Components.embd_store import embed_and_store

def retriv_chunks(chunks, queries):
    vector_store = embed_and_store(chunks)
    retriever = vector_store.as_retriever(search_type = "similarity", search_kwargs = {"K": 4})

    retrieved_context = ""
    for k, v in queries.items():
        contexts = retriever.invoke(v)
        retrieved_context = "\n\n".join(doc.page_content for doc in contexts)
    return retrieved_context

if __name__ == "__main__":
    from RAG_Components.chunking import get_chunks
    from RAG_Components.cap_loader import get_transcript
    text = get_transcript('https://www.youtube.com/watch?v=HAnw168huqA')
    chunk = get_chunks(text)
    queries = {'User input': "Summarize the topic", "AI_query": "Explain the topic briefly"}
    context = retriv_chunks(chunk, queries)
    print(context)