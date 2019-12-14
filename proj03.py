############################################################################
#   Computer Project #3
#
#   Algorithm
#       Prompt for an input of cash
#           If negative, display error and reprompt
#       Prompt for a payment
#           If not enough, repropmpt    
#           If just enough, display "No Change"
#           If more than enough, give change using the fewest coins possible
#               Coins are not replaced after usage
#       Continuously reprompt for inputs and payments
#           Break from the program if change can't be made
#       Print remaining stock 
############################################################################

#==============================================================================
# This code is used by the testing framework.  Uncomment when you want to 
# execute the run_file.py testing program.  This code replace the input
# function so the input from the test.txt file appears in the output.txt file.
#
#import sys
#def input( prompt=None ):
#    if prompt != None:
#        print( prompt, end="" )
#    aaa_str = sys.stdin.readline()
#    aaa_str = aaa_str.rstrip( "\n" )
#    print( aaa_str )
#    return aaa_str
#empty_stock = False
#==============================================================================

#Defines a variable we use later and sets beginning stock
empty_stock = False
pennies = 10
nickels = 10
dimes = 10
quarters = 10

#Welcomes the user and prompts for a price
print("\nWelcome to change-making program.")
in_str = input("Enter the purchase price (xx.xx) or `q' to quit: ")

#Allows the program to end on input of q
while in_str.lower() != 'q':
    
    #Splits input price to dollars and cents and makes them integers
    dollar_str, cents_str = in_str.split(".")
    dollar = int(dollar_str)
    cents = int(cents_str)

    #Prints an error and reprompts when input price is negative
    if dollar < 0 or cents < 0:
        print("Only positive amounts please.")
        in_str = input("Enter the purchase price (xx.xx) or `q' to quit: ")
    
    #Prompts for a payment
    payment_str = input("Enter your payment (int):")
    
    #Reprompts if the payment is insufficient
    if float(in_str) > float(payment_str) :
        print("Insufficient payment. Try again please.")
        payment_str = input("Enter your payment (int):")   
        
        #Splits input into dollars and cents and makes them integers
        dollar_str, cents_str = in_str.split(".")
        dollar = int(dollar_str)
        cents = int(cents_str)
        
        #Continues with program once payment is enough
        if float(in_str) < float(payment_str) :
            
            #Makes payment an integer and calculates change in cents
            pdollar = int(payment_str)   
            change = ((100 * (pdollar - dollar)) - cents)
            
            #Defines variables used to count coins used up
            v = 0
            x = 0
            y = 0
            z = 0
            
            #Uses quarters to make change while possible
            while (change - 25) >= 0 and quarters > 0 :
                change -= 25
                quarters -= 1
                v += 1
            
            #Uses dimes to make change while possible   
            while (change - 10) >= 0 and dimes > 0:
                change -= 10
                dimes -= 1
                x += 1
            
            #Uses nickels to make change while possible    
            while (change - 5) >= 0 and nickels > 0:
                change -= 5
                nickels -= 1
                y += 1
            
            #Uses pennies to make change while possible    
            while (change - 1) >= 0 and pennies > 0:
                change -= 1
                pennies -= 1 
                z += 1
            
            #Prints an error when we can't make enough change    
            if change > (25*quarters + 10*dimes + 5*nickels \
                         + 1*pennies) :
                print("We can't make that change")
                
                #Breaks out of the loop and stops printing of end messages
                empty_stock = True
                break 
         
            #Prints coins you receive, omits showing coins you don't
            print("")
            if v != 0 : 
                print("You get:", v, "quarters")
            if x != 0 :
                print("You get:", x, "dimes")
            if y != 0 :
                print("You get:", y, "nickels")
            if z != 0 :
                print("You get:", z, "pennies")

            #Prints how many coins you receive and remaining stock
            print("Stock:", quarters, "quarters left,", dimes, \
            "dimes left,", nickels, "nickels left,", pennies, \
            "pennies left") 
                            
    #Runs through program when initial payment is enough
    elif float(in_str) < float(payment_str) :     
       
        #Makes payment an integer and calculates change
        pdollar = int(payment_str)   
        change = ((100 * (pdollar - dollar)) - cents)
        
        #Defines variable later used to count coins used so far
        v = 0
        x = 0
        y = 0
        z = 0
        
        #Uses quarters to make change while possible
        while (change - 25) >= 0 and quarters > 0 :
            change -= 25
            quarters -= 1
            v += 1
            
        #Uses dimes to make change while possible
        while (change - 10) >= 0 and dimes > 0:
            change -= 10
            dimes -= 1
            x += 1
            
        #Uses nickels to make change while possible
        while (change - 5) >= 0 and nickels > 0:
            change -= 5
            nickels -= 1
            y += 1
            
        #Uses pennies to make change while possible
        while (change - 1) >= 0 and pennies > 0:
            change -= 1
            pennies -= 1 
            z += 1
            
        #Prints an error when we can't make enough change
        if change > (25*quarters + 10*dimes + 5*nickels + \
                     1*pennies) :
            print("We can't make that change")
            
            #Breaks out of the loop and prevents printing the end messages
            empty_stock = True
            break 
        
        #Prints coins you receive, omits showing coins you don't
        print("")
        if v != 0 : 
            print("You get:", v, "quarters")
        if x != 0 :
            print("You get:", x, "dimes")
        if y != 0 :
            print("You get:", y, "nickels")
        if z != 0 :
            print("You get:", z, "pennies")

        #Prints how many coins you receive and remaining stock 
        print("Stock:", quarters, "quarters left,", dimes, \
        "dimes left,", nickels, "nickels left,", pennies, \
        "pennies left")
    
    #Prints no change when an exactly correct payment is made        
    else :
        print("No change.")
        
    #Reprompts for an input to reloop through the program
    in_str = input("Enter the purchase price (xx.xx) or `q' to quit: ")

#Prints remaining stock only when we were able to make all change necessary
if empty_stock != True :    
    print("")
    print(quarters, "quarters left,", dimes, "dimes left,",\
          nickels, "nickels left,", pennies, "pennies left")
    print('remaining stock:{:.2f}'.format(.25 * quarters + \
          .1 * dimes + .05 * nickels + .01 * pennies)) 
    
    

# Questions 
# Q1: 6 
# Q2: 4 
# Q3: 3 
# Q4: 7 
# Q5: 7