import requests
from news_scrap import get_newslist
from newspaper import Article

def main():
    news_list=get_newslist(5)
    print_news(news_list)


def print_news(news_list):
    for i in range(len(news_list)):
        title=news_list[i]['title']
        link=shorten_url(news_list[i]['link'])
        summary=summarize_article(link)
        print(f"Title: {title}")
        print(f"Summary: {summary}")
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
    

def summarize_article(url):
    # Fetch article content
    article = Article(url)
    article.download()
    article.parse()

    # Generate summary
    article.nlp()
    summary = article.summary

    return summary

main()
