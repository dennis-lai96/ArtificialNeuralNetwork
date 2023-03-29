import csv

#okay this does not work lmao
with open("Data/A_Z Handwritten Data.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        print(row)