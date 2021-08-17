'''
Created on Aug 7, 2021

@author: 4king
'''

from urllib.request import urlopen, Request
import textwrap
from webscrape.searchresults.categorydetails.albumdetail.albumparse.album_parser import album_parser
from webscrape.searchresults.categorydetails.albumdetail.albumdisplay import album_user_reviews
from webscrape import clear

def view_album_details(album_link):
    #clear command line
    clear()
    #obtain the html for the album page
    req = Request(album_link, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    html_album = page.decode("utf-8")
    
    #create the parser and parse each element
    parser = album_parser(html_album)
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
    
    
    #prompt the user to view the reviews of the album
    answer = input("Type r to view user reviews. Type anything else to go back to results page\n")
    
    #while the answer is r
    while (answer == "r"):
        
        album_user_reviews.view_album_user_reviews(album_link + "/user-reviews")
        #clear command line output
        clear()
        #print the results to the command line
        print(name)
        print(body)
        print("\n" + credit + "\n\n")
        
        #prompt the user to view the reviews of the movie
        answer = input("Type r to view user reviews. Type anything else to go back to results page\n")
    
    
    