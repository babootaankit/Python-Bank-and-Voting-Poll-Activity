#import modules
import os
import csv

budget_data_csv = os.path.join("02-Homework", "03-Python", "Instructions", "PyBank", "Resources", "budget_data.csv")

#declare variable and lists
Line_count = 0
Net_total = 0
Average = 0
Previous_net = 0

Net_Change = []
Net_Change_List = []
Months_change = []
Change_date = []

#open csv  
with open(budget_data_csv) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        csv_header = next(csv_reader)
    


        for row in csv_reader:    
            #count number of months    
            Line_count = Line_count + 1
            Net_total = Net_total + int(row[1])
            #track the net change
            basic_net_change = int(row[1])- Previous_net
            Previous_net = int(row[1])
            #Find average change
            Net_Change_List.append(basic_net_change)
            Months_change += row[1]
            
            Average = sum(Net_Change_List)/len(Net_Change_List)
            
            #find greateast increase and decrease
            greatest_increase = max(Net_Change_List)
            greatest_decrease = min(Net_Change_List)

            Change_date.append(row[0])

            dateof_greatest_increase = Change_date[Net_Change_List.index(greatest_increase)]
            dateof_greatest_decrease = Change_date[Net_Change_List.index(greatest_decrease)]

print("Financial Analysis")
print("--------------------------------------------------")                
print("Total Months:" + " " + str(Line_count))
print("Total:" + " "+ "$" + str(Net_total))
print("Average Change:" + " " + "$" + str(Average))
print("Greatest increase in profits:" + " " + str(dateof_greatest_increase) + " " + "$" + str(greatest_increase))
print("Greatest decrease in profits:" + " " + str(dateof_greatest_decrease) + " " + "$" + str(greatest_decrease))


with open('budget_data.txt', 'w') as text:
    text.write("  Financial Analysis"+ "\n")
    text.write("--------------------------------------------------\n\n")
    text.write("Total Months:" + " " + str(Line_count) + "\n")
    text.write("Total:" + "$" + str(Net_total) +"\n")
    text.write("Average Change:" + " " + "$" + str(int(Average)) + "\n")
    text.write("Greatest Increase in Profits:" + " " + str(dateof_greatest_increase) + "$" + str(greatest_increase) + "\n")
    text.write("Greatest Decrease in Profits:" + " " + str(dateof_greatest_decrease) + "$" + str(greatest_decrease) + "\n")
   
