import os
import csv

csvpath = os.path.join("..", "Resources", "budget_data.csv")

with open(csvpath, newline='') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    rows = 0
    total = 0
    previous = 0
    greatest_increase = 0 
    greatest_in_month = ""
    greatest_decrease = 0
    greatest_de_month = ""
    change = []
    for row in csvreader:
        # print (row)
        total += int(row[1])
        rows = rows+1
        change.append(int(row[1]) - previous)
        if previous != 0:
            if (int(row[1]) - previous)>greatest_increase:
                greatest_increase = (int(row[1]) - previous)
                greatest_in_month = row[0]
            if (int(row[1]) - previous)<greatest_decrease:
                greatest_decrease = (int(row[1]) - previous)
                greatest_de_month = row[0]
        previous = int(row[1])
    print("total months: ", rows, "\ntotal: $", total)
    print("Average Change: $",round(sum(change[1:])/len(change[1:]),2))
    print(greatest_in_month, greatest_increase)
    print(greatest_de_month, greatest_decrease)

output = "total months: " + str(rows) + "\ntotal: $" + str(total) + "\nAverage Change: $" + str(round(sum(change[1:])/len(change[1:]),2)) + "\ngreatest_increase, greatest_in_month" + "\ngreatest_de_month, greatest_decrease"
print(output)
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)