To Run On Command Line: python webscraperdriver.py

Run on Eclipse: click run button on webscraperdriver.py

NOTE: This program was made with Python 3.7.2

The idea for my Metacritic webscraper came from after doing research on the available html
parser packages on Python. After learning about Beautiful Soup and Mechanical Soup, I decided
to see what I could parse from Metacritic, a website that aggregates reviews of films, tv shows,
albums, and video games that happens to be one of my favorite websites to browse. After doing
research on Metacritic and webscrapping, I found that many had already used Beatiful Soup and
Mechanical Soup to parse html and submit forms and queries to the website. At that point, I decided
I would try and create my own program that acted as a webscraper for Metacritic rather than duplicating 
what had already been done before. As I was looking through the HTML code of Metacritic, I realized that 
I could use Python's built in String methods in order to parse the details that I wanted. I ended up creating
a program written in Python that prompted the user to search for a tv show, movie, album, or video game on Metacritic in order to 
view its Metascore (aggregate critic rating), its miscellaneous details such as the name, summary, and the people who worked on it, 
and its user reviews.

The program consisted of four different packages that were dedicated to the different parsings and user inputs for the movies, tv shows,
video games, and albums available on the website. In addition to those packages, there was a package dedicated to the 
parser objects required for parsing and navigating the search results on the search result pages and a package that prompted the user to choose 
the search result they wished to view.

Throughout the program, Python's String splicing and find methods were used to find and extract key words in the html code. 
In order to get the html code from a given page, Python's urllib package was used to send requests to
Metacritic's servers in order to recieve it's utf-8 encoded html code.

Files:
webscraperdriver.py - acts as the driver method for the program

package webscrape:
prompt_user_script.py - prompts the user to enter the name of what they want to search
and creates the link for the search


package webscrape.searchresults:
prompt_user_search_results_script.py - prompts the user to select a result from the search
results page that was generated as a result of their search query in prompt_user_script.py


package webscrape.searchresults.searchresultparsers:
page_navigator.py - represents the object that navigates the html pages of the search results
that were generated from the search query

search_result_parser.py - parses the search results so that they may be displayed in
prompt_user_search_results_script.py


package webscrape.searchresults.categorydetails.*detail.*display:
*_detail.py - displays the details of the result chosen by the user

*_user_reviews.py - displays the pages of the user reviews available for the result

*_view_review_detail.py - displays the contents of a chosen user's review of the result


package webscrape.searchresults.categorydetails.*detail.*parse:
*_parser.py - parses the html page of the result in order to obtain its details

*_review.py - represents the object that contains the information for a user's review

*_user_parser.py - parses the html pages of the user reviews in order to obtain all of them