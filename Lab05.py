vowels_str = "aeiouy"

def vowel_count(vowels_str,line):
    vowels = 0
    for ch in line:
        if ch in vowels_str:
            vowels +=1 
    return vowels

file_obj = open("dictionary.txt","r")
for line in file_obj:
    line = line.strip()
    if line.islower():
        if len(line) == 7:
            if "s" not in line:
                if vowel_count(vowels_str,line) == 1:
                    print(line)
                    
file_obj.close()

input()

a = "a"
e = "e"
i = "i"
o = "o"
u = "u"

#def a_count(a,line):
#    a_str = 0
#    for ch in line:
#        if ch == "a":
#            a_str += 1
#    return a_str
#    
#def e_count(e,line):
#    e_str = 0
#    for ch in line:
#        if ch == "e":
#            e_str += 1
#    return e_str
#    
#def i_count(i,line):
#    i_str = 0
#    for ch in line:
#        if ch == "i":
#            i_str += 1
#    return i_str
#    
#def o_count(o,line):
#    o_str = 0
#    for ch in line:
#        if ch == "o":
#            o_str += 1
#    return o_str
#    
#def u_count(u,line):
#    u_str = 0
#    for ch in line:
#        if ch == "u":
#            u_str += 1
#    return u_str
    
file_obj = open("dictionary.txt","r")


for line in file_obj:
    line = line.strip().lower()
    letters = ''
    for ch in line:
        if ch in "aeiou":
            letters += ch
    if letters == "aeiou":
        print(line)


#for line in file_obj:
#    line = line.strip()
#    if a_count(a,line) == 1:
#        if e_count(e,line) == 1: 
#            if i_count(i,line) == 1:
#                if o_count(o,line) == 1: 
#                    if u_count(u,line) == 1:
#                        if line.find(a) < line.find(e):
#                            if line.find(e) < line.find(i):
#                                if line.find(i) < line.find(o):
#                                    if line.find(o) < line.find (u):
#                                        print(line)

file_obj.close()
        
        
        
        
        
        
        
        
        
        
        