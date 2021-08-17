'''
Created on Aug 9, 2021

@author: Jacob Summers
'''
import textwrap
from webscrape import clear
#views the details of the selected user review
def view_review_detail(review):
    #clears the command line output
    clear()
    print("User:\t" + review.get_name())
    print("\nDate:\t" + review.get_year())
    print("\nScore:\t" + review.get_score())
    print("\nSummary:\n")
    #make sure there are no illegal characters in the summary
    print(textwrap.fill(review.get_summary(), 100).encode("ascii", 'ignore').decode("ascii"))
    print("\n\n" + review.get_helpful())
    
    input("Enter anything to go back")