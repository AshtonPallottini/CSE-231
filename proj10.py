###########################################################################
#   Computer Project #7
#
#   Algorithm
#       Initialize and print out deck of cards in eight tableaus
#       Initialize four cells and four foundations
#       Prompt for a move
#           Print error and reprompt if move or input invalid
#           Move cards amongst cells, tableaus, foundations based off input
#       Reprompt for a move until all cards in foundations
###########################################################################
import cards

BANNER = """
    __        _____ _   _ _   _ _____ ____  _ _ _ 
    \ \      / /_ _| \ | | \ | | ____|  _ \| | | |
     \ \ /\ / / | ||  \| |  \| |  _| | |_) | | | |
      \ V  V /  | || |\  | |\  | |___|  _ <|_|_|_|
       \_/\_/  |___|_| \_|_| \_|_____|_| \_(_|_|_)

"""


RULES = """
     ____        _             _        ____
    | __ )  __ _| | _____ _ __( )___   / ___| __ _ _ __ ___   ___
    |  _ \ / _` | |/ / _ \ '__|// __| | |  _ / _` | '_ ` _ \ / _ \\
    | |_) | (_| |   <  __/ |    \__ \ | |_| | (_| | | | | | |  __/
    |____/ \__,_|_|\_\___|_|    |___/  \____|\__,_|_| |_| |_|\___|

    Cells:       Cells are numbered 1 through 4. They can hold a
                 single card each.

    Foundations: Foundations are numbered 1 through 4. They are
                 built up by rank from Ace to King for each suit.
                 All cards must be in the foundations to win.

    Tableaus:    Tableaus are numbered 1 through 8. They are dealt
                 to at the start of the game from left to right
                 until all cards are dealt. Cards can be moved one
                 at a time from tableaus to cells, foundations, or
                 other tableaus. Tableaus are built down by rank
                 and cards must be of the same suit.

"""


MENU = """

    Game commands:
    
    TC x y    Move card from tableau x to cell y
    TF x y    Move card from tableau x to foundation y
    TT x y    Move card from tableau x to tableau y
    CF x y    Move card from cell x to foundation y
    CT x y    Move card from cell x to tableau y
    R         Restart the game with a re-shuffle
    H         Display this menu of commands
    Q         Quit the game
    
"""
   
     
def valid_fnd_move(src_card, dest_card):
    """
    Checks to see if a card can legally be moved to a foundation. Only
    allowed if source is ace and destination is empty, or if source is
    same suit and one higher than destination.
    src_card: Card trying to be moved
    dest_card: Card/spot trying to be moved to
    """
    if src_card != []: #ensures source card is in fact a card
        
        #Checks to see if move proper for non-empty foundation
        if dest_card != []:
            if src_card.suit() == dest_card.suit() and src_card.rank() \
== dest_card.rank() + 1:
                valid = True
            else:
                valid = False
                
        #Checks for valid move if foundation empty        
        else:
            if src_card.rank() == 1:
                valid = True
            else:
                valid = False
                
    else: #For if source card not a card
        valid = False
         
    #Raises error for bad foundation moves    
    if valid == False:
        raise RuntimeError('Error: invalid command because of bad \
foundation move')
  
      
def valid_tab_move(src_card, dest_card):
    """
    Checks to see if a card can legally be moved to a tableau. Only
    allowed if destination is empty, or if source is same suit and 
    one lower than destination.
    src_card: Card trying to be moved
    dest_card: Card/spot trying to be moved to
    """ 
    if src_card != []: #ensures source card is a card
    
        #Checks for valid moves in non-empty tableaus
        if dest_card != []:
            if src_card.suit() == dest_card.suit() and src_card.rank() \
== dest_card.rank() - 1:
                valid = True
            else:
                valid = False
                
        else: #Makes moves to empty tableaus valid
            valid = True
            
    else: #For if source card not a card
        valid = False
        
    #Raises error for bad tableau moves     
    if valid == False:
        raise RuntimeError('Error: invalid command because of bad \
tableau move')
    
    
def tableau_to_cell(tab, cell):
    """
    Attempts to move tableau end-card to a cell. Only works for empty cells
    tab: tableau being moved from (list)
    cell: cell being moved to (list)
    """  
    
    #Removes card from tab and places in cell if cell empty
    if len(cell) == 0:
        cell.append(tab[-1])
        tab.pop()
     
    #Raises error if cell not empty    
    else:
        raise RuntimeError('Error: invalid command, cell not empty')
            
            
def tableau_to_foundation(tab, fnd):
    """
    Attempts to move tableau end-card to a foundation. Calls valid_fnd_move
    to ensure the move is allowed.
    tab: tableau being moved from (list)
    fnd: foundation being moved to (list)
    """
    #Adds to foundation and removes from tableau if move is valid for
    #Non-empty foundation
    if len(fnd) != 0:    
        valid_fnd_move(tab[-1], fnd[-1])
        fnd.append(tab[-1])
        tab.pop()   

    #Adds to foundation and removes from tableau if move is valid for
    #Empty foundation         
    else:
        valid_fnd_move(tab[-1], fnd) 
        fnd.append(tab[-1])
        tab.pop()
        
        
