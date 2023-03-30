import csv
import sqlite3

#okay this does not work lmao


# with open("Data/A_Z Handwritten Data.csv", 'r') as file:
#     csvreader = csv.reader(file)
#     for row in csvreader:
#         print(row)


columns = []
for i in range(764):
    columns.append(f"a{i}")
print(f"letter,{','.join(columns)}")
