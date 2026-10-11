from httpcore import URL
from langchain_community.chat_loaders import langsmith
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from module import video_id

ytt_api = YouTubeTranscriptApi()


def get_transcript(URL):
    vid = video_id.get_video_id(URL)
    try:
        fetched = ytt_api.fetch(video_id=vid, languages=['en'])
        transcript_list = fetched.to_raw_data()

        transcript = " ".join(chunk["text"] for chunk in transcript_list)

    except TranscriptsDisabled:
        print("No caption available for this video")
        return None

    return transcript

if __name__ == "__main__":
    URL = 'https://www.youtube.com/watch?v=HAnw168huqA'
    print(get_transcript(URL))