'''
Created on Aug 9, 2021

@author: Jacob Summers
'''

class game_parser(object):
    '''
    Constructor for Game_Parser object
        Parameters:
        html represents the html page of the movie on metacritic
    '''

    def __init__(self, html):
        
        self.html = html
        self.name = ""
        self.summary = ""
        self.credit = ""
        
        #starts parsing the different aspects of the html page
        self._obtain_name()
        self._obtain_summary()
        self._obtain_credits()
    
    '''
    Retrieves the name of the game
    '''
    def get_name(self):
        return self.name
     
    
    '''
    Retrieves the summary of the game
    '''
    def get_summary(self):
        return self.summary
    
    '''
    Retrieves credits of the game (developer, genre, rating)
    '''
    def get_credit(self):
        return self.credit
    
    
    '''
    Parses through the html code in order to retrieve the name and platform, date, metascore, user score, and other platforms of the game
    '''
    def _obtain_name(self):
        #parse the name of the movie
        def _parse_name():
            #isolate the section that contains the name of the game
            start_index = self.html.find("<div class=\"product_title\">")
            
            htmlname = self.html[start_index:]
            
            #movie name is located within h1 tags, so isolate the name from them
            start_index = htmlname.find("<h1>") + len("<h1>")
            end_index = htmlname.find("</h1>")
            
            name = htmlname[start_index:end_index]
            
            #isolate the section that contains the name of the platform
            start_index = htmlname.find("<span class=\"platform\">") + len("<span class=\"platform\">")
            
            htmlname = htmlname[start_index:]
            
            end_index = htmlname.find("</span>")
            
            htmlname = htmlname[:end_index]
            
            #if there is no link associated with the console
            if (htmlname.find("<a href") == -1):
                end_index = htmlname.find("<")
            
                platform = htmlname[:end_index]
            
                platform = platform.strip()
            #if there is a link associated with the platform
            else:
            
                start_index = htmlname.find(">") + len(">")
                htmlname = htmlname[start_index:]
                
                end_index = htmlname.find("<")
                
                platform = htmlname[:end_index]
                
                platform = platform.strip()
            
            return name + " (" + platform + ")"
           
        ##parse the year
        def _parse_year():
            
            start_index = self.html.find("<span class=\"label\">Release Date:</span>") + len("<span class=\"label\">Release Date:</span>")
            
            
            if (start_index - len("<span class=\"label\">Release Date:</span>") == -1):
                return "TBD"
            
            htmlname = self.html[start_index:]
            #isolate the section that contains the year the movie came out
            #year is located within span tags, so isolate the year from them
            start_index = htmlname.find(">") + len(">")
            
            end_index = htmlname.find("</span>")
            
            
            #self.name =  self.name + "Year: " + htmlname[start_index:end_index] + "\n"
            return htmlname[start_index:end_index]
        
        
        ##parse the metascore
        def _parse_metascore():
            #metascore is located within span class, so isolate the score from the span class
            start_index = self.html.find("<span itemprop=\"ratingValue\">") + len("<span itemprop=\"ratingValue\">")
            if (start_index - len("<span itemprop=\"ratingValue\">") == -1):
                return "TBD"
            
            htmlname = self.html[start_index:]
            
            end_index = htmlname.find("</span>")
            
            metascore = htmlname[:end_index]
           
            return metascore
        
       
        ##parse the user score
        def _parse_score():
            
            start_index = self.html.find("<div class=\"score_summary\">") + len("<div class=\"score_summary\">")
            
            if (start_index - len("<div class=\"score_summary\">") == -1):
                return "TBD"
            
            htmlname = self.html[start_index:]
            
            #user score is located within span class, so isolate the score from the span class
            start_index = htmlname.find("<div class=\"metascore_w user") + len("<div class=\"metascore_w user")
            htmlname = htmlname[start_index:]
            
            start_index = htmlname.find(">") + len(">")
            end_index = htmlname.find("</div>")
            
            return htmlname[start_index:end_index]
        
        #parse the platforms the game is on
        def _parse_platforms():
            #isolate the platforms from everything else
            start_index = self.html.find("Also On:") + len("Also On:")
            
            if (start_index - len("Also On:") == -1):
                return "N/A"
            
            htmlname = self.html[start_index:]
            
            end_index = htmlname.find("</ul>")
            htmlname = htmlname[:end_index]
            
            #get the first platform
            start_index = htmlname.find("class=\"hover_none\">") + len("class=\"hover_none\">")
            end_index = htmlname.find("</a>")
            
            platform = htmlname[start_index:end_index]
            
            htmlname = htmlname[end_index:]
            
            #go to the next platform
            start_index = htmlname.find("class=\"hover_none\">")
            
            while (start_index != -1):
                start_index = start_index + len("class=\"hover_none\">")
                
                htmlname = htmlname[start_index:]
                
                end_index = htmlname.find("</a>")
                
                
                platform = platform + ", " + htmlname[:end_index]
                
                #remove platform from html
                htmlname = htmlname[end_index:]
                
                #go to the next platform
                start_index = htmlname.find("class=\"hover_none\">")
            
            return platform
        
        
        self.name = "Name: " + _parse_name() + "\n"
        self.name =  self.name + "Year: " + _parse_year() + "\n"
        
        self.name = self.name + "Metascore: " +  _parse_metascore() + "\n"
        
        self.name = self.name + "User score: " + _parse_score() + "\n"
        
        self.name = self.name + "Also On: " + _parse_platforms() + "\n" 
        
            
    '''
    Parses through the html code in order to obtain the summary of the game
    '''
    def _obtain_summary(self):
        
        
        start_index = self.html.find("<span class=\"label\">Summary:</span>") + len("<span class=\"label\">Summary:</span>")
        #the summary is contained within <span class="blurb blurb_expanded">, so isolate it from that 
        
        htmlsum = self.html[start_index:]
        
        end_index = htmlsum.find("</li>")
    
        htmlsum = htmlsum[:end_index]
        
        
        start_index = htmlsum.find("<span class=\"blurb blurb_expanded\">") + len("<span class=\"blurb blurb_expanded\">")
        
        
        
        #if the summary is short
        if (start_index - len("<span class=\"blurb blurb_expanded\">") == -1):
            
            start_index = htmlsum.find("<span class=\"data\">") + len("<span class=\"data\">")
            htmlsum = htmlsum[start_index:]
            
            start_index = htmlsum.find(">") + len(">")
            end_index = htmlsum.find("</span>")
            self.summary = "Summary: " + htmlsum[start_index:end_index] + "\n"
            
        
        else:
            htmlsum = htmlsum[start_index:]
        
            end_index = htmlsum.find("</span>")
        
            self.summary = "Summary: " + htmlsum[:end_index] + "\n"
        
        
    
    '''
    Parses through the html in order to get miscellaneous credits such as the developer, genre, and rating
    of the game
    '''
    def _obtain_credits(self):
        
        '''
        Inner method that gets the name of the developer
        '''
        def _get_developer():
            #parse the developer
            #the developer is in the developer span class, so isolate it from the rest of the html
            start_index = self.html.find("<span class=\"label\">Developer:</span>") + len("<span class=\"label\">Developer:</span>")
            
            if (start_index - len("<span class=\"label\">Developer:</span>") == -1):
                return "N/A"
            
            htmlcredits = self.html[start_index:]
            
            #the name of the developer is located within the a href tag of the developer span class
            start_index = htmlcredits.find("<a href=\"/company/") + len("<a href=\"/company/")
            htmlcredits = htmlcredits[start_index:]
            
            #separate the name from the span that it is located in
            start_index = htmlcredits.find(">") + len(">")
            end_index = htmlcredits.find("</a>")
            return htmlcredits[start_index:end_index]
        
        '''
        #Inner method that gets the genres of the game
        '''
        def _get_genres():
        
            #parse the genre(s)
            #the genre is in the genre span class, so isolate it from the rest of the html
            start_index = self.html.find("<span class=\"label\">Genre(s): </span>") + len("<span class=\"label\">Genre(s): </span>")
            htmlcredits = self.html[start_index:]
            
            #isolate the genres from the rest of the html
            end_index = htmlcredits.find("</li>")
            htmlcredits = htmlcredits[:end_index]
            
            
            
            #get the first genre
            start_index = htmlcredits.find("<span class=\"data\" >") + len("<span class=\"data\" >")
            
            end_index = htmlcredits.find("</span>")
            
            
            genre = "Genre(s):\t" + htmlcredits[start_index:end_index]
            
            end_index = end_index + len("</span>")
            
            #move on to the next genre
            htmlcredits = htmlcredits[end_index:]
            
            #get the starting place of the next genre
            start_index = htmlcredits.find("<span class=\"data\" >")
            
            #while there are still genres in the code
            while (start_index != -1):
                
                #seperate the current genre from the span tag it is located in
                start_index = start_index + len("<span class=\"data\" >")
                
                end_index = htmlcredits.find("</span>")
            
                genre = genre + ", " + htmlcredits[start_index:end_index]
            
                end_index = end_index + len("</span>")
                
                #move on to the next genre
                htmlcredits = htmlcredits[end_index:]
            
                #get the starting place of the next genre
                start_index = htmlcredits.find("<span class=\"data\" >")
            
            return genre
        
        
        '''
        #Inner method that gets the rating of the game
        '''
          
        def _get_rating():
            #parse the rating
            #the rating is in the rating span class, so isolate it from the rest of the html
            start_index = self.html.find("<span class=\"label\">Rating:</span>") + len("<span class=\"label\">Rating:</span>")
            htmlcredits = self.html[start_index:]
            
            
            #get the rating that is contained in the span tag 
            start_index = htmlcredits.find("<span class=\"data\" >") + len("<span class=\"data\" >")
            
            end_index = htmlcredits.find("</span>")
            
            rating = htmlcredits[start_index:end_index]
            
            
            return rating
        
        
        #call the inner methods in order to get the necessary credits
        self.credit = "Developer:\t" + _get_developer() + "\n"
        self.credit = self.credit +  _get_genres()
        self.credit = self.credit + "\n" + "Rating:\t\t" + _get_rating()
        