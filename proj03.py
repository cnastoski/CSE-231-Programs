#==============================================================================
# This code is used by the testing framework.  Uncomment when you want to 
# execute the run_file.py testing program.  This code replace the input
# function so the input from the test.txt file appears in the output.txt file.
#
# import sys
# def input( prompt=None ):
#     if prompt != None:
#         print( prompt, end="" )
#     aaa_str = sys.stdin.readline()
#     aaa_str = aaa_str.rstrip( "\n" )
#     print( aaa_str )
#     return aaa_str
# empty_stock = False
#==============================================================================



quarters = 10
dimes = 10
nickels = 10
pennies = 10


print("\nWelcome to change-making program.")
in_str = input("Enter the purchase price (xx.xx) or `q' to quit: ")
out_str = input("Please enter amount paid (int): ")

while in_str.lower() != "q":
    dollar_str, cents_str = in_str.split(".")
    dollar_int = int(dollar_str)*100
    cents_int = int(cents_str)
    total_int = dollar_int + cents_int
    paid_int = int(out_str)*100
    change_int = paid_int - total_int

    
    
    
    
    if paid_int < total_int :
        print("Error: insufficient payment.")
        out_str = input("Please enter amount paid (int): ")    
        
    elif total_int <0:
        print("Error: Please enter a positive amount.")
        in_str = input("Enter the purchase price (xx.xx) or `q' to quit: ")
        out_str = input("Please enter amount paid (int): ")
            
    elif paid_int <0:
        print("Error: Please enter a positive amount.")
        out_str = input("Please enter amount paid (int): ")
        
    else:
        
        d_int = change_int
        while change_int >= 25:
            change_int = change_int - 25
            q_stock = quarters - 1
            
        n_int = d_int                
        while d_int >= 10 and d_int <25 :
            d_int = d_int - 10
            d_stock = dimes - 1
              
        p_int = n_int                
        while n_int >= 5 and n_int <10:
            n_int = n_int - 5
            n_stock = nickels - 1
                
            
                        
        while p_int >= 1 and p_int <5:
            p_int = p_int - 1
            p_stock = pennies - 1    
            
            
        print("Take your change below.")
        print("Quarters:" )
        print("Dimes: " )
        print("Nickels: " )
        print("Pennies: " )
        print()
        print("Stock left: ","Quarters: ",q_stock,"Dimes: ", d_stock \
        ,"Nickels: ", n_stock, "Pennies: ", p_stock)
         

    
         
         
    
        in_str = input("Enter the purchase price (xx.xx) or `q' to quit: ")
    
