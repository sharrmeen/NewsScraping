import cowsay
from requests_html import HTMLSession

session=HTMLSession()

url='https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFZxYUdjU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen'

r=session.get(url)
r.html.render(sleep=1,scrolldown=1)

articles = r.html.find('article')

for item in articles:
    try:
        newsitem = item.find('h3',first=True)
        title = newsitem.text
        link =  newsitem.absolute_links
        print(title,link)
    except:
        pass

