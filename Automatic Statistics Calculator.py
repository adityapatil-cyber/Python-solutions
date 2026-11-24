
# Statistics Calculator

import statistics

print("STATISTICS CALCULATOR")

n = int(input("How many numbers do you want to enter? "))

numbers = []

for i in range(n):

    value = float(input("Enter number: "))

    numbers.append(value)


if n > 0:

    print("\nSTATISTICAL RESULTS")

    print("Mean:", statistics.mean(numbers))

    print("Median:", statistics.median(numbers))

    print("Mode:", statistics.mode(numbers))

    if n >= 2:

        print("Variance:", statistics.variance(numbers))

        print("Standard Deviation:", statistics.stdev(numbers))

    else:

        print("Enter at least two numbers for variance and standard deviation.")

else:

    print("Please enter at least one number.")
