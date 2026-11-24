
# Personal Data Storage System

import pandas as pd

print("PERSONAL DATA STORAGE SYSTEM")

print("\nFirst, see the table structure:")

print("+-------------+-------------+-------------+")
print("| Row Label   | Column 1    | Column 2    |")
print("+-------------+-------------+-------------+")
print("| Row 1       | Data        | Data        |")
print("| Row 2       | Data        | Data        |")
print("+-------------+-------------+-------------+")

columns = int(input("\nHow many columns do you want? "))

column_names = []

for i in range(columns):

    name = input("Enter column name: ")

    column_names.append(name)


rows = int(input("\nHow many rows do you want? "))

data = {}

for column in column_names:

    values = []

    print("\nEnter data for", column)

    for i in range(rows):

        value = input("Enter value for row " + str(i + 1) + ": ")

        values.append(value)

    data[column] = values


row_labels = []

print("\nNow enter row labels:")

for i in range(rows):

    label = input("Enter label for row " + str(i + 1) + ": ")

    row_labels.append(label)


table = pd.DataFrame(data, index=row_labels)

print("\nYOUR COMPLETE TABLE")

print(table)

table.to_csv("my_table.csv")

print("\nYour data has been saved in my_table.csv")
