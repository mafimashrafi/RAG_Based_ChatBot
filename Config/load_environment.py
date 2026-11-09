import os
from dotenv import load_dotenv


def get_keys():
    """
    Load environment variables
    :return: tuple[Key: str, Model: str]
    """
    load_dotenv()

    gemini_api_key = os.getenv("GEMINI_API_KEY")
    gemini_model = os.getenv("GEMINI_MODEL")

    return gemini_api_key, gemini_model

if __name__ == "__main__":
    gemini_api_key, gemma_model = get_keys()
    print(gemini_api_key)
    print(gemma_model)