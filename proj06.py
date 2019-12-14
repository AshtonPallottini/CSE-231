# -*- coding: utf-8 -*-

##########################################################################
#   Computer Project #6
#
#   Algorithm
#       Print Warning message on punishments for hacking
#       Prompt for type of hacking
#           Quits if input is 'q'
#           Uses dictionary hacking for input of 'dictionary'
#               Prompts for input of dictionary to use 
#                   Loops until valid input
#               Prompts for zip file input
#                   Loops until valid input
#               Uses dictionary passwords to try opening the zip file
#               Prints time and correct password
#               Reprompts for type of hacking and loops if not 'q'
#           Uses brute force if input is 'brute force'
#               Prompts for zip file to use
#                   Loops until valid input
#               Checks for password using permutations of letters
#               Prints time and correct password
#           Uses dictionary then brute force if input is 'both'
#               Only prints dictionary results if dictionary find password
#               Prints both results if brute force needs to be used
#           Loops until input is 'q'
##########################################################################

#=========================================================================
#import sys  
#def input( prompt=None ):          
#    if prompt != None:                  
 #       print( prompt, end="" )          
  #  aaa_str = sys.stdin.readline()          
   # aaa_str = aaa_str.rstrip( "\n" )          
    #print( aaa_str )          
    #return aaa_str
#=========================================================================


import zipfile
import time
import string
from itertools import permutations

#Defines variables and sets our alphabet for later
n = 1
x = 0
alphabet = string.ascii_lowercase
password_found = False

#Prints welcome message and warning
print("Cracking Zip Files")
print("Warning: cracking passwords is illegal due to the Computer \
Fraud and Abuse Act and has a maximum prison term of 20 years.")

#Prompts for input on what method to use
print("")
used_method = input("Which Method ('brute force','dictionary',\
'both','q'):")


