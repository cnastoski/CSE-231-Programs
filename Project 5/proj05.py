#==============================================================================
#  Computer Project #5
# Algorithm
#   prompt for a string
#   call get_shift function to find the most common characters shift from E
#   call output_plaintext function to decipher the sentence character by character
#   within output_plaintext call get_char to decipher each character
#   use main() function to call all funtions and decipher the string
#   output decoded text. 
#   asks if input is english, if not then it will run again with the next most
#   common letter
#==============================================================================



def get_char(ch,shift):
    """
    Change the shifted character back to the origional character by using the 
    ascii character ordering.
    ch: the character that is origionally given to the equation(str)
    shift: (int). The change from the order of the letter to the order of the 
    letter plus the shift.
    Returns: The newly shifted letter (str)
    """
    shift1 = ord(ch) + shift  #the order of the shifted letter
    if ch == ch.upper():
        if shift1 > 90:     #Lines 27-43 return the shifted character, but also
                            # wrap the alphabet around so Z goes to A and vice versa
            shift1 = shift1 - 90
            shift1 = 64 + shift1
        if shift1 < 65:
            shift1 = 64 - shift1
            shift1 = 90 - shift1
        shift_char = chr(shift1)
        return shift_char
    else:
             
        if shift1 < 97:
            shift1 = 96 - shift1
            shift1 = 122 - shift1
        if shift1 >122:
            shift1 = shift1 - 122
            shift1 = 96 + shift1
        shift_char = chr(shift1)    
        return shift_char
    

   
def output_plaintext(s,shift):
    """
    Takes a string and calls the get_char function to change the orgional 
    character one by one and then adds it to the empty plaintext string.
    s: the string that is inputted from outside the function.(str)
    shift:(int). The change from the order of the letter to the order of the 
    letter plus the shift.
    Returns: The same string that was inputted but with each character shifted 
    by the specified shift.
    Receives shift from get_shift function.
    """
    plaintext = ''
    for ch in s:
        if ch.isalpha(): #calls get_char to each ch in the string 
            char_add = get_char(ch,shift)
            plaintext += char_add 
        else:
            plaintext  += ch
    return plaintext
    
    
    
def get_shift(s,ignore):
    """
    Figures out the shift of the cipher by finding the most commonly used 
    character and subtracting the order of E from that character.
    s = the string that is inputted from outside the function.(str)
    ignore: A line of characters that is taken from the main function to 
    tell this function to not include those character while iterating through 
    the string. This is helpful for when the most common character is not E.
    Returns: The perceived shift of the string(int) and the most common 
    character(str).
    """
    s = s.upper()
    mode = 0 # count of the most common letter in string
    for ch in s:
        if s.count(ch) > mode and ch not in ignore: #ignores most common letter
            mode = s.count(ch)          #if it is not the right letter
            shifted_char = ch

    common = ord('E')
    mode1 = ord(shifted_char)
    shift = common - mode1 #finds difference between encrypted character and E
    return shift, shifted_char
    
def main():
    ignore = ' ' 
    s = input("please enter a sentence to be decrypted: ")
    shift,common = get_shift(s,ignore)
    decipher = output_plaintext(s,shift)
    print()
    print(decipher) 
    answer = input("is this readable? (yes/no): ")
    while answer == 'no':
        ignore += common
        shift, common = get_shift(s,ignore)
        decipher = output_plaintext(s,shift)
        print()
        print(decipher)
        answer = input("is this readable? (yes/no): ")
    
    return decipher, answer
 

print("Cracking a Caesar Cipher")
main()



#Questions
#Q1: 7
#Q2: 2
#Q3: 1
#Q4: 6
#Q5: 7

   
    


    
        
    
    





