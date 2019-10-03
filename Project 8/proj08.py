#==============================================================================
#  Project 08
#      Algorithm
#       prompt user to enter a data file, keeps prompting if it doesn't exist
#       calls function to compile data into lists and add them all to a main list
#       goes through each state and appends the GDP per capita and Income per capita
#       and adds those values to a list
#       prompts user to enter a region
#       calls function to sift through list to get only states in specefied region
#       calls function to return the states with highest and lowest GDP per capita and income per capita
#       calls function to print GDp per capita and income per capita and also
#       prints the information for all states in the region
#       prompts user if he wants to make a plot
#       prompts user which values to plot
#       calls function to plot values
#       end
#==============================================================================


import pylab


def open_file():
    """
    opens a file and returns a file pointer at the 
    beginning of the file.
    """
    while True: #stays in the loop while the given file does not exist
        text = input("Please enter the file you want to use: ")
        try:
            file = open(text,"r")
            return file # returns file pointer
        except FileNotFoundError:
            print("Error: File not found. Please enter another file.")
            pass
    
def create_state_lists(file):
    """
    iterates through each line in the file and adds them to a list and then adds
    each list to a file and returns that list.
    
    """
    state_lst= [] # initalize the main list
    file.readline() #ignores first line in the file
    for line in file:
        state_data = line.strip().split(",") #makes a list of data of each state
        for i, item in enumerate(state_data): 
            try: #for loop iterates through each item in the list of the state and
                state_data[i] = float(item) #changes each number from a string to a float if possible
            except ValueError:
                pass

        pop = float(state_data[2])  #population of state
        gdp = float(state_data[3])  #Gross domestic product of state
        personal_inc = float(state_data[4]) #personal income for the entire state 
        gdpp = round(((gdp*(10**9))/(pop*(10**6))),2) #calculates gdp per person of state
        state_data.append(gdpp) #adds it to the list of the data of the state
        ipc = round((personal_inc*(10**9))/(pop*(10**6)),2)  #income per capita
        state_data.append(ipc)
        state_lst.append(state_data) #adds all state information into a huge list
   
    return state_lst #list of lists of states
    
    
    
def choose_region(state_lst,selection):
    """
     Takes the states list and an input to sort through the region of each state
     and returns a list of the states within a certain region.
    """
    region_lst = [] #initalize list
    selection.lower() #converts input into all lowercase letters
    for item in state_lst: #takes the index of the state's region and adds that whole
        region = item[1]   #list to the region list
        if region.lower() == selection:
           region_lst.append(item)
        if selection == "all": #adds every list if the user requests all states
            region_lst = state_lst   
            
    return region_lst #a list of the states in the specified region



def calc_extremes(region_lst):
    """
    Takes the region list as an input and calculates the maximum and minimum GDP
    per capit and Income per capit and adds them all to a dictionary along with the 
    corresponding state and returns the dictionary.
    """

    gdpp_max = 0 #initilize each value that we want
    gdpp_min = 5000000 #minimum GDP per capita
    icpc_min = 5000000 #minimum Income per capita
    icpc_max = 0 #maximum Income per capita
    extreme_dict = {} #initalize the dictionary
    
    for item in region_lst: #iterates through each state looking for the max and min GDP and income
        if item[8] > gdpp_max:
            extreme_dict["gdpp_max"] = [item[0], item[8]]#gdpp_max is the key and the state name and gdp are the values 
            gdpp_max = item[8] #sets a new value for the max gdp 
        if item[8] < gdpp_min:
            extreme_dict["gdpp_min"] = [item[0], item[8]] #the dictionary changes each time a smaller value is found
            gdpp_min = item[8]
        if item[9] > icpc_max:
            extreme_dict["icpc_max"] = [item[0], item[9]]
            icpc_max = item[9]
        if item[9] < icpc_min:
            extreme_dict["icpc_min"] = [item[0], item[9]]
            icpc_min = item[9]
    return extreme_dict #dictionary with each max and min
    
    
def display_info(region_lst,selection):
    """
    Takes the list of the states in a region along with the user's choice of region 
    and prints the states with the max and min GDPp and ICp and also prints all
    of the information of the states within the region.
    
    """
    header = ['State','Population(m)','GDP(b)','Income(b)','Subsidies(m)'\
              ,'Compensation(b)','Taxes(b)','GDP per capita',\
              'Income per capita'] #The title for each column
    
    print()
    print("Showing data from the",selection.title(),"region.") #shows which region was specified
    print()
    d1 = calc_extremes(region_lst) #calls function to calculate max and min GDPp and ICp
    print("{} has the highest GDP per capita at ${:,.2f}"\
          .format(d1["gdpp_max"][0],d1["gdpp_max"][1])) #prints max GDPp nicely
    print("{} has the lowest GDP per capita at ${:,.2f}"\
          .format(d1["gdpp_min"][0],d1["gdpp_min"][1])) #prints min GDpp nicely
    print()
    print("{} has the highest income per capita at ${:,.2f}"\
          .format(d1["icpc_max"][0],d1["icpc_max"][1])) #prints max Income per capita nicely
    print("{} has the lowest income per capita at ${:,.2f}"\
          .format(d1["icpc_min"][0],d1["icpc_min"][1])) #prints min Income per capita nicely
    print()
    print("Data for all states in the {} region.".format(selection.title()))
    print()
    print("{:28}{:23}{:20}{:20}{:20}{:20}{:20}{:20}{:20}".format(header[0],\
          header[1],header[2],\
          header[3],header[4],header[5],header[6],header[7],header[8])) #prints each column header nicely
    
    for item in region_lst: #iterates throuch each state printing each column nicely
        del item[1] #removes the region from the state list because it is not needed
        print("{:20}{:20,.2f}{:20,.2f}{:20,.2f}{:20,.2f}{:20,.2f}{:17,.2f}\
        {:20,.2f}{:20,.2f}".format(item[0],\
          item[1],item[2],\
          item[3],item[4],item[5],item[6],item[7],item[8])) #each item in the list is a column
    
    pass #returns nothing since it prints everything


