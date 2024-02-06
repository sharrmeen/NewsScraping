# print("HEllo Project")
# print("News Scraping")
# print("Without Commit")

# import requests

# def shorten_url(long_url, api_key):
#     api_url = 'https://tinyurl.com/api-create.php'
#     params = {'url': long_url, 'apikey': api_key}
#     response = requests.get(api_url, params=params)
    
#     if response.status_code == 200:
#         return response.text
#     else:
#         return None
    

# import requests

# def shorten_url(long_url):
#     api_url = 'https://tinyurl.com/api-create.php'
#     params = {'url': long_url}
#     response = requests.get(api_url, params=params)
    
#     if response.status_code == 200:
#         return response.text
#     else:
#         return None

# # Example usage
# long_url = 'https://www.example.com/very-long-url-that-needs-shortening'

# short_url = shorten_url(long_url)
# if short_url:
#     print('Shortened URL:', short_url)
# else:
#     print('Failed to shorten URL')

# import nltk
# nltk.download('punkt')
# import requests
# from newspaper import Article

# def summarize_article(url):
#     # Fetch article content
#     article = Article(url)
#     article.download()
#     article.parse()

#     # Generate summary
#     article.nlp()
#     summary = article.summary

#     return summary

# # Example usage
# article_url = 'https://news.google.com/articles/CBMid2h0dHBzOi8vd3d3Lm5kdHYuY29tL2luZGlhLW5ld3MvcmVhbC1uY3AtYWppdC1wYXdhci1lbGVjdGlvbi1jb21taXNzaW9uLXN1cHJpeWEtc3VsZS12aWN0b3J5LW9mLWludmlzaWJsZS1wb3dlci01MDA3MjI40gEA?hl=en-IN&gl=IN&ceid=IN%3Aen'
# summary = summarize_article(article_url)
# print(summary)


# import openai

# openai.api_key='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'

# response=openai.Completion.create(
#     engine="gpt-3.5-turbo-instruct",
#     prompt="Summarize the following news article:\n\n" +
#            "limate change poses a significant threat to global biodiversity, with far-reaching consequences for ecosystems and species. Rising temperatures, shifting precipitation patterns, and more frequent extreme weather events are disrupting habitats and altering ecosystems worldwide. Species are facing challenges in adapting to these rapid changes, leading to shifts in species distributions, changes in phenology, and increased extinction risks. Human activities, such as deforestation and carbon emissions, exacerbate these effects, further accelerating biodiversity loss. Urgent action is needed to mitigate climate change and protect biodiversity for the well-being of both ecosystems and human societies.",
#     max_tokens=100 
# )

# summary = response.choices[0].text.strip()
# print(summary)