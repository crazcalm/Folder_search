"""
Coded by Marcus Willock :)
"""

import os

def info():
    
    """
    Asks the user for the Keyword that they want to look up and the number of results that
    they want this program to return.
    """
    
    lookup = raw_input("Write the name of the file that you want to search for: ")
    
    num_of_results = -1
    
    # A loop to ensure that the number of results wanted in an integer greater than zero
    while num_of_results <= 0:
        
        try:
            num_of_results = int(raw_input("Write the number of results that you want to search for (integer greater than 0): "))
        
        except ValueError:
            print "That is not a valid number for this search."
    # Returns both the Keyword to lookup and the number of results wanted
    return lookup, num_of_results


def print_results(results):
    
    """
    Prints both the number of results and the results of the search.
    """
    
    print "\nThere are", len(results), "results:"
    
    for x in results:
        print "\n", x


def main():
    
    """
    Searches through the directories on your computer and finds the directories with
    the your Keyword in their path name. 
    """
    
    # I start the search at C:\Users\crazcalm.
    # Change the directory to widen or narrow the search
    search_start = "C:\\Users\\crazcalm"
    results = [] 
    
    lookup, num_of_results = info()
    
    # A loop to walk through the directories that branch off from
    # our tree (the starting directory)
    for root in os.walk(search_start):
        
        """
        The root is a tuple and the first entry in this tuple is the 
        path name.
        
        We split the path name by "\" and then check to see if any of
        the words in the path name match out Keyword.
        """
        dir = root[0]
        dir_words = dir.split("\\")
        
        for word in dir_words:
            
            # Makes eveything lowercase so we do not have to worry
            # about case sensitivity.
            if word.lower() == lookup.lower():
                
                # Puts our findings into the result list
                results.append(dir)
                break
        
        # If we reach the desired number of results, we end the search
        # and show the results to the user.    
        if len(results) >= num_of_results:
            print_results(results)
            break
        
    # If we do not reach the desired number of results, we show the
    # user what we have found.    
    if len(results) < num_of_results:
        print_results(results)
        
        
if __name__ == '__main__':
    main()
