'''
Created on Aug 10, 2021

@author: Jacob Summers
'''

class album_parser(object):
    '''
    Constructor for Album_Parser object
        Parameters:
        html represents the html page of the album on metacritic
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
    Retrieves the name of the album
    '''
    def get_name(self):
        return self.name
     
    
    '''
    Retrieves the summary of the album
    '''
    def get_summary(self):
        return self.summary
    
    '''
    Retrieves credits of the album (record label, genre)
    '''
    def get_credit(self):
        return self.credit
    
    
    '''
    Parses through the html code in order to retrieve the name and artist, date, metascore, and user score 
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
            
            #isolate the section that contains the name of the artist
            start_index = htmlname.find("<span class=\"band_name\"") + len("<span class=\"band_name\"")
            
            htmlname = htmlname[start_index:]
            
            start_index = htmlname.find(">") + len(">")
            
            htmlname = htmlname[start_index:]
            
            end_index = htmlname.find("</span>")
            
            artist = htmlname[:end_index]
            
            artist = artist.strip()
            
            return name + " by " + artist
           
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
        
        
        
        self.name = "Name: " + _parse_name() + "\n"
        
        self.name =  self.name + "Year: " + _parse_year() + "\n"
        
        self.name = self.name + "Metascore: " +  _parse_metascore() + "\n"
        
        self.name = self.name + "User score: " + _parse_score() + "\n"
        
        
            
    '''
    Parses through the html code in order to obtain the summary of the album
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
    Parses through the html in order to get miscellaneous credits such as the record label and genre
    of the album
    '''
    def _obtain_credits(self):
        
        '''
        Inner method that gets the name of the record label
        '''
        def _get_recordlabel():
            #parse the record label
            
            start_index = self.html.find("<li class=\"summary_detail product_company\">") + len("<li class=\"summary_detail product_company\">")
            #the record label is in the record label span class, so isolate it from the rest of the html
            htmlcredits = self.html[start_index:]
            
            start_index = htmlcredits.find("<span class=\"label\">Record Label:</span>") + len("<span class=\"label\">Record Label:</span>")
            
            if (start_index - len("<span class=\"label\">Record Label:</span>") == -1):
                return "N/A"
            
            htmlcredits = htmlcredits[start_index:]
            
            
            end_index = htmlcredits.find("</li>")
            
            
            htmlcredits = htmlcredits[:end_index]
            
            
            #the name of the record label is located within the span tag
            start_index = htmlcredits.find("<span class=\"data\">") + len("<span class=\"data\">")
            htmlcredits = htmlcredits[start_index:]
            
            
            #separate the name from the span that it is located in
            end_index = htmlcredits.find("</span>")
            return htmlcredits[:end_index]
        
        '''
        #Inner method that gets the genres of the album
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
            start_index = htmlcredits.find("<span class=\"data\" itemprop=\"genre\">") + len("<span class=\"data\" itemprop=\"genre\">")
            
            end_index = htmlcredits.find("</span>")
            
            
            genre = "Genre(s):\t" + htmlcredits[start_index:end_index]
            
            end_index = end_index + len("</span>")
            
            #move on to the next genre
            htmlcredits = htmlcredits[end_index:]
            
            #get the starting place of the next genre
            start_index = htmlcredits.find("<span class=\"data\" itemprop=\"genre\">")
            
            #while there are still genres in the code
            while (start_index != -1):
                
                #seperate the current genre from the span tag it is located in
                start_index = start_index + len("<span class=\"data\" itemprop=\"genre\">")
                
                end_index = htmlcredits.find("</span>")
            
                genre = genre + ", " + htmlcredits[start_index:end_index]
            
                end_index = end_index + len("</span>")
                
                #move on to the next genre
                htmlcredits = htmlcredits[end_index:]
            
                #get the starting place of the next genre
                start_index = htmlcredits.find("<span class=\"data\" itemprop=\"genre\">")
            
            return genre
        
        
        
        #call the inner methods in order to get the necessary credits
        self.credit = "Record Label:\t" + _get_recordlabel() + "\n"
        self.credit = self.credit +  _get_genres()
        
        