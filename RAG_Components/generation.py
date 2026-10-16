import os
from google import genai
from dotenv import load_dotenv
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
gemma_model = os.getenv("GEMMA_MODEL")

client = genai.Client(api_key=gemini_api_key)

def get_response(context):
    response = client.models.generate_content(
        model = gemma_model,
        content = context
    )

    return response.text