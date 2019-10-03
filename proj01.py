############################################################
#  Computer Project #1
#   
#   Algorithm
#    Prompt for input of a floating point number
#    Convert float point to various units
#    Output conversions
#
#
#############################################################

rod_str = input("Enter Distance to Travel(in Rods):")
rod_float = float(rod_str)    #converts input into a floating point number


print("Your Input:", rod_float, "Rods")      #reprinted float input


print("Your Conversions")
print("Meters", (rod_float*5.0292))         #printed conversions 
print("Feet", (rod_float*5.0292)/0.3048)
print("Miles:", (rod_float*5.0292)/1609.34)
print("Furlongs:", (rod_float/40))
print("Time to Walk", rod_float, "Rods Is:" ,\
      rod_float/(3.1*1609.34/5.0292/60), "Minutes")