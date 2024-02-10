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

#### Option 1:

In this case, the ***get_newslist*** function is called with the parameter 'num' that is the number of articles to be printed. The articles recieved from this function are stored in a list called as **news_list**. 

##### get_newslist

The function get_newslist starts by importing the HTMLSession class from the requests_html library, enabling it to interact with web pages. It is designed to retrieve news articles from a specific Google News URL and return them in a structured format. Upon initialization, the function establishes an instance of HTMLSession and assigns the target URL of the Google News page to the variable url. It then sends an HTTP GET request to this URL and renders the HTML content using the render() method to ensure that dynamic elements, such as JavaScript-driven components, are fully loaded. The function then identifies the HTML elements corresponding to news article links using a CSS selector and stores them in the articles variable. Next, it iterates through these articles, extracting the title and link for each one. A limit on the number of articles to retrieve is enforced through a conditional check, ensuring the function stops once the specified maximum number (max_articles) is reached. For each article, its title and link are encapsulated within a dictionary and appended to a list named newslist. Finally, the function returns this list, containing dictionaries representing each news article with its respective title and link. Overall, this function provides a convenient and automated method for programmatically fetching and processing news articles from a Google News page.


