"""
File of function stubs for Projecct 07

@author: enbody
"""
###########################################################################
#   CSE Project #7
#
#   Algorithm
#       Run the open_file function
#       Create a Network of friends from this file using read_file
#       Create a similarities matrix from this using calc_similarity_scores
#       Prompt for user ID
#           Error check to make sure input is in an int in range
#       Use recommend to recommend a friend for this user ID
#       Prompt user whether they want to run it again or not
###########################################################################

###########################################################################
import sys
def input( prompt=None ):
    if prompt != None:
        print( prompt, end="" )
    aaa_str = sys.stdin.readline()
    aaa_str = aaa_str.rstrip( "\n" )
    print( aaa_str )
    return aaa_str
###########################################################################

def open_file():
    ''' Try to open an inputed file except when it is not found
    returns: file that is opened (fp)'''
    
    good_input = False
    file_input = input("Input a file:")
    
    #Attempts to open a file and reprompts until successful
    while good_input == False:
        try:
            file_obj = open(file_input, "r")
            break
        except:
            print("Error in filename.")
            file_input = input("Input a file:")
            
    return(file_obj)


def read_file(fp):  
    ''' Create a list of length n of lists (network), strips and splits 
    line in the opened file, then appends the friends each user has to the 
    corresponding spot in the network
    fp: the file previously opened
    returns: network of friend lists'''
    
    #Creates a list of n lists
    n = fp.readline()
    n = int(n)
    network = []
    for i in range(n):
        network.append([])
    
    #Appends friends to their appropriate lists
    for line in fp:
        line.strip()
        u, v = line.split()
        u = int(u)
        v = int(v)
        network[u].append(v)
        network[v].append(u)
        
    return network

def num_in_common_between_lists(list1, list2):
    ''' Sets a variable at 0, then loops through a list to find out if
    which elements they have in common, giving us the total they have
    returns: total in common'''
    
    total_common = 0
    
    #Adds one if the element is shared by lists
    for element in list1:
        if element in list2:
            total_common += 1
            
    return(total_common)

def init_matrix(n):
    '''Create an nxn matrix, initialize with zeros, and return the matrix.'''
    
    matrix = []
    for row in range(n):  # for each of the n rows
        matrix.append([])  # create the row and initialize as empty
        for column in range(n):
            matrix[row].append(0)  # append a 0 for each of the n columns
    return matrix
    
def calc_similarity_scores(network):  
    ''' Create a matrix with init_matrix, loop through indices within
    the length of the network, ignore when indices are equal, run 
    num_in_common_between_lists to determine similarities between lists,
    set this count at the appropriate value in the matrix
    network: network of list of friends
    returns: a matrix of similarities between friends'''
    
    #initializes similarity_matrix
    similarity_matrix = init_matrix(len(network))
    
    for i in range(len(network)):
        for j in range(len(network)):
            
            #disregards similarities between a list and itself
            if i == j:
                continue
            
            #Finds the lists' common values count and places it in the matrix
            else:
                in_common = num_in_common_between_lists(network[i], \
                                                        network[j])
                similarity_matrix[i][j] = in_common
                similarity_matrix[j][i] = in_common
                
    return(similarity_matrix)


def recommend(user_id,network,similarity_matrix):
    ''' Sets a value at zero, goes through similarity_matrix at the given
    index, skips the element if it is already a friend or is the person we
    are given, otherwise if the common friends exceed the max count it sets
    that person as the recommendation
    user_id = the ID of which user we are looking at
    network: network of list of friends
    similarity_matrix: a matrix of similarities between friends
    returns: the user with the most friends in common that is not already
    a friends'''
    
    max_count = 0
    
    #Loops through the given user's friend similarities
    for element in similarity_matrix[user_id]:
        
        #disregards people they are friends with
        if similarity_matrix[user_id].index(element) in network[user_id]:
            continue
        
        #disregards the person themself
        elif similarity_matrix[user_id].index(element) == user_id:
            continue
        elif element > max_count: #finds the maximum count
            max_count = element
        else:
            continue
    
    #defines the person that the most similarities were with
    max_index = similarity_matrix[user_id].index(max_count)
    
    return(max_index)
        
    
def main():
    
    #definition of variables
    program_run = "Yes"
    integer_input = False
    
    #Prints a welcome message
    print("Facebook friend recommender")
    print("")
           
    #Runs open_file, then read_file, then calc_similarity_scores
    file_pointer = open_file()
    network_here = read_file(file_pointer)
    similarity_matrix = calc_similarity_scores(network_here)
    
    #Loops while user wants it to, quits for variations of "no"    
    while program_run.lower() != "no":
        print("")
        
        #Asks for an ID in the range of possibilities
        user_id_str = input("input a user ID in the range 0 to " \
                            + str(len(similarity_matrix[0]) - 1) + ":")
        
        while integer_input == False:
            try:
                user_id = int(user_id_str)
                
                #Error checks for IDs not in the possible range
                while user_id not in range(len(similarity_matrix[0])):
                    print("Error: user ID must be in range")
                    user_id_str = input("input a user ID in the range 0 to "\
                                        + str(len(similarity_matrix[0]) - 1)\
                                                  + ":")
                    user_id = int(user_id_str) 
                break                               
           
            #error checks for non-integer inputs
            except:
                print("Error: user ID must be an integer.")
                user_id_str = input("input a user ID in the range 0 to " \
                                    + str(len(similarity_matrix[0]) - 1) \
                                              + ":")

        #runs recommend and prints the recommendation    
        recommendation = recommend(user_id, network_here, similarity_matrix)
        print("The recommendation for", user_id, "is:",recommendation)
        print("")
        
        #prompts the user whether or not to run again
        program_run = input("See another recommendation?")

    
if __name__ == "__main__":
    main()

    
#Questions
#Q1:5
#Q2:4
#Q3:2
#Q4:6
#Q5:7   
    