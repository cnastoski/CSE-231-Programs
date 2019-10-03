#==============================================================================
# Project #7
#   Algorithm
#       prompt for a data file
#       prompt for an integer
#       create a list of lists from each line and add all the users to a list 
#       inside of the list of which the index is ranked by the user_id
#       Send all of those lists into a similarity matrix to sort out the similarities 
#       output the most likely user to be friends with the inputted user
#       reprompt for integer
#==============================================================================




def open_file():
    """
    opens a text file full of data and returns a file pointer at the 
    beginning of the file.
    """
    while True: #stays in the loop while the given file does not exist
        text = input("Please enter the file you want to use: ")
        try:
            file = open(text,"r",encoding="utf-8")
            return file
        except FileNotFoundError: #ignores this error
            pass


def read_file(fp):  
    """ 
    Send a file pointer through the file, create a list of lists, and add all
    of the matches to user n in list[n]. Return a network of users.
    """

    n = fp.readline() #top line of the file which is the amount of users
    n = int(n)
    network = [] #The main list
    for i in range(n):  #creates a list inside of the network list according to n
        network.append([])
    for line in fp: #takes column 1 and column 2 of each row and adds them into the network
        line = line.strip()
        person_1, person_2 = line.split()
        person_1 = int(person_1)
        person_2 = int(person_2)
        
        network[person_1].append(person_2) 
        network[person_2].append(person_1)

    return network

def num_in_common_between_lists(list1, list2):
    """
    iterates through two lists and returns the commonalities between them
    """
    common = 0 #adds the amount of common numbers between the two lists
    for item in list1:
        if item in list2:
            common +=1
        
    return common 

def init_matrix(n):
    '''Create an nxn matrix, initialize with zeros, and return the matrix.'''
    matrix = []
    for row in range(n):  # for each of the n rows
        matrix.append([])  # create the row and initialize as empty
        for column in range(n):
            matrix[row].append(0)  # append a 0 for each of the n columns
    return matrix
    
def calc_similarity_scores(network):  
    '''
    creates a similarity matrix from the list of networks and finds the amount 
    of users that other users have in common with. Returns a matrix of each user's
    similar friends with the next user up to the nth user.
    '''
    n = len(network) 
    n_int=int(n)
    similarity_matrix = init_matrix(n_int) #subs out the placeholder 0's with the user's info
    
    for j in range(n_int): 
        for k in range(n_int):
           match =  num_in_common_between_lists(network[j],network[k]) #apends the similarities of j and k to the similarity matrix
           similarity_matrix[j][k] = match
        
    return similarity_matrix

def recommend(user_id,network,similarity_matrix):
    ''' 
    loops through the user's most similar user that the user is not currently friends
    with and returns that user.
    '''
    sim= -1000 #the amount of similar friends they have
    sim_id = -50 #the user's index
    member = int(user_id)
    for index,item in enumerate(similarity_matrix[member]): #iterates through the matrix looking for similar friends
        
        if index == member:
            continue
        if index in network[member]:
            continue
        if item > sim: #replaces the placeholder with the actual amount of similar friends
            sim = item
            sim_id = index
    
    return sim_id
    
def main():
    print("Facebook Friend Reccomendation")
    print()
    network = read_file(open_file())
    user_range = str(len(network) - 1) #amount of users in the network
    similarity_matrix = calc_similarity_scores(network)
    while True: 
        search = input("enter an integer from 0 to "+user_range+" : ")
            #special formatting to include the range in a string
        try: # Error checking to see if the input is in the range
            int_search = int(search)
        except:
            print("Error: Must be between 0 and "+user_range+" : ")
            search = input("enter an integer from 0 to "+user_range+" : ")
            continue
            
        if int_search >= 0 and int_search <= int(user_range): # if the input is valid, runs through the code to find recommended friend.
            friend_rec = recommend(int_search, network,similarity_matrix)
            print("The suggested friend for",int_search,"is",friend_rec)
            cont = input("Do you want to continue (yes/no)?: ")
            cont.lower() #asks if you want to continue and reprompts for input
            if cont == "yes":
                continue
            if cont == "no":
                break
            if int_search <0 or int_search > (int(user_range)):
                continue
            
    
if __name__ == "__main__":
    main()


# Questions
# Q1: 5
# Q2: 3
# Q3: 4
# Q4: 6
# Q5: 7









