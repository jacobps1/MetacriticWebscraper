'''
Created on Aug 5, 2021

@author: Jacob Summers
'''
from urllib.request import urlopen, Request
import textwrap
from webscrape.searchresults.categorydetails.moviedetail.movieparse.movie_parser import movie_parser
from webscrape.searchresults.categorydetails.moviedetail.moviedisplay import movie_user_reviews
from webscrape import clear

#views the details of the movie that are parsed out by the movie_parser object
def view_movie_details(movie_link):
    #clear the command line output
    clear()
    #obtain the html code for the movie page
    req = Request(movie_link, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    html_movie = page.decode("utf-8")
    
    #create the parser and parse each element
    parser = movie_parser(html_movie)
    name = parser.get_name()
    cast = parser.get_cast()
    summary = parser.get_summary()
    summary = summary.replace('<br/>', '\n')
    credit = parser.get_credit()
    
    #print the results to the command line
    print(name)
    print(cast + "\n")
    #create the formatting for the summary
    body = '\n\n'.join(['\n'.join(textwrap.wrap(line, 100,
                 break_long_words=False, replace_whitespace=False))
                 for line in summary.splitlines() if line.strip() != ''])
    
    print(body)
    print("\n" + credit + "\n\n")
    
    #prompt the user to view the reviews of the movie
    answer = input("Type r to view user reviews. Type anything else to go back to results page\n")
    
    #while the
    while (answer == "r"):
        
        movie_user_reviews.view_movie_user_reviews(movie_link + "/user-reviews")
        #clear the command line output
        clear()
        #print the results to the command line
        print(name)
        print(cast + "\n")
        print(body)
        print("\n" + credit + "\n\n")
        
        #prompt the user to view the reviews of the movie
        answer = input("Type r to view user reviews. Type anything else to go back to results page\n")
    
    
    
    
    