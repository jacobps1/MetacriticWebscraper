'''
Created on Aug 7, 2021

@author: Jacob Summers
'''

from urllib.request import urlopen, Request
import textwrap
from webscrape.searchresults.categorydetails.gamedetail.gameparse.game_parser import game_parser
from webscrape.searchresults.categorydetails.gamedetail.gamedisplay import game_user_reviews
from webscrape import clear

def view_game_details(game_link):
    
    #clear command line
    clear()
    
    #obtain the html code for the game page
    req = Request(game_link, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    html_game = page.decode("utf-8")
    
    
    #create the parser and parse each element
    parser = game_parser(html_game)
    name = parser.get_name()
    
    summary = parser.get_summary()
    summary = summary.replace('<br/>', '\n')
    credit = parser.get_credit()
    
    #print the results to the command line
    print(name)
    #create the formatting for the summary
    body = '\n\n'.join(['\n'.join(textwrap.wrap(line, 100,
                 break_long_words=False, replace_whitespace=False))
                 for line in summary.splitlines() if line.strip() != ''])
    print(body)
    print("\n" + credit + "\n\n")
    
    
    #prompt the user to view the reviews of the movie
    answer = input("Type r to view user reviews. Type anything else to go back to results page\n")
    
    #while the answer is r
    while (answer == "r"):
        
        game_user_reviews.view_game_user_reviews(game_link + "/user-reviews")
        #clear the command line
        clear()
        #print the results to the command line
        print(name)
        print(body)
        print("\n" + credit + "\n\n")
        
        #prompt the user to view the reviews of the movie
        answer = input("Type r to view user reviews. Type anything else to go back to results page\n")
    
    