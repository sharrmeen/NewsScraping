import requests
import nltk
import random
from news_scrap import get_newslist
from newspaper import Article

def main():
    print("Welcome. What would you like to do today?")
    print("1.Read News")
    print("2.Play Rock,Paper,Scissor")
    option=int(input("Option: "))
    if option==1:
        num=int(input("How many articles would you like to see ? "))
        news_list=get_newslist(num)
        print_news(news_list)
    elif option==2:
        player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        result=rps(player_choice)
        print(result)
    

def print_news(news_list):
    print("")
    for i in range(len(news_list)):
        title=news_list[i]['title']
        link=news_list[i]['link']
        summary=summarize_article(link)

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
    try:
        # Fetch article content
        article = Article(url)
        article.download()
        article.parse()

        # Generate summary
        article.nlp()
        summary = article.summary

        return summary
    
    except Exception as e:
        return f"Error: {str(e)}"



def shorten_url(long_url):
    api_url = 'https://tinyurl.com/api-create.php'
    params = {'url': long_url}
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()   
        return response.text
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

    
def rps(player_choice):

    
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    # Determine the winner
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

if __name__=="__main__":
    main()
