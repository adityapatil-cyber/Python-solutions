
# Simple Shop Billing Calculator

print("WELCOME TO OUR SHOP")

n = int(input("How many products? "))

total = 0

for i in range(n):

    print("\nProduct", i + 1)

    name = input("Enter product name: ")

    qty = int(input("Enter quantity: "))

    price = float(input("Enter price: "))

    gst = float(input("Enter GST percentage (example 18): "))

    discount = float(input("Enter discount percentage (0 if none): "))

    amount = qty * price

    amount = amount - (amount * discount / 100)

    tax = amount * gst / 100

    final = amount + tax

    print("\nProduct:", name)

    print("Price:", amount)

    print("GST:", tax)

    print("Final price:", final)

    total = total + final


print("\n----------------------")

print("TOTAL BILL =", round(total, 2))

print("THANK YOU FOR SHOPPING!")
