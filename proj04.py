###########################################################################
#   Computer Project #4

#   Algorithm
#       Print brief description of game
#       Prompt for a input with only spaces and letters
#           Ensure only spaces and letters by removing spaces and checking
#       Format a current as dashes and spaces representing the input
#           Dashes fill spots of letters
#       Prompt for a guess
#           Guesses limited to 6
#           Case doesn't matter in guesses 
#       Ensure guess is only spaces and letters by removing spaces
#       Edit the current so user knows what inputs have worked
#       Keep a running line of what guesses have been made
#           If guess exceeds 2 letters, it must be correct to win.
#                Incorrect guesses are losses in this case
#       If all letters are guessed correctly, the user wins
#       Display closing messages
###########################################################################

#==========================================================================
#import sys
#def input( prompt=None ):
#   if prompt != None
#        print( prompt, end="" ) 
#   aaa_str = sys.stdin.readline() 
#   aaa_str = aaa_str.rstrip( "\n" )
#   print( aaa_str )
#   return aaa_str 
#==========================================================================

#Defines variables used later in the program
k = 0
picks = ""
space = " "

#Welcomes the user and prompts for input
print("Hangman: guess letters until you can guess the whole word or \
phrase.")
#print("")
print("In this game you get six tries.")
print("")
word = input("Enter a word or phrase:")

#Defines variables as the input for later editing with no consequences
phrase = word
further_check = word
spaceless_word = word

#Checks if spaces or numbers or characters are in the word
while spaceless_word.isalpha() == False :    
    
    #Removes spaces from the word
    if space in spaceless_word :
        while space in spaceless_word:
            spotspace = spaceless_word.find(space)
            spaceless_word = spaceless_word[0:spotspace] + \
            spaceless_word[(spotspace + 1):]
    
    #Prints an error for number inputs 
    else:
        print("")
        print("Error. Only letters and spaces allowed.")
        print("")
        word = input("Enter a word or phrase:")
        
        #Defines variables for non-space entries
        phrase = word
        further_check = word
        spaceless_word = word


else:
    
    #Sets a baseline for current when input has spaces for after one space
    if space in further_check:
        spotspace = further_check.find(space)
        length = len(further_check[0:spotspace])
        current = ((length * "-") + space)
        even_further = further_check[(spotspace + 1):]
        
        #Adds to the baseline when input has multiple spaces
        while space in even_further :
            spotspace = even_further.find(space)
            length = len(even_further[0:spotspace])
            current += ( (length * "-") + space)
            even_further = even_further[(spotspace + 1):]
        
        #Defines the current when input has only one space
        else:
            length = len(even_further)
            even_further = "-" * length
            current += even_further
        
    #Defines current when input has no spaces
    else:   
        length = len(phrase)
        current = (length * "-")
    
    #Prints starting information for the player
    print("")
    print("phrase:", phrase)
    print("current:", current)
    print(k, "guesses so far out of 6.")
        
#Repeatedly prompts for guesses when less than six have been made    
while k < 6 :
    print("")
    guess = input("Guess a letter or a word/phrase:")
     
    #Removes spaces from guesses to check for numbers
    while space in guess :
        spaceful_guess = guess
        spotspace = guess.find(space)
        guess = guess[0:spotspace] + guess[(spotspace + 1):]
    
    #Defines a variable when there are no spaces to prevent output error
    else : 
        spaceful_guess = guess

    #Checks for numbers in the spaceless guess
    while guess.isalpha() == False :
        
        #Prints error messages when there are numbers in the guess
        if guess.isalpha() == False and space not in guess:
            print("")
            print("Letters only in guesses.")
            print(k, "guesses so far out of 6.")
            print("")
            guess = input("Guess a letter or a word/phrase:")        
        elif guess.isalpha() == False and space in guess:
            print("")
            print("Letters only in guesses.")
            print(k, "guesses so far out of 6.")
            print("")
            guess = input("Guess a letter or a word/phrase:")        
    
    #Separates guessing into one letter and full phrases
    if len(guess) < 2 :
        
        #Ensures that case doesn't matter
        if guess.lower() in word or guess.upper() in word :
            
            #Ensures guesses that have already been made don't count
            if guess in picks :
                print("")
                print("You already chose that. Repick.")
                guess = input("Guess a letter or a word/phrase:")
        
            #Edits the current when lower case guesses are in the phrase
            while guess.lower() in word :
                spot1 = word.find(guess.lower())
                current = current[0:spot1] + guess.lower() + \
                current[spot1 + 1:] 
                word = word[0:spot1] + "-" + word[(spot1 + 1):]

            #Edits the current when upper case guesses are in the phrase
            while guess.upper() in word :
                spot2 = word.find(guess.upper())
                current = current[0:spot2] + guess.upper() + \
                current[spot2 + 1:] 
                word = word[0:spot2] + "-" + word[(spot2 + 1):]                
            
            #Makes user win and game ends when all letters are guessed
            if current.lower() == phrase.lower() :
                print("")
                print("current:", current)
                print("You won.")
                break             

            #Adds to number of guesses and what picks have been made 
            k += 1
            picks += guess.lower()
            
            #Displays current and how many guesses have been made
            print("")
            print("current:", current)
            print (k, "guesses so far out of 6:", (picks))
                                           
        #Adds to guesses and picks when the letter guess in wrong
        elif guess.lower() not in phrase and guess.upper() \
        not in phrase :
            print("")
            print("Letter not in phrase.")
            print("current", current)
            picks += guess
            k += 1
            print (k, "guesses so far out of 6:", (picks))
            
    #Prints a message and ends game if the user guesses the full phrase right
    else :
        if spaceful_guess.upper() == phrase.upper() \
        or guess.upper() == spaceless_word.upper() :
            print("")
            print("You won.")
            break
        
        #Prints a message and ends game if user guesses the full phrase wrong
        else :
            print("")
            print("You lost.")
            print("Wrong guess of word or phrase.")
            print("The phrase/word was:", phrase)
            break

#Prints a message and ends game if all guesses are used up without winning        
else :
    print("")
    print("You lost.")
    print("The phrase/word was:", phrase)



#Questions
#Q1:6
#Q2:5
#Q3:2
#Q4:7
#Q5:7
    