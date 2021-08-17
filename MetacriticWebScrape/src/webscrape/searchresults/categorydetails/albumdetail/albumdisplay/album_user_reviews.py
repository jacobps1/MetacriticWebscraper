'''
Created on Aug 10, 2021

@author: Jacob Summers
'''
from webscrape.searchresults.categorydetails.albumdetail.albumparse.album_user_parser import album_user_parser
from webscrape.searchresults.categorydetails.albumdetail.albumdisplay import album_view_review_detail
from webscrape import clear

#represents the parser that parses the review pages
parser = 0

#goes to the next page of reviews
def _next_page(page, results):
    #check to see if the page exists
    if (page > parser.get_last_page()):
        print("Page does not exist")
        #view the results again
        view_results(results)
        return
    
    #move the parser to the next page
    parser.move_to_page(page)
    
    #get the new review results from the parser
    results = parser.get_results()
    #view them
    view_results(results)
    
#print the reviews that are on the given page
def print_page_reviews(results):
    #clear command line output
    clear()
    #number of reviews on the page
    number = 1
    #loop through each review and print it
    for result in results:
        print(str(number) + ". " + result.to_string())
        number = number + 1
    #if the number is still 1, then the for loop was never entered due to results being empty
    if (number == 1):
        print("There are no user reviews on this page")
        
    #print the current page
    print("Page " + str(parser.get_current_page()) + " of " + str(parser.get_last_page()))  
        
#displays the reviews and prompts the user to navigate the pages of reviews
def view_results(results):
    
    #prints the reviews
    print_page_reviews(results)
    
    #prompts the user to either enter a page number or view a review
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
        _next_page(page, results)
        
        return
    #cast the user input into a number
    number = int(number)
    
    #while the number is a valid number
    while (number > 0 and number < len(results) + 1):
        
        #get the chosen review
        chosenresult = results[number-1]
        
        #view the details of the review here
        album_view_review_detail.view_review_detail(chosenresult)
        
        
        print_page_reviews(results)
        
        
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
            _next_page(page, results)
        
            return
    
        number = int(number)
        

#view the user reviews of the movie      
def view_album_user_reviews(user_link):
    global parser
    
    #create the parser for the review
    parser = album_user_parser(user_link)
    
    #get the reviews on the page
    results = parser.get_results()
    
    #view the results
    view_results(results)