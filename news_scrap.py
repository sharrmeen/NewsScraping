from requests_html import HTMLSession

def get_newslist(max_articles=5):

    session=HTMLSession()

    url='https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFZxYUdjU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen'
    r=session.get(url)
    r.html.render(sleep=1,scrolldown=1)

    articles = r.html.find('a.gPFEn')
    # print(articles)
    newslist=[]


    for idx,item in enumerate(articles):

        if idx==max_articles:
            break
        
        title = item.text
        link = "https://news.google.com" + item.attrs['href']

        newsarticle = {
            'title': title,
            'link': link 
        }
        newslist.append(newsarticle)


    return newslist
