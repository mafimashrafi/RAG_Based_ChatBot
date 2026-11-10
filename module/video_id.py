import re

_ID_PATTERN = re.compile(r"(?:v=|youtu\.be/|shorts/|embed/|live/)([A-Za-z0-9_-]{11})")

def get_video_id(URL):
    URL = URL.strip()
    match = _ID_PATTERN.search(URL)
    if match:
        return match.group(1)
    if re.fullmatch(r"[A-Za-z0-9_-]{11}", URL):  # a bare id was pasted
        return URL
    raise ValueError(f"Could not find a YouTube video id in: {URL!r}")

if __name__ == '__main__':
    URL = 'https://youtu.be/0lJKucu6HJc?si=PN_9MFBGMvrms27O'
    print(get_video_id(URL))