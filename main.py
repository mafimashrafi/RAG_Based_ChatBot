from RAG_Components.cap_loader import get_transcript
from RAG_Components.chunking import get_chunks
from RAG_Components.retrival import retriv_chunks
from RAG_Components.generation import get_response
from RAG_Components.augmentation import get_final_prompt

from middleware.query_multiplier import get_queries
from utils.query_input import get_query

url, query = get_query()

all_query_dict = get_queries(query)
transcript = get_transcript(url)
chunks = get_chunks(transcript)
context = retriv_chunks(chunks, all_query_dict)
prompt = get_final_prompt(context, query)
resp = get_response(prompt)

print(resp)