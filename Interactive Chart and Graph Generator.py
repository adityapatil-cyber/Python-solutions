# Chart Generator

import matplotlib.pyplot as plt

print("CHART GENERATOR")

print("1. Line Graph")
print("2. Bar Graph")
print("3. Pie Chart")
print("4. Histogram")
print("5. Scatter Plot")

choice = int(input("Enter chart number (1-5): "))

title = input("Enter chart title: ")

if choice == 1 or choice == 2 or choice == 3:

    n = int(input("How many data entries? "))

    labels = []
    values = []

    for i in range(n):

        label = input("Enter category or X label: ")
        value = float(input("Enter value: "))

        labels.append(label)
        values.append(value)

    if choice == 1:

        plt.plot(labels, values)

        x_label = input("Enter X-axis label: ")
        y_label = input("Enter Y-axis label: ")

        plt.xlabel(x_label)
        plt.ylabel(y_label)

    elif choice == 2:

        plt.bar(labels, values)

        x_label = input("Enter X-axis label: ")
        y_label = input("Enter Y-axis label: ")

        plt.xlabel(x_label)
        plt.ylabel(y_label)

    elif choice == 3:

        plt.pie(values, labels=labels, autopct="%1.1f%%")


elif choice == 4:

    n = int(input("How many numbers? "))

    values = []

    for i in range(n):

        value = float(input("Enter number: "))
        values.append(value)

    plt.hist(values)

    plt.xlabel("Values")
    plt.ylabel("Frequency")


elif choice == 5:

    n = int(input("How many data points? "))

    x_values = []
    y_values = []

    for i in range(n):

        x = float(input("Enter X value: "))
        y = float(input("Enter Y value: "))

        x_values.append(x)
        y_values.append(y)

    plt.scatter(x_values, y_values)

    x_label = input("Enter X-axis label: ")
    y_label = input("Enter Y-axis label: ")

    plt.xlabel(x_label)
    plt.ylabel(y_label)


else:

    print("Invalid chart choice")


if choice >= 1 and choice <= 5:

    plt.title(title)
    plt.show()
