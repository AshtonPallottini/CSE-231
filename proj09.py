# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 16:16:07 2017

@author: Ashton
"""
##########################################################################
#   Computer Project #9
#   
#   Algortihm
#   Prompt for a file and error check until successfully opened
#   Read file and form a dictionary of words and a list of their lines
#       Omit non-alphabetical words, punctuation, and short words
#   Prompt for words to check for
#       Return None if no common lines or bad input
#       Split words into a list, remove punctuation and make lower-case
#       Grab the set of the first word input
#       Find intersection with all future sets
#   Print out lines in common
#   Prompt if they want to check more
#       Quit on input of "q" or "Q"
##########################################################################

##########################################################################
import sys
def input( prompt=None ):
    if prompt != None:
        print( prompt, end="" )
    aaa_str = sys.stdin.readline()
    aaa_str = aaa_str.rstrip( "\n" )
    print( aaa_str )
    return aaa_str
##########################################################################

import string

def open_file():
    '''Prompts the user to input a file, error checks until a correct
    file is input, then returns the opened file'''
    
    good_input = False
    file_input = input("Input a file:") #Prompts for a file
    
    #Error checks until the file can be opened
    while good_input == False:
        try:
            file_obj = open(file_input, "r")
            break
        except:
            print("Error in Filename")
            file_input = input("Input a file:")
            
    return(file_obj)
    
def read_data(fp):
    '''Reads file, formats the words in the way specified, removes
    short words and non-alphabetic words, and adds the words to a 
    dictionary as keys whith a set of their line occurances as the value.
    fp = file opened for reading
    returns: a dictionary with words as keys and a set of lines as values'''
    
    #Initialize line count and dictionary
    n = 0
    dictionary_words= dict()
    
    for line in fp:
        n += 1 #Counts lines
        
        #Removes punctuation, makes words lowercase, and puts into list
        line = line.lower().strip()
        word_list = line.split()
        word_list = [w.strip(string.punctuation) for w in word_list]
        for word in word_list:
            
            #Removes certain characters from the words
            for ch in word:
                if ch == "-" or ch == "'":
                    ch_spot = word.find(ch)
                    word = word[0:ch_spot]+word[(ch_spot+1):]
            
            #Removes non-alphabetic and one-letter words
            if word.isalpha() == False:
                continue
            if len(word) < 2:
                continue
            
            #Initializes word as key in dictionary and adds set of lines
            #as value
            if word not in dictionary_words:
                dictionary_words[word] = set()
                dictionary_words[word].add(n)
            else:                
                dictionary_words[word].add(n)
        
    return dictionary_words

def find_cooccurance(D, inp_str):
    '''Takes the input and splits it, formats the words like they are in
    the dictionary, checks for if word is in file and returns none if it 
    isn't, grabs the set of lines of the first input word, finds the 
    intersection of this set with all other input words' sets, returns a
    sorted list of this intersection if there is an intersection, returns
    empty sets otherwise
    D = Dictionary of words and sets of their line appearances
    inp_str: A string of words to look for co-occurances for
    Returns:A sorted list of the lines of co-occurance'''
    
    if inp_str != "": #handles inputs of nothing
        
        #Formats words like they are in the dictionary
        words_need = inp_str.lower().split()
        words_need = [w.strip(string.punctuation) for w in words_need]
        for element in words_need:
            for ch in element:
                if ch.isalpha() == False:
                    elem_spot = words_need.index(element) 
                    spot = element.find(ch)
                    element = element[0:spot] + element[(spot + 1):]
                    words_need[elem_spot] = element       
                        
            if element in D.keys():#Makes sure word is in the file
            
                #Sets first set as the first word input's value in the dict
                if words_need.index(element) == 0:
                    set_words_1 = D[words_need[0]]
                    intersection_words = D[words_need[0]]

                #Finds the first set's intersection with other words lines
                else:
                    set_words = D[element]
                    intersection_words = set_words & set_words_1 
            
            #Returns None if word not in file
            else:
                intersection_words = "None"
                break
            
        #Turns the intersections of lines into a sorted list    
        if intersection_words != "None":
            list_intersect = list(intersection_words)
            list_intersect_sort = sorted(list_intersect)
            
        else:#Handles when there is no intersection
            list_intersect_sort = list()
            
    else:#Handles empty inputs
        list_intersect_sort = list()
        
    return list_intersect_sort

def main():
    #Runs functions from above
    file_obj = open_file()
    dict_words = read_data(file_obj)
    
    print()
    input_str = input("Input space-separated words:")#Prompts for words

    while input_str.lower() != "q": #quits for inputs of 'q' or 'Q'
        
        lines_in = find_cooccurance(dict_words, input_str) #Runs function
        
        #Prints out a message with the words we searched for
        list_input = input_str.split()
        occ_message = "The co-occurance for:"
        for x in list_input:
            occ_message += (x.lower() + ", ")
        if occ_message != "The co-occurance for:":
            occ_message = occ_message[0:-2]
        print(occ_message)
        
        #Prints out a message with the lines of co-occurance
        lines = "Lines:"
        for v in lines_in:
            lines += (str(v) + ", ")
        if lines != "Lines:":
            lines = lines[0:-2]
        else:
            lines += " None"
        print(lines)
        print()
        
        #Reprompts for input of words
        input_str = input("Input space-separated words:")
    
    
if __name__ == "__main__":
    main()
    
    
    
    
    
#Questions
#Q1:5
#Q2:2
#Q3:2
#Q4:6
#Q5:7