##########################################################################
#   Computer Project #8
#   
#   Algorithm
#       Prompt for a file and open (with error checking)
#       Prompt for a region (with error checking)
#       Find all states in the file in said region
#           Append two per capita data pieces to each stae
#           Add these states to a list
#       Print out the region list
#       Prompt the user if they want to make a graph
#           If yes, prompt for two variables (with error checking)
#       Make a graph with chosen variables
#           Title graph, label axes, and label points
#       Add a regression line to the graph
#       Save the graph to a .png file
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
    
import pylab

# Here are some constants that are optional to use -- feel free to modify them, if you wish
REGION_LIST = ['far_west',
 'great_lakes',
 'mideast',
 'new_england',
 'plains',
 'rocky_mountain',
 'southeast',
 'southwest',
 'all']
VALUES_LIST = ['Pop', 'GDP', 'PI', 'Sub', 'CE', 'TPI', 'GDPp', 'PIp']
VALUES_NAMES = ['Population(m)','GDP(b)','Income(b)','Subsidies(m)','Compensation(b)','Taxes(b)','GDP per capita','Income per capita']
PROMPT1 = "Specify a region from this list -- far_west,great_lakes,mideast,new_england,plains,rocky_mountain,southeast,southwest,all: "
PROMPT2 = "Specify x and y values, space separated from Pop, GDP, PI, Sub, CE, TPI, GDPp, PIp: "

def plot_regression(x,y):
    '''Draws a regression line for values in lists x and y.
       x and y must be the same length.'''
    xarr = pylab.array(x) #numpy array
    yarr = pylab.array(y) #numpy arry
    m,b = pylab.polyfit(xarr,yarr, deg = 1) #creates line, only takes numpy arrays
    #as parameters
    pylab.plot(xarr,m*xarr + b, '-') #plotting the regression line
    


def plot(region_list):
    '''Plot the values in the parameters.'''
    
    # prompts for which values to plot and error checks
    
    variable_input = input("Specify x and y values, space separated from \
    Pop, GDP, PI, Sub, CE, TPI, GDPp, PIp:")
    x,y = variable_input.split()    
    while x not in VALUES_LIST or y not in VALUES_LIST:
        variable_input = input("Specify x and y values, space separated \
        from Pop, GDP, PI, Sub, CE, TPI, GDPp, PIp:")
        x,y = variable_input.split()
        
    # build x, the list of x values
    # build y, the list of y values
    # build the list of state names    
    x_index = VALUES_LIST.index(x) + 2
    y_index = VALUES_LIST.index(y) + 2    
    x = list()
    y = list()
    state_names = list()    
    for element in region_list:
        x.append(float(element[x_index]))
        y.append(float(element[y_index]))
        state_names.append(element[0])
    
    #Adds the title to the plot
    pylab.title(VALUES_NAMES[x_index - 2] + " versus " + \
                VALUES_NAMES[y_index - 2])

    pylab.xlabel(VALUES_NAMES[x_index - 2])   #label x axis
    pylab.ylabel(VALUES_NAMES[y_index - 2])   #label y axis

    #Makes scatter plot and labels each point
    pylab.scatter(x,y)
    for i, txt in enumerate(state_names): 
        pylab.annotate(txt, (x[i],y[i]))
         
    plot_regression(x,y) #Adds regression line to the plot 
          
    pylab.savefig("plot.png")   # saves the plot to file plot.png

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
    
def read_file(file_obj):
    '''Prompts for a region input, error checks until the region exists,
    appends all state data in that region to a region list, calculates
    and appends two new per capita variables to that list
    file_obj: file previously opened for reading
    Returns: region_list comprised of data on that region'''
    
    #Prompts for a region and initiates the region_list
    region_chosen = input("Choose a region:")
    region_list = list()
    good_region_input = False

    while good_region_input == False:   #Error checking loop     
        if region_chosen.lower() == "all": #Used to display all states
            for line in file_obj:
                if "State" in line: #skips the first line
                    continue
                
                #Adds data on all states to the region list
                else:           
                    state_list = line.strip().split(",")
                    region_list.append(state_list)
                    
            good_region_input = True
            
        #Displays states in chosen region
        elif region_chosen.lower() in REGION_LIST: 
            for line in file_obj:
                
                #Skips states not in region
                if region_chosen.lower() not in line.lower():
                    continue
                
                #Adds states in region to region list
                else:
                    state_list = line.strip().split(",")
                    region_list.append(state_list)
            good_region_input = True 
            
        #Prompts to re-enter region if not in list of regions
        else:
            print("Error in region name")
            region_chosen = input("Choose a region:")
    
    for element in region_list:
        
        #Calculates GDPp and PIp and appends it to each state in 
        #region list
        element_pop = float(element[2])*1000000
        element_inc = float(element[4])*1000000000
        element_gdp = float(element[3])*1000000000
        gdp_per = round(element_gdp / element_pop, 2)
        inc_per = round(element_inc / element_pop, 2)
        element.append(gdp_per)
        element.append(inc_per)
                
    return(region_list)

    
def display_info(region_list):
    '''Determines the max and min PIp and GDPp in the region, displays
    these findings, prints out a header line, then prints out all data
    from the region list
    region_list: List of data for states in a certain region'''
    
    max_gdp = 0
    max_income = 0
    min_gdp = 1000000000
    min_income = 1000000000
    
    #Determines the states with mins and maxes for PIp and GDPp
    for element in region_list:
        if element[8] > max_gdp:
            max_gdp = element[8]
            state_max_gdp = element
        if element[8] < min_gdp:
            min_gdp = element[8]
            state_min_gdp = element
        if element[9] > max_income:
            max_income = element[9]
            state_max_income = element
        if element[9] < min_income:
            min_income = element[9]
            state_min_income = element
            
    #Displays the states with mins and maxes for PIp and GDPp
    print("Max GDP:", state_max_gdp[0] + ":", "${:,.2f}".format(max_gdp)) 
    print("Min GDP:", state_min_gdp[0] + ":", "${:,.2f}".format(min_gdp))
    print("Max Income:", state_max_income[0] + ":", "${:,.2f}".format(max_income))
    print("Min Income:", state_min_income[0] + ":", "${:,.2f}".format(min_income))
    
    #Prints the variable names
    print("")
    print("{:20}{:20}{:20}{:20}{:20}{:20}{:20}{:20}{:20}{:20}".format(\
    "State","Region","Population(m)","GDP(b)","Personal Income(b)",\
    "Subsidies(m)","Comp of emp(b)","Tax on Prod/Imp(b)", \
    "GDP per capita", "Income per capita"))
    
    #Prints out all the data for each state in region list
    for element in region_list:
       print("{:20}{:20}{:^20,.2f}{:<20,.2f}{:^20,.2f}{:^20,.2f}{:^20,.2f}\
       {:^20,.2f}{:^20,.2f}{:^20,.2f}".format(element[0],element[1],\
       float(element[2]),float(element[3]),float(element[4]),\
             float(element[5]),float(element[6]),float(element[7]),\
                   float(element[8]),float(element[9]))) 
       

        
def main():
    #Runs three functions made above
    file_obj = open_file()
    region_list = read_file(file_obj)
    display_info(region_list)
    
    #Asks if the user wants a plot and makes one if answered yes
    make_plot = input("Do you want to create a plot?")
    if make_plot.lower() == "yes":
        plot(region_list)
    
    
if __name__ == "__main__":
    main()
    
    
    
    
    
#Questions
#Q1:5
#Q2:3
#Q3:2
#Q4:6
#Q5:7