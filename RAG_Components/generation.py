from Config.load_environment import get_keys
from google import genai


gemini_api_key, gemini_model = get_keys()

client = genai.Client(api_key=gemini_api_key)

def get_response(context):
    response = client.models.generate_content(
        model = gemini_model,
        content = context
    )

    return response.text