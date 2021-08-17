'''
Created on Aug 7, 2021

@author: Jacob Summers
'''

'''
Represents the object that parses the metacritic html page of a movie
'''
class movie_parser(object):
   
    '''
    Constructor for Movie_Parser object
        Parameters:
        html represents the html page of the movie on metacritic
    '''

    def __init__(self, html):
        
        self.html = html
        self.name = ""
        self.cast = ""
        self.summary = ""
        self.credit = ""
        
        #starts parsing the different aspects of the html page
        self._obtain_name()
        self._obtain_cast()
        self._obtain_summary()
        self._obtain_credits()
    
    '''
    Retrieves the name of the movie
    '''
    def get_name(self):
        return self.name
   
    '''
    Retrieves the names of the cast
    '''    
    def get_cast(self):
        return self.cast   
    
    '''
    Retrieves the summary of the movie
    '''
    def get_summary(self):
        return self.summary
    
    '''
    Retrieves credits of the movie (director, genre, rating, runtime)
    '''
    def get_credit(self):
        return self.credit
    
    
    '''
    Parses through the html code in order to retrieve the name, year, metascore, and user score of the movie
    '''
    def _obtain_name(self):
        #parse the name of the movie
        #isolate the section that contains the name of the movie
        start_index = self.html.find("<div class=\"product_page_title oswald\">")
        
        htmlname = self.html[start_index:]
        
        #movie name is located within h1 tags, so isolate the name from them
        start_index = htmlname.find("<h1>") + len("<h1>")
        end_index = htmlname.find("</h1>")
        
        self.name = "Name: " + htmlname[start_index:end_index] + "\n"
        
        ##parse the year
        
        #isolate the section that contains the year the movie came out
        #year is located within span tags, so isolate the year from them
        start_index = htmlname.find("<span class=\"release_year lighter\">") + len("<span class=\"release_year lighter\">")
        end_index = htmlname.find("</span>")
        
        self.name =  self.name + "Year: " + htmlname[start_index:end_index] + "\n"
        
        
        
        ##parse the metascore
        #metascore is located within span class, so isolate the score from the span class
        start_index = htmlname.find("<span class=\"metascore_w") + len("<span class=\"metascore_w")
        htmlname = htmlname[start_index:]
        
        start_index = htmlname.find(">") + len(">")
        end_index = htmlname.find("</span>")
        
        self.name = self.name + "Metascore: " +  htmlname[start_index:end_index] + "\n"
        
        
        ##parse the user score
        #user score is located within span class, so isolate the score from the span class
        start_index = htmlname.find("<span class=\"metascore_w user") + len("<span class=\"metascore_w user")
        htmlname = htmlname[start_index:]
        
        start_index = htmlname.find(">") + len(">")
        end_index = htmlname.find("</span>")
        
        self.name = self.name + "User score: " +  htmlname[start_index:end_index] + "\n"
        
    
    
    '''
    Parses through the html code in order to obtain the cast list of the movie
    '''
    def _obtain_cast(self):
    
    #if there is a starring label in the html
        if (self.html.find("<span class=\"label\">Starring:</span>") != -1):
            #get to first person
            start_index = self.html.find("<a href=\"/person/")
            htmlcast = self.html[start_index:]
            
            #remove the rest of the html that doesn't involve the cast
            end_index = htmlcast.find("</span>")
            htmlcast = htmlcast[:end_index]
            
            #isolate the first person from the a tag it is in
            start_index = htmlcast.find(">") + len(">")
            end_index = htmlcast.find("</a>")
            
            self.cast = "Cast: " + htmlcast[start_index:end_index]
            
            
            #remove the cast member from html
            end_index = end_index + len("</a>")
            htmlcast = htmlcast[end_index:]
            
            
            #move on to parse the next person in the list
            start_index = htmlcast.find("<a href=\"/person/")
            
            #have a count that adds a new space every 5 people
            count = 1
            newline = ""
            
            #while there are still people in the list
            while (start_index != -1):
                
                #add a new line every 5 people
                if (count == 5):
                    newline = "\n"
                    count = 0
                
                #start parsing the current person
                htmlcast = htmlcast[start_index:]
                
                #isolate the person from the a tag
                start_index = htmlcast.find(">") + len(">")
                end_index = htmlcast.find("</a>")
                
                
                count = count + 1
                self.cast = self.cast + ", " + newline + htmlcast[start_index:end_index]
                
                newline = ""
                
                #remove cast member from html
                end_index = end_index + len("</a>")
                #move on to the next person
                htmlcast = htmlcast[end_index:]
                
                start_index = htmlcast.find("<a href=\"/person/")
        else:
            self.cast = "Cast: N/A"
            
    '''
    Parses through the html code in order to obtain the summary of the movie
    '''
    def _obtain_summary(self):
        
        start_index = self.html.find("<span class=\"label\">Summary:</span>") + len("<span class=\"label\">Summary:</span>")
        #the summary is contained within <span class="blurb blurb_expanded">, so isolate it from that 
        
        htmlsum = self.html[start_index:]
        
        end_index = htmlsum.find("</div>")
    
        htmlsum = htmlsum[:end_index]
        
        
        start_index = htmlsum.find("<span class=\"blurb blurb_expanded\">") + len("<span class=\"blurb blurb_expanded\">")
        
        
        
        #if the summary is short
        if (start_index - len("<span class=\"blurb blurb_expanded\">") == -1):
            
            start_index = htmlsum.find("<span>") + len("<span>")
            htmlsum = htmlsum[start_index:]
            start_index = htmlsum.find("<span>") + len("<span>")
            htmlsum = htmlsum[start_index:]
            
            end_index = htmlsum.find("</span>")
            self.summary = "Summary: " + htmlsum[:end_index] + "\n"
            
        
        else:
            htmlsum = htmlsum[start_index:]
        
            end_index = htmlsum.find("</span>")
        
            self.summary = "Summary: " + htmlsum[:end_index] + "\n"
        
    
    '''
    Parses through the html in order to get miscellaneous credits such as the director, genre, rating, and runtime
    of the movie
    '''
    def _obtain_credits(self):
        
        '''
        Inner method that gets the name of the director
        '''
        def _get_director():
            #parse the director
            #the director is in the director div class, so isolate it from the rest of the html
            start_index = self.html.find("<div class=\"director\">")
            htmlcredits = self.html[start_index:]
            
            #the name of the director is located within the a href tag of the director div class
            start_index = htmlcredits.find("<a href=\"/person/")
            htmlcredits = htmlcredits[start_index:]
            
            #separate the name from the span that it is located in
            start_index = htmlcredits.find("<span>") + len("<span>")
            end_index = htmlcredits.find("</span>")
            return htmlcredits[start_index:end_index]
        
        '''
        Inner method that gets the genres of the movie
        '''
        def _get_genres():
        
            #parse the genre(s)
            #the genre is in the genre div class, so isolate it from the rest of the html
            start_index = self.html.find("<div class=\"genres\">")
            htmlcredits = self.html[start_index:]
            
            #get the different genres isolated
            start_index = htmlcredits.find("<span>") + len("<span>")
            
            end_index = htmlcredits.find("</div>")
            
            htmlcredits = htmlcredits[start_index:end_index]
            
            #get the first genre
            start_index = htmlcredits.find("<span>") + len("<span>")
            
            end_index = htmlcredits.find("</span>")
            
            genre = "Genre(s):\t" + htmlcredits[start_index:end_index]
            
            end_index = end_index + len("</span>")
            
            #move on to the next genre
            htmlcredits = htmlcredits[end_index:]
            
            #get the starting place of the next genre
            start_index = htmlcredits.find("<span>")
            
            #while there are still genres in the code
            while (start_index != -1):
                
                #seperate the current genre from the span tag it is located in
                start_index = start_index + len("<span>")
                
                end_index = htmlcredits.find("</span>")
            
                genre = genre + ", " + htmlcredits[start_index:end_index]
            
                end_index = end_index + len("</span>")
                
                #move on to the next genre
                htmlcredits = htmlcredits[end_index:]
            
                #get the starting place of the next genre
                start_index = htmlcredits.find("<span>")
            
            return genre
        
        
        '''
        Inner method that gets the rating of the movie
        '''
        def _get_rating():
            #parse the rating
            #the rating is in the rating div class, so isolate it from the rest of the html
            start_index = self.html.find("<div class=\"rating\">")
            htmlcredits = self.html[start_index:]
            
            #get the rating that is contained in the span tag within the div
            start_index = htmlcredits.find("<span>") + len("<span>")
            
            end_index = htmlcredits.find("</div>")
            
            htmlcredits = htmlcredits[start_index:end_index]
            
            rating = htmlcredits[:htmlcredits.find("</span>")]
            
            return rating
        
        '''
        Inner method that gets the runtime of the movie
        '''
        def _get_runtime():
            #parse the runtime
            #the runtime is in the runtime div class, so isolate it from the rest of the html
            start_index = self.html.find("<div class=\"runtime\">")
            htmlcredits = self.html[start_index:]
            
            #get the runtime that is contained in the span tag within the div
            start_index = htmlcredits.find("<span>") + len("<span>")
            
            end_index = htmlcredits.find("</div>")
            
            htmlcredits = htmlcredits[start_index:end_index]
            
            time = htmlcredits[:htmlcredits.find("</span>")]
            
            return time
        
        
        #call the inner methods in order to get the necessary credits
        self.credit = "Director:\t" + _get_director() + "\n"
        self.credit = self.credit +  _get_genres()
        self.credit = self.credit + "\n" + "Rating:\t\t" + _get_rating().strip()
        self.credit = self.credit + "\n" + "Runtime:\t" + _get_runtime()
        
    
        
        