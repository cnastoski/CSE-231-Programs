






in_str = input("Please enter squares, cubes, or power: ")


def squares(s_number,s_terms):   
    total = 0
    for i in range(s_terms):
        total += (s_number)**2 
        s_number += 1   
    return total    

def cubes(c_number,c_terms):
    total = 0
    for i in range(c_terms):
        total+= (c_number)**3
        c_number += 1
    return total

def power(p_number,p_terms,p_exp):
    total = 0
    for i in range(p_terms):
        total += (p_number)**p_exp
        p_number += 1
    return total
        





while in_str.lower() != "exit":
        
        
        if in_str.lower() == "squares":
            s_nstr = input("Please enter the initial number in the series: ")
            s_tstr = input("Please enter the amount of terms: ")
            s_number = int(s_nstr)
            s_terms = int(s_tstr)
            print(squares(s_number,s_terms))
            in_str = input("Please enter squares, cubes, or power: ")
            
        if in_str.lower() == "cubes":
            c_nstr = input("Please enter the initial number in the series: ")
            c_tstr = input("Please enter the amount of terms: ")
            c_number = int(c_nstr)
            c_terms = int(c_tstr)
            print(cubes(c_number,c_terms))
            in_str = input("Please enter squares, cubes, or power: ")

        if in_str.lower() == "power":
            p_nstr = input("Please enter the initial number in the series: ")
            p_tstr = input("Please enter the amount of terms: ")
            p_estr = input("Please enter the exponent to raise to: ")
            p_exp = int(p_estr)
            p_number = int(p_nstr)
            p_terms = int(p_tstr)
            print(power(p_number,p_terms,p_exp))
            in_str = input("Please enter squares, cubes, or power: ")
            
    
        else:
            print("***invalid choice***")
            in_str = input("Please enter squares, cubes, or power: ")
    
    
else:
    print("Progrem halted normally")
    quit






