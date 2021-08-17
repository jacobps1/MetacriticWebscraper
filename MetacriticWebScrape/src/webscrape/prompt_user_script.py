'''
Created on Aug 5, 2021

@author: Jacob Summers
'''

from webscrape.searchresults import prompt_user_search_results_script

from webscrape import clear

#insert the spaces into the url search
def insertSpaces(name):
    
    for i in range(len(name)):
        if (name[i] == " "):
            num = i + 1
            name = name[:i] + "%20" + name[num:]  
    
    ##print(name)
    newN = name
    return newN
    
    


#prompt the user to enter their search choices
def prompt_user():
    print("Welcome to Metacritic Webscraping!\n\n")
   
    
    
    categories = ["movie", "tv", "game", "album", "all"]
    print("1. Movies")
    print("2. TV Shows")
    print("3. Video Games")
    print("4. Album")
    print("5. All")
    #prompt the user to enter their search category
    index = input("Enter the number that corresponds with the category you would like to search in\nOr\nEnter invalid number to exit\n")
    
    if (index.isdigit() == False):
        index = -1
    index = int(index)
    
    while(index > 0 and index <= len(categories)):
        
        category = categories[index - 1]
        
        #convert the user input to lower-case for consistency
        name = input("Enter the name of what you wish to search\n")
        name = name.lower()
        
        searchName = name
        if " " in name:
            searchName = insertSpaces(name)
         
         
        #clear output here
        clear()
         
        if (searchName != None):
            prompt_user_search_results_script.find_results(searchName, category)
        
        #clear output here
        clear()
        
        print("1. Movies")
        print("2. TV Shows")
        print("3. Video Games")
        print("4. Album")
        print("5. All")
        
        index = input("Enter the number that corresponds with the category you would like to search in\nOr\nEnter invalid number to exit\n")
        #check to see if the index is a valid number
        if (index.isdigit() == False):
            index = -1
        
        index = int(index)
        
    
    print("Thanks for using my program!")
    
    


    
