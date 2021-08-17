'''
Created on Aug 8, 2021

@author: Jacob Summers
'''

'''
Represents the object that parses information about a user review from the given html code
'''
class movie_review(object):
    

    '''
    Constructor for the Movie_Review object
        Parameters:
        html represents the html code of a given user review
    '''
    def __init__(self, html):
        
        #represents the html code that contains the user review information
        self.html = html
        #represents the date that the review was published
        self.year = ""
        #represents the score that the user gave
        self.score = 0
        #represents the name of the user
        self.name = ""
        #represents the summary that the user gave
        self.summary = ""
        #represents how many people found the review helpful
        self.helpful = ""
        
        #begins parsing the information
        self._begin_parse()
    '''
    Prints the object as a formatted string
    '''
    def to_string(self):
        return "Score of " + self.get_score() + " -- User: " + self.get_name() + " -- Date: " + self.get_year() + " -- " + self.get_helpful()
    
    '''
    Gets the date of the user's review
    '''  
    def get_year(self):
        return self.year
    
    '''
    Gets the score that the user gave
    ''' 
    def get_score(self):
        return self.score
    
    '''
    Gets the name of the user who made the review
    ''' 
    def get_name(self):
        return self.name
    
    '''
    Gets the detailed summary of the user's review
    ''' 
    def get_summary(self):
        return self.summary
    
    '''
    Gets the number of people who found the review helpful
    ''' 
    def get_helpful(self):
        return self.helpful
    
    '''
    Parses the review information from the html code
    ''' 
    def _begin_parse(self):
        
        '''
        Parses the date that the review was made
        '''
        def parse_year():
            #get the index where the date is located
            start_index = self.html.find("<span class=\"date\">") + len("<span class=\"date\">")
            html = self.html[start_index:]
            
            end_index = html.find("<")
            
            #isolate it from the rest of the code
            year = html[:end_index]
            
            return year
        '''
        Parses the score that the user gave in the review
        '''
        def parse_score():
            
            #get the index where the score is located in the review
            start_index = self.html.find("<div class=\"metascore_w user") + len("<div class=\"metascore_w user")
            html = self.html[start_index:]
            
            start_index = html.find(">") + len(">")
            end_index = html.find("</div>")
            
            #isolate it from the rest of the html code
            score = html[start_index:end_index]            
            
            
            return score
        
        '''
        Parses the name of the user in the review
        '''
        def parse_name():
            
            #get the index where the user's name is located
            start_index = self.html.find("<a href=") + len("<a href=")
           
            html = self.html[start_index:]
            
            start_index = html.find(">") + len(">")
            end_index = html.find("<")
            
            #isolate it from the rest of the code
            name = html[start_index:end_index]
            
            return name
        '''
        Parses the text summary of the user's review
        '''
        def parse_summary():
            #isolate the summary from the rest of the user code
            start_index = self.html.find("<div class=\"summary\">") + len("<div class=\"summary\">")
            html = self.html[start_index:]
            end_index = html.find("</div>")
            html = html[:end_index]
            
            #the summary is contained within <span class="blurb blurb_expanded"> if it can be expanded
            start_index = html.find("<span class=\"blurb blurb_expanded\">") + len("<span class=\"blurb blurb_expanded\">")
            
            #if the summary isn't expanded
            if (start_index - len("<span class=\"blurb blurb_expanded\">") == -1):
                
                start_index = html.find("div class=\"review_body\">") + len("div class=\"review_body\">")
                html = html[start_index:]
                #contained with span tags
                start_index = html.find("<span>") + len("<span>")
                end_index = html.find("</span>")
                
                #isolate the summary from the rest of the html code
                summary = html[start_index:end_index]
                
                #remove excess whitespace from both sides
                summary = summary.strip()
                return summary
            
            html = html[start_index:]
        
            end_index = html.find("</span>")
            #isolate it from the rest of the html code
            summary = html[:end_index]
            
            return summary
        
        '''
        Parses the number of people that found the review helpful
        '''
        def parse_helpful():
            
            #find the count of people who found the review helpful
            start_index = self.html.find("<span class=\"yes_count\">") + len("<span class=\"yes_count\">")
            html = self.html[start_index:]
            
            end_index = html.find("</span>")
            #isolate it from the rest of the code and put it in a variable
            yescount = html[:end_index]
            
            #find the total count of users who found it helpful or not
            start_index = html.find("<span class=\"total_count\">") + len("<span class=\"total_count\">")
            html = html[start_index:]
            
            end_index = html.find("</span>")
            
            #isolate it from the rest of the code and put it in a variable
            totalcount = html[:end_index]
            
            
            #combine the two counts together into a formatted string
            return yescount + " of " + totalcount + " users found this helpful"
    
    
        #call the inner methods in order to parse the specific values and assign them to the instance variables
        self.year = parse_year()
        self.score = parse_score()
        self.name = parse_name()
        self.summary = parse_summary()
        self.helpful = parse_helpful()