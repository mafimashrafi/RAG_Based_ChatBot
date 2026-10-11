import re

def get_video_id(URL):

    vid = re.split(r'[/?=]', URL)[-1]

    return vid

if __name__ == '__main__':
    URL = 'https://www.youtube.com/watch?v=vF6dV6H8QFA'
    print(get_video_id(URL))