#==============================================================================
#       Project 9
#        Algorithm
#open a file and return a pointer at the beginning
#create a dictionary with each unique word and the corresponding line as the values
#prompt user to input words separated by spaces
#iterate through file to find the words line numbers'
#compare the words' line numbers
#return the line numbers that have all of the inputted words
# keep repormpting user until q is entered
#==============================================================================


import subprocess
n = input("Enter a single-digit test number: ")
myoutput = open("output"+n+".txt","w")
myinput = open("test"+n+".txt",encoding="ascii",errors="surrogateescape")
p1 = subprocess.check_call(['python',"proj09.py"],stdin=myinput,stdout=myoutput)
myoutput.flush()
myinput.close()
myoutput.close()

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
        
        
        
        
def read_data(fp):
    ''' iterate through a file line by line and create a dictionary with each 
    unique word and the corresponding line numvbers'''
    line_dict = {} #initilize empty dictionary
    punctuation = '''.',-''' #the characthers we do not want
    line_num = 1 # represents the line number
    for line in fp:
        new_line = "" #create an empty string for each line
        for char in line: #recreate the line without punctuation 
            if char not in punctuation:
                new_line += char.lower()
        line_lst = new_line.strip().split(" ") #create a list of the line
        for item in line_lst:# remove all items from the list which are not words
            if item.isalpha() == False:
                line_lst.remove(item)
            try:
                if len(item) < 2: #remove all words less than 2 characters from the list
                    line_lst.remove(item)
            except ValueError:
                continue
        for item in line_lst:       #add the line number as the value to the word which
            if item in line_dict:   #is the key
                line_dict[item].add(line_num)
            else:
                line_dict[item] = set([line_num])#create the key for the dictionary
        line_num += 1 #turns into the next line
            
    return line_dict #returns a dictionary
    
    
def find_cooccurance(line_dict, inp_str):
    ''' takes an input of words and returs the common line numbers between all 
    of those words'''
    exclude = ".'," #the punctuation we do not want
    word_lst = ''.join(c for c in inp_str if c not in exclude) #recreate the string without punct
    word_lst = word_lst.strip().split(" ") #make a list of the words
    compare_lst = [] #initlize the list of words to compare
    for item in word_lst: #add the lines of the word to a list if it is in the file
        if item in line_dict.keys():
            compare_lst += [(line_dict[item])]
    try:
        coocurance = set.intersection(*compare_lst)
        return sorted(list(coocurance)) #uses set intersections to find the common lines 
    except TypeError:# ignores the input if there are no intersections
        pass
        
        
    
def main():
    fp = open_file()
    line_dict = read_data(fp)
    inp_str = input("Enter the space-separated words: ")
    inp_str = inp_str.lower()
    
    while inp_str != 'q': #stays in loop until user wants to quit
        inp_lst = inp_str.split(" ") #creates a list of the inputs
        print("The co-occurance for: ",", ".join(inp_lst)) 
        lines = find_cooccurance(line_dict,inp_str)
        try: #tries printing the lines neatly and prints none if the words are not in file
            print("Lines: ",", ".join([str(item) for item in lines])) #converts all numbers to strings
        except TypeError:
            print("Lines: None")
        inp_str = input("Enter the space-separated words: ")
        inp_str = inp_str.lower()
    pass



if __name__ == "__main__": 
    main()
    
    
#Questions
#Q1:7
#Q2:2
#Q3:1
#Q4:6
#Q5:7