while used_method != "q":
    if used_method == "dictionary":
        
        #Reiterates what type is being used
        print("")
        print("Dictionary Cracking")
        print("")

        #Defines variable used in looping until input is good
        good_dic_input = False
        
        #Prompts for dictionary input
        dictionary_input = input("Enter dictionary file name:")        
        
        #Reprompts until the dictionary input is valid
        while good_dic_input == False:           
            try:
                dictionary_used = open(dictionary_input, "r")
                break
            except:
                print("")
                dictionary_input = input("Enter dictionary file name:")

        #Prompts for a zip file input
        print("")        
        zip_file_in = input("Enter zip file name:")
        print("")
        
        #Starts clock to find time
        start = time.process_time()
        
        #Runs through all lines until correct password is found
        for line in dictionary_used:
            
            #Cleans up the lines for reading
            line_stripped = line.strip()

            #Defines variable used in looping until input is good            
            good_zip_input = False
            
            #Reprompts until the zip file input is valid
            while good_zip_input == False:
                try:
                    zip_file = zipfile.ZipFile(zip_file_in)
                    good_zip_input = True
                except:
                    zip_file_in = input("Enter zip file name:")  
                    print("")
                    
            #Attempts passwords for the file and prints the right one        
            try:  
                zip_file.extractall(pwd = line_stripped.encode())
                print("")
                print("Dictionary password is:", line_stripped)
                
                #Ends clock, calculates time that passed and prints
                end = time.process_time()
                time_elapsed = round((end-start), 4)
                print("Elapsed time (sec):", time_elapsed)
                dictionary_used.close()
                print("")
                
                #Prompts for next method to use
                used_method = input("Which Method ('brute force',\
'dictionary','both','q'):")
                break
            
            #Continues to next line if error with previous one
            except:
                continue
    
    
    elif used_method == "brute force":
        
        #Reiterates what type is being used
        print("")
        print("Brute Force Cracking")
        
        #Defines variable used in looping until input is good
        good_zip_input = False
        
        #Prompts for a zip file input
        print("")
        zip_file_in = input("Enter zip file name:")
        print("")
              
        #starts clock to find time
        start_brute = time.process_time()        
        
        #Runs through letter permutations shorter than 27 in length        
        while n <= len(alphabet):
            for items in permutations(alphabet, n):
                
                #Reprompts until the zip file input is valid
                try:
                    while good_zip_input == False:
                        try:
                            zip_file = zipfile.ZipFile(zip_file_in)
                            good_zip_input = True
                        except:
                            zip_file_in = input("Enter zip file name:")
                    
                    #Keeps track of number of permutations gone through       
                    x += 1                
                    zip_file = zipfile.ZipFile(zip_file_in)
                    
                    #Forms passwords from permutations and tries them
                    password_brute = "".join(items)
                    zip_file.extractall(pwd = password_brute.encode())
                    
                    #Prints correct password, stops clock, and prints time 
                    print("Password is:", password_brute)
                    end_brute = time.process_time()
                    time_elapsed_brute = round((end_brute - \
                                                start_brute), 4)
                    print("Elapsed time (sec):", time_elapsed_brute)
                    print("")
                    
                    #Prompts for next method to use
                    used_method = input("Which Method ('brute force',\
'dictionary','both','q'):")
                    break
                
                #Goes to next permutation of certain length
                except:
                    if x <= 24:
                        continue
                    
                    #Increases length of permutations used
                    else:
                        n += 1
                        continue

                    
                    
    elif used_method == "both":
        
        #Reiterates what type is being used
        print("")
        print("Both Attacks.")
        print("")
        
        #Defines variable used in looping until input is good
        good_dic_input = False        
        
        #Prompts for dictionary input
        dictionary_input = input("Enter dictionary file name:")
        print("")    
        
        #Reprompts until the dictionary input is valid
        while good_dic_input == False:             
            try:
                dictionary_used = open(dictionary_input, "r")
                break
            except:
                dictionary_input = input("Enter dictionary file name:")
                print("")
        
        #Defines variable used in looping until input is good        
        good_zip_input = False
        
        #Prompts for zip file input
        zip_file_in = input("Enter zip file name:")
        print("")
        
        #starts clock to find time
        start = time.process_time()
        
       #Runs through all lines until correct password is found 
        for line in dictionary_used:
            line_stripped = line.strip()
            
           #Reprompts until the zip file input is valid 
            while good_zip_input == False: 
                    try:
                        zip_file = zipfile.ZipFile(zip_file_in)
                        good_zip_input = True
                    except:
                        zip_file_in = input("Enter zip file name:")
                        print("")
            
            #Attempts passwords for the file and prints the right one            
            try:
                zip_file.extractall(pwd = line_stripped.encode())
                print("Dictionary password is:", line_stripped)
                
                #Ends clock, calculates and prints time elapsed
                end = time.process_time()
                time_elapsed = round((end-start), 4)
                print("Elapsed time (sec):", time_elapsed)
                dictionary_used.close()
                
                #Reprompts for next method if password found
                print("")
                used_method = input("Which Method ('brute force',\
'dictionary','both','q'):")
                
                #Makes sure brute force not used unnecessarily
                password_found = True
                break
            
            #Continues to next line if previous one incorrect
            except:
                continue  
        
        #Prints message and time if dictionary didn't work    
        if password_found == False :    
            print("No Password Found.")
            end = time.process_time()
            dict_time_elapsed = round((end-start), 4)
            print("Dictionary elapsed time (sec):", dict_time_elapsed)
        
            #Runs through letter permutations shorter than 27 in length
            while n <= len(alphabet):
                #starts clock to find time
                start_brute = time.process_time()                
                
                for items in permutations(alphabet, n):
                    try:
                        
                        #Keeps track of number of permutations gone through
                        x += 1                
                        zip_file = zipfile.ZipFile(zip_file_in)
                        
                        #Forms passwords from permutations and tries them
                        password_brute = "".join(items)
                        zip_file.extractall(pwd = password_brute.encode())
                        
                        #Prints correct password, stops clock, and prints time
                        print("Brute Force password is:", password_brute)
                        end_brute = time.process_time()
                        time_elapsed_brute = round((end_brute - \
                                                    start_brute), 4)
                        print("Brute Force elapsed time (sec):"\
                              , time_elapsed_brute)
                        print("")
                        
                        #Prompts for next method to use
                        used_method = input("Which Method (\
'brute force','dictionary','both','q'):")
                        break
                    
                    #Goes to next permutation of certain length
                    except:
                        if x <= 24:
                            continue
                        
                        #Increases length of permutation used
                        else:
                            n += 1
                            continue   