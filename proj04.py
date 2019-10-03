
print("Welcome to hangman")
print("to play, just enter a word and then try to guess letters until you can \
 guess the whole word")



k = 6

word= input("Please enter a word: ")
word = word.lower()

if word.isalpha() == False:
        print("Error: You can only enter a word or phrase.")
        word= input("Please enter a word: ")





while word != "quit":
    
    current = "-"*len(word)
    print("current: ", current)
    
    guess = input("Please enter a letter: ")
    
    
        
    
    
    
    
    while k > 0:
        
        
        if guess not in word:
            k -= 1
            print("incorrect, guess again: ")
            print(k,"guesses so far out of 6:", guess)
            guess = input("Please enter a letter: ")
            
        if guess in word[0]:
            k-1
            current1 = guess+ current[1:]
            print(k,"guesses so far out of 6:", guess)
            guess = input("Please enter a letter: ")
            break
        if guess in word[1]:
            k-1
            current2 = current1[0] + guess + current1[2:]
            print(k,"guesses so far out of 6:", guess)
            guess = input("Please enter a letter: ")
            break
        if guess in word[2]:
            k-1
            current3 = current2[:1] + guess + current[3:]
            print(k,"guesses so far out of 6:", guess)
            guess = input("Please enter a letter: ")
            break
        if guess in word[3]:
            k-1
            current4 = current3[:2] + guess + current3[4:]
            print(k,"guesses so far out of 6:", guess)
            guess = input("Please enter a letter: ")
            break
        if guess in word[4]:
            k-1
            current5 = current4[:3] + guess + current4[5:]
            print(k,"guesses so far out of 6:", guess)
            guess = input("Please enter a letter: ")
            break
            
            
            
            
            
        guess = input("Please enter a letter: ")
           
                
#Questions
#Q1: 1 
#Q2: 6
#Q3: 6
#Q4: 4
#Q5 :6               
            
    
            
        
        
        
        
        
        







