"""" Here we call another model and provide the query.
All that model does is generate few more queries.
But all the question asks for the same thing.

Basic design is: Import the query ->
                send it to LLM ->
                gen more queries ->
                save them for retrival.
"""
import sys
from pathlib import Path

from utils.query_input import get_query
from Config.load_environment import get_keys
from google import genai

PROMPT_PATH = Path(__file__).resolve().parent.parent/ "Config" / "query_multi_pmpt.md"
SYSTEM_PROMPT = PROMPT_PATH.read_text(encoding="utf-8")

api_key, model = get_keys()
client = genai.Client(api_key=api_key)


Prompts =""
Queries = {}

def get_queries(query):
    Prompts = f"System: {SYSTEM_PROMPT}\n\n Query: {query}"
    Queries = {'User input': query}

    response = client.models.generate_content(
        model=model,
        contents = Prompts
    )
    Queries['AI_query'] = response.text

    return Queries


if __name__ == "__main__":
    print(Queries)