import os
import csv

election_data_csv = os.path.join("02-Homework","03-Python","Instructions","PyPoll","Resources","election_data.csv")
with open(election_data_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)

    #Declare Variables
    Total_votes = 0
    Votes_percentage = 0
    Cand_list = []
    Cand_votes = []
    Winner = []
    Unique_cand = []
    Percentage = []


    for row in csv_reader:
        Total_votes = Total_votes + 1
        Cand_list.append(row[2])
    for x in set(Cand_list):
        Unique_cand.append(x)
        y = Cand_list.count(x)
        Cand_votes.append(y)
        Votes_percentage = int((y / Total_votes) * 100)
        Percentage.append(Votes_percentage)

Max_count = max(Cand_votes)
Winner = Unique_cand[Cand_votes.index(Max_count)]

print("Election Results")   
print("-------------------------")
print("Total Votes:" + " " + str(Total_votes))
print("-------------------------")

for i in range(len(Unique_cand)):
    print(Unique_cand[i] + ": " + str(Percentage[i]) +"%" + " " + str(Cand_votes[i]))

print("-------------------------")
print("Winner:" + " " + Winner)
print("-------------------------")



with open('election_data.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("-------------------------\n")
    text.write("Total Votes:" + " " + str(Total_votes) + "\n")
    text.write("-------------------------\n")

    for i in range(len(set(Unique_cand))):
        text.write(Unique_cand[i] + ": " + str(Percentage[i]) +"% (" + str(Cand_votes[i]) + ")\n")

    text.write("-------------------------\n")
    text.write("Winner: " + " " + Winner + "\n")
    text.write("-------------------------\n")
    