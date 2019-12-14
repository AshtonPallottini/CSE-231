#########################################################################
#   Computer Project #5
#
#   Algorithm
#       Prompt for a cipher text
#       Remove spaces and punctuation from input
#       Find most common character
#           Find shift from this character to E
#       Convert characters using shift
#           Concatenate these converted characters together
#       Prompt to see if output legible
#           Loop to next common character user says output is not correct
#########################################################################


#========================================================================
#import sys
#def input( prompt=None ):
#    if prompt != None:
#        print( prompt, end="" )
#    aaa_str = sys.stdin.readline()
#    aaa_str = aaa_str.rstrip( "\n" )
#    print( aaa_str )
#    return aaa_str
#========================================================================

    
import string


def get_char(ch,shift):
    """
    Use new alphabet and the shift to find the deciphered letter value
    Use this value and indexing to convert cipher to decipher
    ch: The character in the string being decoded
    shift: The distance from ch to E
    Returns: The deciphered text character
    """
    cipher_text_number = (alphabet.find(ch)  + shift) % 26
    cipher_text_char = alphabet[cipher_text_number]
    return (cipher_text_char)

def get_shift(s,ignore):
    """
    Sets variables max_count and max_character
    s: The string that is being analyzed for shift
    Converts the s to uppercase
    Counts occurences of characters in s
        Sets the maximum character if it has the highest count
    ignore: Characters ignored in finding the maximum
    Calculates shift using the most common character
    Returns: The calcluted shift used for deciphering the text
        
    """
    max_count = 0
    max_character = None
    s_upper = s.upper()    
    for ch in s_upper :
        char_count = s_upper.count(ch)
        if char_count > max_count and ch not in ignore:
            max_count = char_count
            max_character = ch
           
    shift = 5 - (alphabet.find(max_character) + 1)
    return(shift)
    
    
def output_plaintext(s,shift):
    """
    s: the string that is being decrypted
    Converts s to uppercase
    Converts individual characters in s
    Concatenates these characters together
    shift: The distance from ch to E
    Returns: the entire deciphered text
    """
    decipher_text = ""
    s_upper = s.upper()
    for ch in s_upper :
        cipher_text_char = get_char(ch, shift)  
        decipher_text += cipher_text_char 
    return(decipher_text)

def max_character(s,ignore):
    """
    Sets variables max_count and max_character
    s: The string that is being analyzed for shift
    Converts the s to uppercase
    Counts occurences of characters in s
        Sets the maximum character if it has the highest count
    ignore: Characters ignored in finding the maximum
    Returns: The maximum character to be used in the shift and ignore        
    """
    max_count = 0
    max_character = None
    s_upper = s.upper()    
    for ch in s_upper :
        char_count = s_upper.count(ch)
        if char_count > max_count and ch not in ignore:
            max_count = char_count
            max_character = ch            
    return(max_character)
        
def main():
    pass 

if __name__ == "__main__": 
    main()

#Sets the alphabet so that we can search through all uppercase letters    
alphabet = string.ascii_uppercase
 
#Sets variables to be used later
ignore_char = ""     
space = " "
punctuation = ":;,.-'"
end_confirm = False

#Welcomes the user and prompts for input
print("Cracking a Caeser Cypher")
print("")    
cipher_text = input("Input text to decipher:")
print("")

#Sets variables equal to the input that we can manipulate later
test_text = cipher_text
test_text2 = cipher_text

#Ensure we loop until the input is correct
while end_confirm == False : 

    #Removes spaces from the input
    while space in cipher_text :
        space_spot = cipher_text.find(space)
        cipher_text = cipher_text[0:space_spot] + \
        cipher_text[(space_spot + 1):]
                    
    #Removes any punctuation from the input
    while cipher_text.isalpha() == False :
        for ch in cipher_text :
            if ch in punctuation:
                punctuation_spot = cipher_text.find(ch)
                cipher_text = cipher_text[0:punctuation_spot] + \
                cipher_text[(punctuation_spot + 1):]
    
    #Calculates the shift distance using a function
    shift_dist = get_shift(cipher_text, ignore_char)
    
    #Adds the function-found max character to ignore characters
    ignore_char += max_character(cipher_text, ignore_char)

    #Adds the decipher characters together in one string
    decipher_text = ""
    decipher_text += output_plaintext(cipher_text,shift_dist)
    
    #Adds spaces and punctuation back into the deciphered text
    while test_text.isalpha() == False :    
        for ch in test_text :
            if ch.isalpha() == False :
                space_spot = test_text.find(ch)
                test_text = test_text[0:space_spot] + "a" + \
                test_text[(space_spot + 1):]
                decipher_text = decipher_text[0:(space_spot)] + ch + \
                decipher_text[(space_spot):]
            
   #Prints output and checks if it is correct
    print("")
    print (decipher_text)
    print("")    
    print("")
    legible_confirm = input("Is the statement readable in English? \
(yes/no):")
    print("")
    
    #Resets test_text for future loops
    test_text = test_text2
        
    #Ends the loop if the output is correct
    if legible_confirm.lower() == "yes" :
        end_confirm = True
 
        
# Questions 
# Q1: 5 
# Q2: 2 
# Q3: 3 
# Q4: 6 
# Q5: 7