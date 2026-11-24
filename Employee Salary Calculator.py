
# Employee Salary Calculator

print("EMPLOYEE SALARY CALCULATOR")

name = input("Enter employee name: ")

basic = float(input("Enter basic salary: "))

hra = basic * 30 / 100

da = basic * 20 / 100

pf = basic * 12 / 100

net_salary = basic + hra + da - pf

print("\n----- SALARY DETAILS -----")

print("Employee Name:", name)

print("Basic Salary:", basic)

print("HRA:", hra)

print("DA:", da)

print("PF:", pf)

print("--------------------------")

print("NET SALARY:", net_salary)
