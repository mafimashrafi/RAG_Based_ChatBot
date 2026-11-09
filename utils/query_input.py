""" We simply take input fomr the user here.
A YouTube video URL and their question"""

def get_query():
    """
    :rtype: tuple[str, str]
    """
    url = input('Enter YouTube Video URL: ')
    query = input("Enter your question about the content of the URL: ")

    return url, query

if __name__ == '__main__':
    url, query = get_query()
    print(url)
    print(query)