def tableau_to_tableau(tab1, tab2):
    """
    Attempts to move tableau end-card to a tableau. Calls valid_tab_move
    to ensure the move is allowed.
    tab1: tableau being moved from (list)
    tab2: tableau being moved to (list)
    """ 
    #Removes from tab1 and tab2 if both aren't empty
    if len(tab1) != 0:
        if len(tab2) != 0:
            valid_tab_move(tab1[-1], tab2[-1])
            tab2.append(tab1[-1])
            tab1.pop()
            
        #Removes from tab1 and tab2 if only tab2 empty    
        else:
            valid_tab_move(tab1[-1], tab2)
            tab2.append(tab1[-1])
            tab1.pop()
    
    #Raises an error for empty tab1        
    else:
        if len(tab2) != 0:
            valid_tab_move(tab1, tab2[-1]) 
        else:
            valid_tab_move(tab1, tab2)
            


def cell_to_foundation(cell, fnd):
    """
    Attempts to move cell card to a foundation. Calls valid_fnd_move
    to ensure the move is allowed.
    cell: cell being moved from (list)
    fnd: foundation being moved to (list)
    """   
    
    #Removes from cell and adds to foundation if both non-empty
    if len(cell) != 0:
        if len(fnd) != 0:
            valid_fnd_move(cell[-1], fnd[-1])
            fnd.append(cell[-1])
            cell.pop()
            
        #Removes from cell and adds to foundation if only cell non-empty    
        else:
            valid_fnd_move(cell[-1], fnd)
            fnd.append(cell[-1])
            cell.pop()
     
    #Raises an error for empty cell        
    else:
        if len(fnd) != 0:
            valid_fnd_move(cell, fnd[-1])
        else:
            valid_fnd_move(cell, fnd)        


def cell_to_tableau(cell, tab):
    """
    Attempts to move cell card to a tableau. Calls valid_tab_move
    to ensure the move is allowed.
    cell: cell being moved from (list)
    tab: tableau being moved to (list)
    """  
    
    #Removes from cell and adds to tableau if both non-empty
    if len(cell) != 0:
        if len(tab) != 0:
            valid_tab_move(cell[-1], tab[-1])
            tab.append(cell[-1])
            cell.pop()
            
        #Removes from cell and adds to tableau if only tableau empty
        else:
            valid_tab_move(cell[-1], tab)
            tab.append(cell[-1])
            cell.pop()
            
    #Raises error if cell empty        
    else:
        if len(tab) != 0:
            valid_tab_move(cell, tab[-1])
        else:
            valid_tab_move(cell, tab)
              
              
def is_winner(foundations):
    """
    Runs through and counts whether or not all 52 cards are in the
    foundations or not. Returns a boolean for true/false if they are or
    aren't. The player wins if true is returned
    foundations: List of foundations in game
    Returns: winner- boolean for whether they won or not
    """   
    
    total_fnd = 0 #initialize count
    
    #Adds length of foundations together for count
    for element in foundations:
        total_fnd += len(element)
    
    #Player wins if 52 cards in foundations    
    if total_fnd == 52:
        winner = True
    else:
        winner = False
        
    return winner
    
    


def setup_game():
    """
    The game setup function. It has 4 cells, 4 foundations, and 8 tableaus. All
    of these are currently empty. This function populates the tableaus from a
    standard card deck. 

    Tableaus: All cards are dealt out from left to right (meaning from tableau
    1 to 8). Thus we will end up with 7 cards in tableaus 1 through 4, and 6
    cards in tableaus 5 through 8 (52/8 = 6 with remainder 4).

    This function will return a tuple: (cells, foundations, tableaus)
    """
    
    stock = cards.Deck()
    cells = [[], [], [], []]                    #list of 4 lists
    foundations = [[], [], [], []]              #list of 4 lists
    tableaus = [[], [], [], [], [], [], [], []] #list of 8 lists
    
    n = 0 #start on left tableau
    
    #deals card and then moves right a tableau
    while len(stock) > 0: 
        tableaus[n].append(stock.deal())
        n += 1
        
        #returns back to first tableau
        if n == 8:
            n -= 8

    return cells, foundations, tableaus


