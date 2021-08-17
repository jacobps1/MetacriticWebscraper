'''
Created on Aug 5, 2021

@author: 4king
'''


from webscrape.searchresults.categorydetails.moviedetail.moviedisplay import movie_detail
from webscrape.searchresults.categorydetails.tvdetail.tvdisplay import tv_detail
from webscrape.searchresults.categorydetails.albumdetail.albumdisplay import album_detail
from webscrape.searchresults.categorydetails.gamedetail.gamedisplay import game_detail
from webscrape.searchresults.searchresultparsers.search_result_parser import search_result_parser
from webscrape.searchresults.searchresultparsers.page_navigator import page_navigator
from webscrape import clear
#represents the navigator that gets the html code for each page
navigator = 0


'''
Gets the given page of the search results
    Parameters:
    page represents the page number that will be navigated to
'''
def _next_page(page):
    
    
    #get the html portion of the search results from the given page
    resultsPage = navigator.get_page(page)
    
    if resultsPage is None:
        return
    #create the parser object that will obtain the results and links from the html portion
    parser = search_result_parser(resultsPage)
    
    #retrieve the links and formatted results
    links = parser.get_links()
    results = parser.get_results()
    
    #prompt the user to choose their result
    _choose_result(links, results)
    

'''
Prints the formatted search results in order
    Parameters:
    resultnames represents the list of formatted results
'''
def _print_results(resultnames):
    #represent the result number
    clear()
    number = 1
    #for each result in resultnames, print the values in order
    for results in resultnames:
        print(str(number) + ": " + results)
        number = number + 1
    #if the for loop was not entered, then there were no results available on the page
    if (number == 1):
        print("There are no movies, tv shows, video games, or albums on this page")
    
    #print the current page
    print("Page " + str(navigator.get_current_page()) + " of " + str(navigator.get_last_page()))    

'''
Allows the user to choose the search result they want to look at
    Parameters:
    result represents the html result
'''  
def _choose_result(links, resultnames):
    #prints all of the formatted search results
    _print_results(resultnames)
    
    #prompts the user to either view a new page or to view a search result
    number = input("Enter the number that corresponds with the result you would like to view. Enter invalid number to exit\n OR \nType 0 to change the page\n")
    #if the number is invalid
    if (number.isdigit() == False):
        number = -1
    #if the number is zero then the user wants to navigate to a different page
    if (number == "0"):
        #prompt user for page number
        page = input("Enter page number\n")
        #if the page is not valid
        if (page == ""):
            page = 0
        
        page =  int(page)
        #go to the next page    
        _next_page(page)
        
        return
    #cast the user input into a number
    number = int(number)
    
    #while the number is a valid number
    while (number > 0 and number < len(resultnames) + 1):
        
        #get the chosen result link
        chosenresult = links[number-1]
        chosenresultname = resultnames[number-1]
        #view the details
        
        #if the category is a movie
        if (chosenresultname.find("Category: Movie,") != -1):
            movie_detail.view_movie_details(chosenresult)
        
        #if the category is a tv show
        elif (chosenresultname.find("Category: TV Show,") != -1):
            tv_detail.view_tv_details(chosenresult , 0)
        
        #if the category is a album
        elif (chosenresultname.find("Category: Album,") != -1):
            album_detail.view_album_details(chosenresult)
        
        #if the category is a video game
        elif (chosenresultname.find("Category: Game,") != -1):
            game_detail.view_game_details(chosenresult)
        
        
        #prints the formatted results in order
        _print_results(resultnames)
        
        #prompts the user to either view a new page or to view a search result
        number = input("Enter the number that corresponds with the result you would like to view. Enter invalid number to exit\n OR \nType 0 to change the page\n")
            #if the number is invalid
        if (number.isdigit() == False):
            number = -1
        
        #if the number is zero then the user wants to navigate to a different page
        if (number == "0"):
            #prompt user for page number
            page = input("Enter page number\n")
            #if the page is not valid
            if (page.isdigit() == False):
                page = 0
            
            page =  int(page)
                
            #go to the next page 
            _next_page(page)
        
            return
    
        number = int(number)
           
    

'''
Finds the list of results that are obtained from doing the search query on metacritic
    Parameters:
    resultName represents the name that the user is trying to search for
    category represents the what category the user is searching resultName in
'''
def find_results(resultName, category):
    #represents the url that will be used for navigating to different pages
    searchUrl = "https://www.metacritic.com/search/" + category + "/"+ resultName + "/results"
    
    #initialize the navigator object that obtains the html code from each page of the search results
    global navigator
    navigator = page_navigator(searchUrl)
    
    
    #get the html portion of the search results from the first page
    resultsPage = navigator.get_first_page()
    
    if (resultsPage == None):
        return
    #create the parser object that will obtain the results and links from the html portion
    parser = search_result_parser(resultsPage)
    
    #retrieve the links and formatted results
    links = parser.get_links()
    results = parser.get_results()
    
    #prompt the user to choose their result
    _choose_result(links, results)
    
    