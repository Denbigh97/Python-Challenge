
# library imports
import os
import csv
import math


# path of file
elections = os.path.join("resources", "elections.csv")

#read csv
with open (elections,'r', newline="") as csvfile:
    #csv reader file
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    print("Poll Results")
    print("---------------------------")
    
    header = next(csvreader)
    
    #variables
    khancount = 0
    khanpercent = 0.00
    correycount = 0
    correypercent = 0.00
    licount = 0
    lipercent = 0.00
    otooleycount = 0
    otooleypercent = 0.00
    winnercount = 0
    totalcount = 0
    winner = ""
    for row in csvreader:
        totalcount = totalcount + 1
        if(row[2] == "Khan"): # +1 vote for Khan
            khancount = khancount + 1
        elif (row[2] == "Correy"): # +1 vote for Correy
            correycount = correycount + 1
        elif (row[2] == "Li"): # +1 vote for Li
            licount = licount + 1
        elif (row[2] == "O'Tooley"): # +1 vote for O'Tooley
            otooleycount = otooleycount + 1
# percentage over the total
khanpercent = khancount / totalcount * 100
correypercent = correycount / totalcount * 100
lipercent = licount / totalcount * 100
otooleypercent = otooleycount / totalcount * 100
# name of canidiate
winnercount = max(khancount, correycount, licount, otooleycount)
if(winnercount == khancount):
    winner = "Khan" 
elif(winnercount == correycount):
    winner = "Correy"
elif(winnercount == licount):
    winner = "Li"
else:
    winner = "O'Tooley"

#print totaly 
print ('total', totalcount)
print ('khan', khancount)
print ('correy', correycount)
print ('li', licount)
print ('otooley', otooleycount)
print('----------------------------')

print ('khan', khanpercent)
print ('correy', correypercent)
print ('li', lipercent)
print ('otooley', otooleypercent)
print('-------------------------------')
print ('electionwinner', winner)





   # output to a text file

file = open("output.txt","w")

file.write("election results" + "\n")

file.write("...................................................................................." + "\n")

file.write("\ntotalcount: " + str(totalcount))

file.write("\n----------------------------------------------------------------------------")

file.write("\nKhan:" + " " + str(round(khanpercent[0],3)) + "%" + "("+str(khancount[0])+")")
file.write("\nCorrey:" + " " + str(round(correypercent[1],3)) + "%" + "("+str(correycount[1])+")")
file.write("\nLi:" + " " + str(round(lipercent[2],3)) + "%" + "("+str(licount[2])+")")
file.write("\nO'Tooley:" + " " + str(round(otooleypercent[3],3)) + "%" + "("+str(otooleycount[3])+")")
file.write("\n----------------------------------------------------------------------------------------")
file.write("\nwinner: " + winner)
file.close()