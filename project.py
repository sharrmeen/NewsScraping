import requests
import nltk
from news_scrap import get_newslist
from newspaper import Article

def main():
    news_list=get_newslist(5)
    print_news(news_list)
    

def print_news(news_list):
    print("")
    for i in range(len(news_list)):
        title=news_list[i]['title']
        link=news_list[i]['link']
        summary=summarize_article(link)


        # api_url = 'https://tinyurl.com/api-create.php'
        # params = {'url':link }
        # response = requests.get(api_url, params=params)
        # 
        # website=response.text
        
        print("******************")
        print("")
        print(f"HEADLINE {i+1}")
        print(f"Title: {title}")
        print("")
        print(f"Summary: {summary}")
        print("")
        print(f"Link: ",link)
        print("")
        print("******************")
        





def summarize_article(url):
    # Fetch article content
    article = Article(url)
    article.download()
    article.parse()

    # Generate summary
    article.nlp()
    summary = article.summary

    return summary



# def shorten_url(long_url):
#     api_url = 'https://tinyurl.com/api-create.php'
#     params = {'url': long_url}
#     response = requests.get(api_url, params=params)
#     return response.text
    

main()
