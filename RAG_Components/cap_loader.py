from httpcore import URL
from langchain_community.chat_loaders import langsmith
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from module import video_id

ytt_api = YouTubeTranscriptApi()


def get_transcript(URL):
    vid = video_id.get_video_id(URL)
    try:
        # Fix: Fetch the transcript list instance from the instantiated object
        transcript_list = ytt_api.list(vid)

        # Select the preferred manual or auto track (falls back to English defaults)
        fetched = transcript_list.find_transcript(['en'])

        # Extract the structured text blocks mapping
        transcript_data = fetched.fetch()

        # Combine the text segments into a single paragraph
        transcript = " ".join(chunk.text for chunk in transcript_data)
        return transcript

    except TranscriptsDisabled:
        print("No caption available for this video")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

if __name__ == "__main__":
    URL = 'https://www.youtube.com/watch?v=HAnw168huqA'
    print(get_transcript(URL))