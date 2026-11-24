
# Student Marks Analyzer

import pandas as pd

print("STUDENT RESULT ANALYZER")

n = int(input("Enter number of students: "))

names = []
maths = []
science = []
ai = []

for i in range(n):

    print("\nStudent", i + 1)

    name = input("Enter student name: ")

    m = float(input("Enter Maths marks: "))

    s = float(input("Enter Science marks: "))

    a = float(input("Enter AI marks: "))

    names.append(name)

    maths.append(m)

    science.append(s)

    ai.append(a)


total_marks = []

average_marks = []

for i in range(n):

    total = maths[i] + science[i] + ai[i]

    average = total / 3

    total_marks.append(total)

    average_marks.append(average)


data = {
    "Name": names,
    "Maths": maths,
    "Science": science,
    "AI": ai,
    "Total": total_marks,
    "Average": average_marks
}

result = pd.DataFrame(data)

print("\nCOMPLETE RESULT")

print(result)

top_position = average_marks.index(max(average_marks))

print("\nHighest Average:", max(average_marks))

print("Top Student:", names[top_position])
