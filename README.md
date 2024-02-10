# News On the Go

### A simple implementation of web scraping from the Google News website

In this fast pacing world it's getting harder and harder to stay aware of current affairs.
***News on the Go*** is simplified rendition of a biggger idea that I hope to work on in the future.
The current program allows you to specify the number of news stories you would like to read and then outputs them in an orderly manner along with their summaries and links to the original article.
Similar to the fashion of traditional newspapers, it also includes a game of _rock,paper,scissors_ that the users can choose if they want to indulge themselves in a refreshment task. 

### _Implemntation_

The main principle behind this program is to use the techninque of web scraping for a popular news publishing website, in this case - Google News, and select the number of stories specified by the user. We assume that the articles are arranged in their order of decreasing importance and therefore the article at the top has the most relevancy and so on.

The main function asks the user to choose between reading the news or playing a game of rock,paper and scissors.
Depending on the input recieved, it then calls the necessary functions.

### Option 1:

In this case, the ***get_newslist*** function is called with the parameter 'num' that is the number of articles to be printed. The articles recieved from this function are stored in a list called as **news_list**. 

#### get_newslist(num)

The function get_newslist starts by importing the HTMLSession class from the requests_html library, enabling it to interact with web pages. It is designed to retrieve news articles from a specific Google News URL and return them in a structured format. Upon initialization, the function establishes an instance of HTMLSession and assigns the target URL of the Google News page to the variable url. It then sends an HTTP GET request to this URL and renders the HTML content using the render() method to ensure that dynamic elements, such as JavaScript-driven components, are fully loaded. The function then identifies the HTML elements corresponding to news article links using a CSS selector and stores them in the articles variable. Next, it iterates through these articles, extracting the title and link for each one. A limit on the number of articles to retrieve is enforced through a conditional check, ensuring the function stops once the specified maximum number (max_articles) is reached. For each article, its title and link are encapsulated within a dictionary and appended to a list named newslist. Finally, the function returns this list, containing dictionaries representing each news article with its respective title and link. Overall, this function provides a convenient and automated method for programmatically fetching and processing news articles from a Google News page.

#### print_news(news_list)

After recieving the *_news_list _* from the ***get_newlist*** function the list is passed to another function called print_news.


The function print_news is designed to display news articles stored in a list in a formatted manner. It takes news_list as its input, which is a list of dictionaries, each containing information about the news article, specifically its title and link. Within the function, a loop iterates over the length of the news_list. For each article in the list, it retrieves the title and link from the corresponding dictionary. Additionally, it calls a function summarize_article(link) to generate a summary of the article using its provided link. This summary is then printed alongside the article's title and link in a structured format. The function precedes each article with a decorative header denoting the article number. Overall, print_news facilitates the easy display of news articles along with their titles, summaries, and links, enhancing readability and accessibility of the news content.

#### summarize_article(url)

summarize_article(url) summarizes the content of an article found at the provided URL. It uses the Article class from the newspaper3k library to download and parse the article. Then, it applies natural language processing to generate a summary of the article's main points using the nlp() method. If any errors occur during this process, such as network issues or parsing problems, it catches them using a try-except block and returns an error message indicating the encountered exception.


### Option 2:

If the user selects this option, then a game of rock,paper,scissors is initiated. The player is asked for his choice (amongst rock,paper and scissors) and the input is passed to the ***rps*** function.

#### rps(player_choice)

This function begins by creating a list of choices (rock, paper, scissors) and randomly selects one for the computer's choice. The function then compares the player's choice with the computer's choice to determine the winner. If both choices are the same, it's a tie. Otherwise, it checks all possible winning scenarios for the player against the computer (rock beats scissors, paper beats rock, scissors beats paper). If the player's choice matches any of these winning scenarios, the player wins; otherwise, the computer wins. The function then returns a string indicating the outcome of the game.

## Conclusion

This is the final project developed for Harvard's 'Introduction to Programming with Python' by David J. Malan .
I have used many of the concepts taught in class along with some additional modules that are listed in requirements.txt .
