import requests
from news_scrap import get_newslist

def main():
    news_list=get_newslist(5)
    print_news(news_list)


def print_news(news_list):
    for i in range(len(news_list)):
        title=news_list[i]['title']
        link=shorten_url(news_list[i]['link'])
        print(f"Title: {title}")
        print(f"Link: {link}")
        print("")



def shorten_url(long_url):
    api_url = 'https://tinyurl.com/api-create.php'
    params = {'url': long_url}
    response = requests.get(api_url, params=params)
    
    if response.status_code == 200:
        return response.text
    else:
        return None
    