def display_game(cells, foundations, tableaus):
    """
    Displays headers for cells and foundations, adds cells and foundations
    to string to display with proper spacing, converts tableaus to rows
    of strings and prints them in format.
    cells: list of cells
    foundations: list of foundations
    tableaus: list of tableaus
    """
    #Labels for cells and foundations
    print("    =======Cells========  ====Foundations=====")
    print("     --1----2----3----4--  --1----2----3----4--")
        
    cf_str = "      " #initialize cell and foundation line
    
    for element in cells:
        
        #shows empty list if cell empty
        if len(element) == 0:
            cf_str += "[ ]  "
            
        #shows card in cell if non-empty
        else:
            cf_str += (" " + str(element[0]) + "  ")
            
    cf_str += "  "  #adds spaces
     
    for element in foundations:
        
        #shows empty list if foundation empty
        if len(element) == 0:
            cf_str += "[ ]  "
        
        #shows top card in foundation if non-empty
        else:
            cf_str += (" " + str(element[-1]) + "  ")
            
    print(cf_str)
    print()
    
    #Labels for tableaus
    print("    =================Tableaus=================")
    print("    ---1----2----3----4----5----6----7----8---")
    
    #Initializes variables
    x = 0
    tab_lst = list()
    tab_str = "    "
    
    while x <= 52: #ensures we can print max tableau length
        for element in tableaus:
            
            #Tries to add tableau card to list, adds placeholder otherwise
            try:
                tab_lst.append(str(element[x]))
            except:
                tab_lst.append('  ')
                        
        x += 1 #moves to next tableau
        
        #Prints out formatted tableau in row, ignores empty lines
        for element in tab_lst:
            tab_str += "{:>5s}".format(element)
        if tab_str.strip() != "":
            print(tab_str)
            
        #Re-initialize variables    
        tab_str = "    "
        tab_lst = list()



#Prints rules and moves, initializes and displays game        
print(RULES)
cells, fnds, tabs = setup_game()
display_game(cells, fnds, tabs)
print(MENU)

#Prompts for and ideally edits command
command = input("prompt :> ").strip().lower()

while command != 'q': #quits on input of 'q' or 'Q'

    #Restarts for inputs of r
    if command == 'r':
        cells, fnds, tabs = setup_game()
    
    #Prints menu if prompted
    elif command == 'h':
        print(MENU)
    else:
        try:
            if command != '': #handles empty inputs
            
                #Splits command into list of inputs
                command_lst = command.split()
                
                #ensures input is long enough and has two numbers
                if len(command_lst) == 3 and command_lst[2].isnumeric() \
and command_lst[1].isnumeric():
                    command_lst[1] = int(command_lst[1])
                    command_lst[2] = int(command_lst[2])
                else:
                    raise RuntimeError("Error: Invalid command because \
of bad input")
          
            else:
                raise RuntimeError("Error: Invalid command because of \
empty input")
            
            #Moves from tab to fnd and checks for good indexing    
            if "tf" in command:
                if len(tabs) >= command_lst[1] and len(fnds) >= \
command_lst[2]:
                    tableau_to_foundation(tabs[command_lst[1] - 1], \
                                          fnds[command_lst[2] - 1])
                else:
                    raise RuntimeError("Error: Invalid command because \
input out of range")
                    
            #Moves from cell to fnd and checks for good indexing         
            elif "cf" in command:
                if len(cells) >= command_lst[1] and len(fnds) >= \
command_lst[2]:
                    cell_to_foundation(cells[command_lst[1] - 1], \
                                       fnds[command_lst[2] - 1])
                else:
                    raise RuntimeError("Error: Invalid command because \
                    input out of range")
                    
            #Moves from tab to tab and checks for good indexing         
            elif "tt" in command:
                if len(tabs) >= command_lst[1] and len(tabs) >= \
command_lst[2]:
                    tableau_to_tableau(tabs[command_lst[1] - 1], \
                                       tabs[command_lst[2] - 1])
                else:
                    raise RuntimeError("Error: Invalid command because \
                    input out of range")
                    
            #Moves from cell to tab and checks for good indexing         
            elif "ct" in command:
                if len(cells) >= command_lst[1] and len(tabs) >= \
command_lst[2]:
                    cell_to_tableau(cells[command_lst[1] - 1], \
                                    tabs[command_lst[2] - 1])
                else:
                    raise RuntimeError("Error: Invalid command because \
                    input out of range")
                    
            #Moves from tab to cell and checks for good indexing         
            elif "tc" in command:
                if len(tabs) >= command_lst[1] and len(cells) >= \
command_lst[2]:
                    tableau_to_cell(tabs[command_lst[1] - 1], \
                                    cells[command_lst[2] - 1])
                else:
                    raise RuntimeError("Error: Invalid command because \
                    input out of range")
           
            #Raises error if no proper move type given       
            else:
                raise RuntimeError("Error: Invalid command because of \
                bad input")

        #Prints error messages for raised RuntimeErrors        
        except RuntimeError as error_message:
            print("{:s}\nTry again.".format(str(error_message)))
    
    display_game(cells, fnds, tabs) #Re-displays game
    
    #Checks to see if they won and terminates program if they did
    if is_winner(fnds) == True:
        print(BANNER)
        break

    #Reprompts for new command               
    command = input("prompt :> ").strip().lower()


#Questions
#Q1: 7
#Q2: 5
#Q3: 3
#Q4: 6
#Q5: 7