'''
Created on Aug 7, 2021

@author: 4king
'''
from urllib.request import urlopen, Request
'''
Represents the object that navigates the search result pages and obtains their html
'''

class page_navigator(object):
    
    '''
    Constructor for Page_Navigator object
        Parameters:
        searchUrl represents the base url for the pages of search results 
    '''
    def __init__(self, searchUrl):
        self.searchUrl = searchUrl
        self.lastpage = 0
        self.currentpage = 0
    
    
    '''
     Gets the number of the current page that the navigator is on
    '''
    def get_current_page(self):
        return self.currentpage
    
    '''
    Gets the number of the last page of the search results
    '''
    def get_last_page(self):
        return self.lastpage
    
    
    '''
    Gets the first page of the search results
    '''
    def get_first_page(self):
        
        req = Request(self.searchUrl, headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(req).read()
        
        #decodes the page into legible html
        html_search = page.decode("utf-8")
        
        #get the total number of pages that the search result produced
        self._obtainPageNumbers(html_search)
        
        ##get the beginning index of the list of search results
        get_result_beginning_index = html_search.find("<ul class=\"search_results module\">")
        
        #if there are no search results, then the entry doesn't exist
        if (get_result_beginning_index == -1):
            print("Entry Does Not Exist")
            return
        
        
        #create a temp variable that splices the html string by getting rid of everything before the search results
        temp = html_search[get_result_beginning_index:]
        
        #get the end index of the list of search results
        get_result_end_index = temp.find("</ul>")
        
        #create a new variable that only contains the html code for the search results 
        resultsPage = temp[:get_result_end_index] 
        return resultsPage
    
    
    '''
    Gets the given page of the search results
        Parameters:
        page represents the page number that will be navigated to
    '''
    def get_page(self, page):
       
        #update the current page to this new page
        self.currentpage = page
        
        #build the new search url
        newUrl = self.searchUrl + "?page=" + str(page)
        
        #send out a request to obtain the html source code from the searchUrl in utf-8 encoding
        req = Request(newUrl, headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(req).read()
        
        #decodes the page into legible html
        html_search = page.decode("utf-8")
        
        #if there are no search results, then the page doesn't exist
        get_result_beginning_index = html_search.find("<ul class=\"search_results module\">")
        if (get_result_beginning_index == -1):
            print("Page Does Not Exist")
            return None
        
        #create a temp variable that splices the html string by getting rid of everything before the search results
        temp = html_search[get_result_beginning_index:]
        
        #get the end index of the list of search results
        get_result_end_index = temp.find("</ul>")
        
        #create a new variable that only contains the html code for the search results on the new page
        resultsPage = temp[:get_result_end_index] 
        
        return resultsPage
        
    '''
    Obtains the page number of the last page in the Metacritic search query
        Parameters:
        html represents the html code of the search query site page
    '''
    def _obtainPageNumbers(self, html):
        #find the index that contains the information of the last page in the query
        last_page_index = html.find("<li class=\"page last_page\">")
        
        #declare the lastpage as a global variable
        
        
        #if there are no other pages besides the current page
        if(last_page_index == -1):
            
            self.lastpage = 0
            return
        
        #update the html so that it only contains code after the last page code
        html = html[last_page_index:]
        
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
        #update lastpage global variable
        self.lastpage = int(html[0]) - 1