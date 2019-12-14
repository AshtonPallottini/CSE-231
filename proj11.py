############################################################################
#   Computer Project #11
#   
#   Algorithm
#   Prompt for a file to open
#   Loop until valid file input
#   Create a matrix with adjacent rooms in the appropriate index
#   Create a list of all rooms
#   Create a list of combinations of x rooms in this list 
#   Loop through each combination
#       Loop through each room
#           Use first room as set 1
#           Find Union of this set and sets of other rooms in combination
#           If union has all rooms, print end number TAs and rooms assigned
#   Print out Adjacency Matrix
############################################################################
   
import itertools

class Matrix(object):
    '''Reads a file and creates a matrix of rooms that each room is 
    adjacent to.'''
    
    def __init__(self):
        '''Create and initialize your class attributes.'''
        self._matrix = []
        self._rooms = 0
        
    def read_file(self,fp):
        '''Build an adjacency matrix that you read from a file fp.'''
        self.fp = fp
        n = fp.readline() #Skips first line and determines number of rooms
        n = int(n)
        self._rooms = n
        network = []

        #Initializes matrix of n lists
        for i in range(n):
            network.append([])
            
        #Adds adjacent rooms to appropriate list in matrix
        for line in fp:
            line.strip()
            u, v = line.split()
            u = int(u)
            v = int(v)
            network[u - 1].append(v)
            network[v - 1].append(u)
            
        self._matrix = network
            
        return network
            
    def __str__(self):
        '''Return the matrix as a string.'''
        s = ''
        n = 1 #Used for room number
        
        #Adds room numbers and elements of matrix to string
        for element in self._matrix:
            s += (str(n) + ": " + str(element) + "                          \
                                                               ")
            
            #Removes brackets and commas
            for ch in s:
                if ch == "[" or ch == "]" or ch == ",":
                    spot = s.find(ch)
                    s = s[0:spot] + s[(spot + 1):]
            n += 1
        return s 

    def __repr__(self): 
        '''Call __str__() to return a string for displaying in the shell'''
        return self.__str__()  
        
    def adjacent(self,index):
        '''Return the set of connecting rooms to room specified by index'''
        return set(self._matrix[index - 1])

    def rooms(self):
        '''Return the number of rooms'''
        return self._rooms

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
                
    return file_obj        

    

def main():
    
    #Runs functions and makes a matrix from the opened file
    file_obj = open_file()
    A = Matrix()
    print()
    connection = Matrix.read_file(A, file_obj)
    
    #Initializes variables for combination length,finding match, and room list
    match = False
    n = 1
    list_rooms = list()
    
    #Makes list of all rooms
    for i in range(1, (len(connection) + 1)):
        list_rooms.append(i)
        
    while match == False:
        
        #Makes list of all combinations of length n from list of rooms
        combinations = list(itertools.combinations(list_rooms, n))
        set_total = set()
        for element in combinations:
            for room in element:
                
                #Sets first room's adjacencies in combination as first set
                if element.index(room) == 0:
                    set_1 = set(connection[room - 1])
                    set_1.add(room)
                    set_union = set_1
                    set_total = set_union
                    
                #Finds Union of first set and set of nth room's adjacencies     
                else:
                    set_2 = set(connection[room - 1])
                    set_2.add(room)
                    set_union = set_1 | set_2
                    
                    #Makes set of all rooms covered by combination
                    for number in set_union:
                        set_total.add(number)
                        
            #Prints end message and breaks if all rooms covered by combination            
            if len(set_total) == len(list_rooms):
                match = True
                print("TAs needed:", n)
                assign_str = "TAs assigned to rooms:" + \
                str([i for i in element])
                
                #Removes brackets from message
                for ch in assign_str:
                    if ch == "[" or ch == "]":
                        spot = assign_str.find(ch)
                        assign_str = assign_str[0:spot] + assign_str[(spot + 1):]
                print(assign_str)
                break
            
        n += 1 #Increases length of combinations
    
    #Prints out Adjacency Matrix at the end
    print()
    print("Adjacency Matrix")
    print(Matrix.__str__(A))
            
    
    
    
    
if __name__ == "__main__":
    main()
    
    
    
    
#Questions
#Q1:4
#Q2:2
#Q3:2
#Q4:6
#Q5:7