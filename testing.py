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

import requests

# def summarize_url(url, api_key, summary_length=5):
#     api_url = "https://api.smmry.com"
#     params = {
#         "SM_API_KEY": api_key,
#         "SM_LENGTH": summary_length,
#         "SM_URL": url,  # Use this instead of input_text if summarizing a URL
#         "SM_WITH_BREAK": True  # Return summary with line breaks
#     }
#     response = requests.post(api_url, data=params)
#     if response.status_code == 200:
#         # Extract the summarized text from the response
#         data = response.json()
#         if 'sm_api_error' in data:
#             return f"Error: {data['sm_api_error']}"
#         else:
#             summary = data.get("sm_api_content")
#             return summary
#     else:
#         return f"Error: {response.status_code}"


# # Example usage:
# api_key = "460CBC23A1"
# url="https://www.livemint.com/news/india/modi-unveils-projects-worth-over-rs-1-330-crore-in-goa-11707221147382.html"
# summary = summarize_url(url, api_key)
# print(summary)

# def summry():
# API_ENDPOINT = "https://api.smmry.com"
# API_KEY = "460CBC23A1"

# params = {
#     "SM_API_KEY":API_KEY,
#     "SM_URL":"https://news.google.com/articles/CBMiigFodHRwczovL3d3dy5uZHR2LmNvbS9pbmRpYS1uZXdzL3JhaHVsLWdhbmRoaS1iaGFyYXQtam9kby15YXRyYS1ob3ctaGF2ZS1kb2dzLWhhcm1lZC1ianAtcmFodWwtZ2FuZGhpLXJlc3BvbmRzLXRvLXZpcmFsLXB1cHB5LXZpZGVvLTUwMDQ5NDjSAQA?hl=en-IN&gl=IN&ceid=IN%3Aen"
# }

# r = requests.get(url=API_ENDPOINT, params=params)
# print(r.json())

