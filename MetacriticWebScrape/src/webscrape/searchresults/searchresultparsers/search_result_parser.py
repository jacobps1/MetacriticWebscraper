'''
Created on Aug 7, 2021

@author: Jacob Summers
'''

'''
    Represents the object that parses the results and their links from the html search results
'''
class search_result_parser(object):
    '''
    Constructor for Search_Result_Parser
        Parameters:
        results represent the html code consisting of the list of results
    '''

    def __init__(self, results):
        self.html = results
        self.results = []
        self.links = []
        
        
        self._parse_results()
    
    
    '''
    Gets the list of formatted results
    '''
    def get_results(self):
        return self.results
    
    
    '''
    Gets the list of links associated with the results
    '''
    def get_links(self):
        return self.links
    
    '''
    Parses out a list of the different search results in html format
        Parameters:
        none
    '''
    def _parse_results(self):
        
        
        
        #creates the list that holds the individual results in html format
        results = []
        
        #finds the index of the first search result listed in the html code
        entry_start = self.html.find("<li class=\"result first_result\">")
        
        #finds where the first search result ends
        entry_last = self.html.find("</li>") + len("</li>")
        
        #adds the result in html form to the list
        results.append(self.html[entry_start:entry_last])
        
        #gets rid of the first search result in the html code
        html = self.html[entry_last:]
        
        
        #finds the index of the next result
        entry_start = html.find("<li class=\"result\">")
        
        #while there are still search results
        while (entry_start != -1):
            
            #finds where the current search result ends
            entry_last = html.find("</li>") + len("</li>")
            
           
            #adds the result in html form to the list
            results.append(html[entry_start:entry_last])
            
            #gets rid of the current search result in the html code
            html = html[entry_last:]
            
            #moves on to the next result
            entry_start = html.find("<li class=\"result\">")
        
        
        #format the html results into readable results
        self._format_results(results)
        
        
        '''
    Creates the lists consisting of the formatted html results and the links used to access their metacritic pages
        Parameters:
        resultslist represents the list of html results
    '''
    def _format_results(self, resultslist): 
        #represents the list of website links associated with each result
        #links = []
        
        #represents the formatted names of the results
        #resultnames = []
        
        #for each result in the list of html results
        for result in resultslist:
            #get the formatted name of the html result
            result_name = self._get_result_name(result)
            #get the link to the result's page from the html result
            link = self._get_result_link(result)
            
            #check to see if the result is a movie, tv show, video game, or album
            if self._is_valid_category(result_name) and "/person/" not in link:
                
                #add the result to the list
                self.results.append(result_name)
                #add the link to the list        
                self.links.append(link)
            
        #call the function that allows the user to choose a result
        #_choose_result(links, resultnames)
        
        
        
        '''
    Gets the link from the html search result
        Parameters:
        result represents the html result
    '''  
    def _get_result_link(self, result):
        #base url used on the metacritic website
        baseurl = "https://www.metacritic.com"
        
        #isolate the metascore in the html code by finding the indices of the a href class that it is surrounded in
        link_start_index = result.find("<a href=\"")
        link_start_index = link_start_index + len("<a href=\"")
        
        link = result[link_start_index:]
        
        #isolate the link in the html by finding the indices of the carrot that surrounds it to the right
        link_end_index = link.find("\">")
        
        link = link[:link_end_index]
        
        #build the link from the metacritic link
        link = baseurl + link
        
        return link
    
    
    '''
    Gets the metascore from the html search result
        Parameters:
        result represents the html result
    '''
    def _get_result_metascore(self, result):
        
        #isolate the metascore in the html code by finding the indices of the span class that it is surrounded in
        score_start_index = result.find("<span class") + len("<span class")
        score_end_index = result.find("/span>")
        result = result[score_start_index:score_end_index]
        
        #isolate the metascore in the html by finding the indices of the carrots that surround it 
        score_start_index = result.find(">") + 1
        score_end_index = result.find("<")
        score = result[score_start_index: score_end_index]
        
        #remove any unnecessary leading or trailing whitespace
        score = score.strip()
        
        #if there is no valid metascore
        if (score == ""):
            score = "tbd"
        
        
        return score
        
         
    '''
    Gets the category (movie, video game, tv show, album) from the html result
        Parameters:
        result represents the html result
    '''
    def _get_result_category(self, result):
        
        #isolate the category by finding the indices of the p tags that surround it
        cat_start_index = result.find("<p>") + len("<p>")
        cat_end_index = result.find("</p>")
        category = result[cat_start_index:cat_end_index]
        
        
        #check to see if the result is a video game
        if "<span class=\"platform\">" in category:
            platform = ""
            
            #isolate the value of the platform from the category
            cat_start_index = category.find("<span class=\"platform\">") + len("<span class=\"platform\">")
            cat_end_index = category.find("</span>")
            platform = category[cat_start_index:cat_end_index]
            
            #after isolating the platform from the category, obtain the category
            cat_start_index = category.find("</span>") + len("</span>")
            category = category[cat_start_index:]
            
            #remove any unnecessary leading or trailing whitespace
            category = category.strip()
            platform = platform.strip()
            
            #format the category string
            #return platform + ": " + category + " "
            format = category + " (" + platform + ")"
            format = format.strip()
            return format
            
        #remove any unnecessary leading or trailing whitespace
        category = category.strip()
        
        return category
        
    '''
    Gets the formatted name of the html result that consists of the name, metascore, and category
        Parameters:
        result represents the html result
    '''
    def _get_result_name(self, result):
        
        #calls the _get_result_metascore method to get the value of the metascore
        metascore = self._get_result_metascore(result)
        
        #calls the _get_result_category method to get the category
        category = self._get_result_category(result)
        
        #find the index where the link begins (which contains the name of the result)
        link_start_index = result.find("<a href") 
        
        #splice the result so that it only contains html code after the link
        result = result[link_start_index:]
        
        #isolate the name of the result by getting the indices of the strings that surround it
        link_start_index = result.find("\">") + len("\">")
        link_end_index = result.find("</a>") 
        result_name = result[link_start_index:link_end_index]
        
        #remove any new line characters in the name of the result
        result_name = result_name.replace("\n", "")
        
        #get rid of unnecessary spacing
        result_name = result_name.strip()
        
        #format the string
        result_name = result_name + " (Metascore: " + metascore + ")" + "- Category: " + category 
        return result_name
    
    
    '''
    Checks to see if a result name is a part of a valid category
        Parameters:
        result_name represents a formatted search result
    '''
    def _is_valid_category(self, result_name):
        if "<span class=\"title_prefix\">Trailer:</span>" not in result_name:
            if "- Category: Report" not in result_name:
                if "<span class=\"label\">Latest" not in result_name:
                    return True
    
        return False
        