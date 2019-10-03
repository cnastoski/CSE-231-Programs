#==============================================================================
# Project 6
#   algorithm
#       prompts user for imput  method
#       if brute force call brute_force_attack function, execute, and  show password
#       and time elapsed
#       if dictionary call dictionary_attack function and execute
#       if both call dictionary_attack function first and if it doesn't work call 
#       brute_force_attack function
#       ask user to prompt for type of hacking again
#==============================================================================





from itertools import product
import time
import zipfile
import string


def open_zip_file():
    """
    opens a zip file and returns a file pointer at the beginning of the file.
    
    """
    while True:
        file = input("Please enter the name of the zipfile you want to open: ")
        try:
            zip_file = zipfile.ZipFile(file)
            return zip_file
        except FileNotFoundError: #repromts user to enter a new file if the origional is invalid
            pass

def open_dict_file():
    """
    opens a text file full of passwords and returns a file pointer at the 
    beginning of the file.
    """
    while True: #stays in the loop while the given file does not exist
        text = input("Please enter the dictionary you want to use: ")
        try:
            dict_file = open(text,"r",encoding="utf-8")
            return dict_file
        except FileNotFoundError:
            pass
    
def brute_force_attack(zip_file):
    """
    attempts to crack a password protected zip file by checking each product
    of the alphabet up to 8 characters.
    zip_file: The zip_file that is supposed to be cracked.
    returns: the password of the zip file
    """
    for i in range(1,8): #repeats each product up to 8 characters
       for items in product(string.ascii_lowercase, repeat = i):
            password = "".join(items) #adds each letter to a line 
            try:
                zip_file.extractall(pwd=password.encode())  #attempts to crack the file by entering each 
                print("Brute force password is: ",password) # generated password
                return
            except: #takes care of all errors when iterating through passwords
                pass
                
def dictionary_attack(zip_file,dict_file):
    """
    attempts to crack a password protected zip file by iterating through a text
    file full of passwords.
    zip_file: The zip_file that is supposed to be cracked.
    dict_file: The text file full of passwords.
    returns the password of the zip file.
    """
    for line in dict_file:
        line = line.strip()
        try:
           password = line #sets each string of each line as a password
           zip_file.extractall(pwd=password.encode()) #tries to crack with the password of each line
           print("Dictionary password is: ", password) 
           return True #returns true if the correct password is found
        except:
            pass
    return False #Returns False if the password is not in the file
    



def main():
    
    hack = input("What type ('brute force','dictionary','both','q'): ")
    
    while hack != 'q': # enter q to quit the program
        if hack == 'dictionary':
            print("initiating",hack, "cracking")
            dict_file = open_dict_file() #open dict_file
            zip_file = open_zip_file() #open zip_file
            start = time.process_time() #starts to count time
            dictionary_attack(zip_file,dict_file)
            end = time.process_time() #ends time counting after the programs finishes
            total = end - start #calculates total time elapsed
            print('Elapsed TIme (seconds): ', total)
            hack = input("What type ('brute force','dictionary','both','q'): ")
            
            
        
        if hack == 'brute force':
            print('initiating',hack,'cracking')
            zip_file = open_zip_file()
            start1 = time.process_time()
            brute_force_attack(zip_file)
            end1 =  time.process_time()
            total1 = end - start
            print('Elapsed Time (seconds): ',total1)
            hack = input("What type ('brute force','dictionary','both','q'): ")
        
        if hack == 'both':
            print('initiating',hack,'types ')
            dict_file = open_dict_file()
            zip_file = open_zip_file()
            start = time.process_time()
            ans = dictionary_attack(zip_file,dict_file)
            end = time.process_time()
            total = end - start
            if ans == True: #if dictionary cracking succeeds , prints password and time.
                print('Elapsed TIme (seconds): ', total)
            if ans == False: # if dictionary cracking fails, moves on to brute force cracking
                print("No password was found")
                print('Dictionary Elapsed time (seconds): ',total)
                start1 = time.process_time()
                brute_force_attack(zip_file)
                end1 = time.process_time()
                total1 = end1 - start1
                print('Brute Force Elapsed Time (seconds): ', total)
            hack = input("What type ('brute force','dictionary','both','q'): ")
        else:
            quit
        


        
print("Cracking zip files.")
print("Warning: cracking passwords is illegal due to Sec. 53a-252.")
print("and has a prison term of 20 years")

if __name__ == "__main__": 
    main()












if pair[0] not in self.adj_list:
    vertex = Graph.Vertex(pair[0])
    vertex.add_edge(pair[1])
    self.adj_list[pair[0]] = vertex

if pair[1] not in self.adj_list:
    vertex = Graph.Vertex(pair[1])
    vertex.add_edge(pair[0])
    self.adj_list[pair[1]] = vertex

vertex1 = self.adj_list[pair[0]]  # add one
vertex1.add_edge(pair[1])
vertex2 = self.adj_list[pair[1]]  # add the second
vertex2.add_edge(pair[0])


