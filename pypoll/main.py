import os
import csv
#import numpy as np

#path to file location
csvpath = os.path.join('..','pypoll','election_data.csv')

#assignvariables
khan_votes=0
correy_votes=0
li_votes=0
otooley_votes=0
totalvotes= 0
khan_percentage = []
correy_percentage = []
otooley_percentage = []
li_percentage = []

#open file, read file
with open(csvpath, newline='') as file:   
    csvreader = csv.reader(file, delimiter=',')
    header = next(csvreader)
    #calculating the total rows by looping through the file
    for row in csvreader:
        totalvotes +=1
        if row[2] =="Khan":
            khan_votes +=1
        elif row[2] =="Correy":
            correy_votes +=1
        elif row[2] =="O'Tooley":
            otooley_votes +=1

#creating lists for candidates and candidate votes

candidates = ["Khan", "O'Tooley", "Correy", "Li"]
votes_percandidate =[khan_votes, otooley_votes, correy_votes, li_votes]

#zipping the lists and creating a dictionary

zipped_dict = dict(zip(candidates, votes_percandidate))
winner_votes = max(zipped_dict, key=zipped_dict.get)

#calculating percentages of vote
khan_percentage.append(round(khan_votes/totalvotes * 100,5))
otooley_percentage.append(round(otooley_votes/totalvotes * 100,5))
correy_percentage.append(round(correy_votes/totalvotes *100,5))
li_percentage.append(round(li_votes/totalvotes *100,5))


#printing of Results
print("   Election Results   ")
print("-----------------------")
print(f" Total votes: {totalvotes}")
print("-----------------------")
print(f"Khan: {khan_percentage:}% ({khan_votes})")
print(f"Correy: {correy_percentage:}% ({correy_votes})")
print(f"LI: {li_percentage:}% ({li_votes})")
print(f"O'Tooley: {otooley_percentage:}% ({otooley_votes})")
print(f"------------------------")
print(f"Winner: {winner_votes}")
print(f"------------------------")

#output file

outputfile = os.path.join('..', 'pypoll', 'newanalysis.txt')
with open(outputfile, "w") as newfile:
    newfile.write("Election Results")
    newfile.write("\n")
    newfile.write("-----------------")
    newfile.write("\n")
    newfile.write(f" Total votes: {totalvotes}")
    newfile.write("\n")
    newfile.write("-----------------")
    newfile.write("\n")
    newfile.write(f"Khan: {khan_percentage:}% ({khan_votes})")
    newfile.write("\n")
    newfile.write(f"Correy: {correy_percentage:}% ({correy_votes})")
    newfile.write("\n")
    newfile.write(f"LI: {li_percentage:}% ({li_votes})")
    newfile.write("\n")
    newfile.write(f"O'Tooley: {otooley_percentage:}% ({otooley_votes})")
    newfile.write("\n")
    newfile.write(f"Winner: {winner_votes}")
    newfile.write("\n")