def plot_regression(x,y):
    '''Draws a regression line for values in lists x and y.
       x and y must be the same length.'''
    xarr = pylab.array(x) #numpy array
    yarr = pylab.array(y) #numpy arry
    m,b = pylab.polyfit(xarr,yarr, deg = 1) #creates line, only takes numpy arrays
    #as parameters
    pylab.plot(xarr,m*xarr + b, '-') #plotting the regression line
    
def choose_axes():
    """
    Error checks the plot axes to see if the inputs match the values given and 
    returns the two x and y axes.
    
    """
    
    value_lst = ['pop', 'gdp', 'pi', 'sub', 'ce', 'tpi', 'gdpp', 'pip'] #all of the available axes
    
    while True: #stays in loop while the input is not valid
        inputs = input("Specify x and y values, space separated from Pop, GDP,\
PI, Sub, CE, TPI, GDPp, PIp: ") 
        try:
            x,y =  inputs.lower().split(" ") #tries to pull two values from the input
            while (x or y) not in value_lst: #keeps reprompting if the two values are not in the list
                print("Error: You must Enter the axes from the list") 
                inputs = input("Specify x and y values, space separated \
from Pop, GDP, PI, Sub, CE, TPI, GDPp, PIp: ") 
                x,y =  inputs.lower().split(" ")
            return x,y #returns the two axes
        except ValueError: #reprompts user if the user puts in only one value or more than one value
            print("Error: you must enter 2 values from the list")
            pass



def plot(region_lst):   # you need to replace pass with parameters
    '''Plots the values in the parameters.'''
    value_lst = ['pop', 'gdp', 'pi', 'sub', 'ce', 'tpi', 'gdpp', 'pip']
    title = ['Population(m)','GDP(b)','Income(b)','Subsidies(m)'\
              ,'Compensation(b)','Taxes(b)','GDP per capita',\
              'Income per capita']
    
    x,y = choose_axes() #calls function to error check the axes 
    
    x_index = value_lst.index(x) + 1 #finds index of the first specified value according to the input
    y_index = value_lst.index(y) + 1 #finds index of second value using the input 
    x_lst = [item[x_index] for item in region_lst] # build x, the list of x values
    y_lst = [item[y_index] for item in region_lst] # build y, the list of y values
    state_names = [item[0] for item in region_lst] # builds a list of the state names

    pylab.title("{} vs. {}".format(title[x_index-1],title[y_index-1])) # plot title
    pylab.xlabel("{}".format(title[x_index-1]))   #label x axis                
    pylab.ylabel(title[y_index-1])   #label y axis
    
    pylab.scatter(x_lst,y_lst)
    for i, txt in enumerate(state_names): #labes each point with the corresponding state
       pylab.annotate(txt, (x_lst[i],y_lst[i]))
    
    plot_regression(x_lst,y_lst) #calls function to plot the regression line
    
    pylab.show() #displays plot
    pass


def main():
    prompt1 = "Specify a region from this list -- \
far_west,great_lakes,mideast,new_england,plains,rocky_mountain\
,southeast,southwest,all: " #the prompt
    region_lst = ['Far_West',
                   'Great_Lakes',
                   'Mideast',
                   'New_England',
                   'Plains',
                   'Rocky_Mountain',  
                   'Southeast',
                   'Southwest',
                   'All'] #list of available regions
    file = open_file() #opens file
    state_lst = create_state_lists(file) #compiles a list of lists
    choice = input("{}".format(prompt1)) #prompts for region       
    while choice.title() not in region_lst: #stays in loop while user enters an invalid region
        print("Error: Invalid Region")
        choice = input("{}".format(prompt1))
    choice = choice.lower() #turns all letters into lowercase
    region_lst = choose_region(state_lst,choice) #sifts through states looking for states within region
    display_info(region_lst,choice) #prints data nicely
    ans = input("Would you like to create a plot?: ") #prompts user to if he wants to plot values
    if ans.lower() ==  "yes": #plots a function if the user says yes and end the program otherwise
        plot(region_lst)
    pass


if __name__ == "__main__": 
    main()
    
    
#Questions
#Q1:7
#Q2:2
#Q3:1
#Q4:6
#Q5:7