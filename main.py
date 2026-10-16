from RAG_Components.cap_loader import get_transcript
from RAG_Components.chunking import get_chunks
from RAG_Components.retrival import retriv_chunks
from RAG_Components.generation import get_response
from RAG_Components.augmentation import get_final_prompt

url = input('Enter URL: ')
query = input("Enter your question about the content of the URL: ")

transcript = get_transcript(url)
chunks = get_chunks(transcript)
context = retriv_chunks(chunks, query)
prompt = get_final_prompt(context, query)
resp = get_response(prompt)

print(resp)