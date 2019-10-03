#==============================================================================
#   Project 11
#       Algorithm
#prompts user to enter a file, reprompts if file doesn't exist
#Initilizes the matrix class and inputs the file into it
#Creates the room adjacency matrix
#creates a list of all of the rooms
#starts with one TA
#iterates through a while loop trying all combonations of one TA in the rooms
#makes a set union of all of the rooms covered by one TA
#if one TA covers all rooms, the code breaks
#otherwise another TA is added and the code loops again
#prints out the output of how many TA's are needed and where they will be put
#break
#==============================================================================
import itertools

class Matrix(object):
    '''Class designed to take in a file and create an adjacency matrix with all
    of the given values. Takes in a file as an input and outputs the adjacent rooms
    to a particular rooms or outputs all of the rooms in the file.'''
    
    def __init__(self):  
        '''Create and initialize your class attributes.'''
        self._matrix = []
        self._rooms = 0
        
    def read_file(self,fp):  #fp is a file pointer
        '''Build an adjacency matrix that you read from a file fp.'''
        self._rooms = fp.readline() #top line of the file which is the amount of users
        self._rooms = int(self._rooms) #change from a string to an int
        for i in range(self._rooms):  #creates alists inside of the network list according to how many rooms there are
            self._matrix.append([]) 
        for line in fp: #takes column 1 and column 2 of each row and adds them into the network
            line = line.strip()
            room_1, room_2 = line.split()
            room_1 = int(room_1)    
            room_2 = int(room_2)
            
            self._matrix[room_1-1].append(room_2) #assembles the matrix
            self._matrix[room_2-1].append(room_1) #each room is a list with the items being all of the other 
                                                  # connected rooms
        return self._matrix
            
    def __str__(self):
        '''Return the matrix as a string.'''
        s = ''
        for i in range(self._rooms): #iterates through each room, 
            matrix_str = ' '.join(map(str, self._matrix[i]))#adding the room number and the adjacent rooms
            s = s +"\n" + "{}: {}".format(i+1,matrix_str) #and adds a new line for each room
            
        return s  #__str__ always returns a string

    def __repr__(self): 
        '''Call __str__() to return a string for displaying in the shell'''
        return self.__str__()  
        
    def adjacent(self,index):
        '''Return the set of connecting rooms to room specified by index'''
        adj = self._matrix[index-1] #finds the index of the desired room and returns that as a set
        return set(adj)  

    def rooms(self):
        '''Return the number of rooms'''
        rooms = self._rooms #takes the first line of the file and returns that
        return int(rooms)# the first line of the file should be the number of rooms
        
        
        
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

def main():
    fp = open_file() #the file we are iterating through
    M = Matrix() #initilize the matrix
    M.read_file(fp) #assemble the matrix
    rooms = M.rooms()
    rooms_lst = [] #initilize the list of rooms
    for i in range(rooms): #create the list of rooms
        rooms_lst.append(i+1)
    ta = 1 #minimum number of TA's
    stop = False #tells the code when to stop
    while stop == False: #loops until the minimum viable number of TA's are reached
        combo_lst = itertools.combinations(rooms_lst,ta) #creates all combonations of the TA's in the rooms
        for item in combo_lst: #iterates through each combonation
            covered_lst = [] #initilize the rooms covered list
            c_set = set() #this will add the rooms the TA's are in, since they also cover those too
            for c in item: #iterates through each item in a combonation
                adj = M.adjacent(c) #finds the adjacent rooms to the room the TA is in
                covered_lst.append(adj) #adds it to the list of covered rooms
                c_set.add(c) 
            covered_lst.append(c_set) #add the room the TA is in to the covered list
            check_set = set.union(*covered_lst) #makes a union of all of the sets in the covered list
            check_lst = list(check_set) #converts it to a list to compare to the original room list
            if check_lst == rooms_lst: 
                stop = True              #if the program finds one combonation that 
                print("TAs needed: ",ta) #covers all rooms, stop the code and print the results
                list(item)
                print("Tas assigned to rooms: ",', '.join(map(str, item))) #print the rooms the TA's are in nicely
                print()
                print("Adjacency Matrix")
                print(M)
                break
        if stop == False: #if that many TA's are not enough, add another and try again
            ta += 1

    pass   

if __name__ == "__main__":
 main()    
 

 
 
 
# Questions
# Q1: 7
# Q2: 2
# Q3: 1
# Q4: 5
# Q5: 7
        
            