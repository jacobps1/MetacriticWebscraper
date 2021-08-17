'''
Created on Aug 7, 2021

@author: 4king
'''

from urllib.request import urlopen, Request
import textwrap
from webscrape.searchresults.categorydetails.tvdetail.tvparse.tv_parser import tv_parser
from webscrape.searchresults.categorydetails.tvdetail.tvdisplay import tv_user_reviews
from webscrape import clear

def view_tv_details(tv_link, season_number):
    #clears the command line output
    clear()
    #if the link is the season of a show
    if (season_number != 0):
        req = Request(tv_link + "/season-" + str(season_number), headers={'User-Agent': 'Mozilla/5.0'})
    
    #if the link is the series overview
    else:
        req = Request(tv_link, headers={'User-Agent': 'Mozilla/5.0'})
    
    page = urlopen(req).read()
    html_tv = page.decode("utf-8")
    
    
    #create the parser and parse each element
    parser = tv_parser(html_tv)
    name = parser.get_name()
    cast = parser.get_cast()
    summary = parser.get_summary()
    summary = summary.replace('<br/>', '\n')
    credit = parser.get_credit()
    seasons = parser.get_seasons()
    num_seasons = parser.get_number_seasons()
    #print the results to the command line
    print(name)
    print(cast + "\n")
    
    #create the formatting for the summary
    body = '\n\n'.join(['\n'.join(textwrap.wrap(line, 100,
                 break_long_words=False, replace_whitespace=False))
                 for line in summary.splitlines() if line.strip() != ''])
    
    print(body)
    print("\n" + credit + "\n\n")
    print(seasons + "\n") 
    
    
    #prompt the user to view the reviews of the show
    answer = input("Type r to view user reviews. Type s to change to a different season. Type anything else to go back to results page\n")
    
    if (answer == "s"):
        season = input("Enter the number that corresponds with the season you want to view. Invalid numbers default to series overview\n")
        if (season.isdigit() == False):
            season = "0"
        
        season = int(season)
        
        if (season > num_seasons):
            season = 0
        view_tv_details(tv_link, season)
        
        return
    
    #while the answer s still user reviews
    while (answer == "r"):
        
        
        tv_user_reviews.view_tv_user_reviews(tv_link + "/user-reviews")
        
        #clears the command line output
        clear()
        
        #print the results to the command line
        print(name)
        print(cast + "\n")
        print(body)
        print("\n" + credit + "\n\n")
        
        
        #prompt the user to view the reviews of the show
        answer = input("Type r to view user reviews. Type s to change to a different season. Type anything else to go back to results page\n")
    
        if (answer == "s"):
            season = input("Enter the number that corresponds with the season you want to view. Invalid numbers default to series overview\n")
            
            if (season.isdigit() == False):
                season = "0"
        
            season = int(season)
        
            if (season > num_seasons):
                season = 0
            
            view_tv_details(tv_link, season)
        
            return
    