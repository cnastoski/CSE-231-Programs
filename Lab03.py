



word_str = input('Please enter a word: ')

while word_str.lower() != "quit":
    if word_str[0] in "aeiou":
        pig_str = word_str + 'way'
        print('{:>15s} becomes {:<15s}'.format(word_str,pig_str))
        
        
    else: 
        new_word = word_str
        while new_word[0] not in 'aeiou':
            new_word = new_word[1:] + new_word[0]
        new_word += 'ay'
        print('{:<15s} becomes {:>15s}'.format('"'+word_str+'"','"'+new_word+'"'))
            
            
    word_str = input('Please enter a word: ') 
    
        
    
        
        