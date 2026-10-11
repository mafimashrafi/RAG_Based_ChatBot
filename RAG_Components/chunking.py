from langchain_text_splitters import RecursiveCharacterTextSplitter

def get_chunks(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.create_documents([text])

    return chunks

if __name__ == '__main__':
    from RAG_Components.cap_loader import get_transcript
    text = get_transcript('https://www.youtube.com/watch?v=HAnw168huqA')
    chunk = get_chunks(text)
    print(chunk[0])