
minimum = 5.0
minimum_w = 150.0
maximum = 1.0
maximum_w = 1.0
avg_h = 0
avg_w = 0
count = 0
avg_bmi = 0
max_bmi = 1.0
min_bmi = 300.0

file = open("data1.txt","r")
title = file.readline()
outfile = open("output.txt","w")

print(title.strip(), "{:>8}".format("BMI"),file = outfile)
for line in file:
    line = line.strip()
    height = float(line[12:23])
    weight = float(line[23:35])
    avg_h += height
    avg_w += weight
    count += 1
    bmi = weight/(height**2)
    avg_bmi += bmi
    print(line, "{:>14.2f}".format(bmi),file = outfile)
    if height < minimum:
        minimum = height
    if height > maximum:
        maximum = height
        
    if weight < minimum_w:    
        minimum_w = weight
    if weight > maximum_w:
        maximum_w = weight
    if bmi > max_bmi:
        max_bmi = bmi
    if bmi < min_bmi:
        min_bmi = bmi
        

       
print("",file = outfile)
print("Average","{:>8.2f}".format(avg_h/count),"{:>12.2f}".format(avg_w/count),"{:>14.2f}".format(avg_bmi/count),file = outfile)
print("Max","{:>12.2f}".format(maximum),"{:>12.2f}".format(maximum_w),"{:>14.2f}".format(max_bmi),file = outfile)    
print("Min", "{:>12.2f}".format(minimum),"{:>12.2f}".format(minimum_w),"{:>14.2f}".format(min_bmi),file = outfile)    
    
outfile.close()   


