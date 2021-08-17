'''
Created on Aug 10, 2021

@author: Jacob Summers
'''

from urllib.request import urlopen, Request
from webscrape.searchresults.categorydetails.tvdetail.tvparse.tv_review import tv_review

class tv_user_parser(object):
    '''
    Constructor for TV_User_Parser object
    Parameters:
        link represents the link (url) of the tv's user reviews
    '''
    def __init__(self, link):
        
        #results represents the list of reviews on a given page
        self.results = []
        
        #link represents the link of the url
        self.link = link
        #gets the html page of the first page
        self._get_html_page(0)
        
        #represents the current page
        self.current_page = 0
        
        #represents the last page
        self.lastpage = self._get_page_count()
        
    '''    
    Moves to the next page of the user reviews 
    '''   
    def move_to_page(self, page):
        
        self._get_html_page(page)
    '''
    Gets the user reviews on the current page and returns them
    '''
    def get_results(self):
        self.results = self._get_reviews()
        return self.results
    
    '''
    Gets the current page number 
    '''
    def get_current_page(self):
        return self.currentpage
    
    '''
    Gets the last page number
    '''
    def get_last_page(self):
        return self.lastpage
    
    '''
    Gets the html page of a given page of the user reviews
    '''
    def _get_html_page(self, page):
        
        self.currentpage = page
        
        #retreives the html code from the website
        req = Request(self.link + "?page=" + str(page), headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(req).read()
        self.html = page.decode("utf-8")
        
        
    '''
    Gets the number of pages of user reviews that are available for the given item
    '''    
    def _get_page_count(self):
        #find the index that contains the information of the last page in the query
        last_page_index = self.html.find("<li class=\"page last_page\">")
        
         
        #if there are no other pages besides the current page
        if(last_page_index == -1):
            
            return 0
        
        #update the html so that it only contains code after the last page code
        html = self.html[last_page_index:]
        
        #find the code where the page number of the last page is located
        last_page_index = html.find("<a class")
        last_page_index_end = html.find("</a>")
        
        #shorten the html further so that the page number can be extracted
        html = html[last_page_index:last_page_index_end]
        last_page_index = html.find(">") + 1
        
        #make the html string only equal to the page number
        html = html[last_page_index:]
        
        #eliminate any leading or trailing whitespace
        html = html.split()
        
        return int(html[0]) - 1
    
    '''
    Parses all of the reviews on the given page
    '''
    def _get_reviews(self):
        #empty list that will hold the review objects
        reviews = []
        
        #find the index where user reviews begin in the html code
        start_index = self.html.find("<div class=\"user_reviews\">") + len("<div class=\"user_reviews\">")
        
        
        #seperate the review html from everything before it
        html = self.html[start_index:]
        
        
        start_index = html.find("<div class=\"review pad_top1\"") 
        
        #if there are no reviews available
        if (start_index == -1):
            return []
        
        
        #get the first review
        start_index = start_index + len("<div class=\"review pad_top1\"")
        
        current_review = html[start_index:]
        
        #create the movie_review object that will parse the review
        review = tv_review(current_review) 
        
        #add the review to the list
        reviews.append(review)
        
        #move the html to the next review
        html = html[start_index:]
        
        #find the index of the next review
        start_index = html.find("<div class=\"review pad_top1\"")
        
        #while there are still reviews left
        while (start_index != -1):
            
            #get the first review
            start_index = start_index + len("<div class=\"review pad_top1\"")
            
            current_review = html[start_index:]
            
            #create the movie_review object that will parse the review
            review = tv_review(current_review) 
            
            #add the review to the list
            reviews.append(review)
            
            
            #move the html to the next review
            html = html[start_index:]
            
            #find the index of the next review
            start_index = html.find("<div class=\"review pad_top1\"") 
        
       
        
        return reviews
        