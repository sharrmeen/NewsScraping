from news_scrap import get_newslist

news_list=get_newslist(5)


for i in range(len(news_list)):
    title=news_list[i]['title']
    link=news_list[i]['link']
    print(f"Title: {title}")
    print(f"Link: {link}")
    print("")
