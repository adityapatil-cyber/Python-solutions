
# Vehicle Service Reminder

print("VEHICLE SERVICE REMINDER")

last_service = int(input("Enter kilometre reading at last service: "))

current_reading = int(input("Enter current kilometre reading: "))

if current_reading < last_service:

    print("Invalid kilometre reading")

else:

    distance = current_reading - last_service

    print("\nDistance travelled since last service:", distance, "km")

    if distance >= 15000:

        print("SERVICE REQUIRED!")

        print("Please take your vehicle for servicing.")

        print("Overdue by:", distance - 15000, "km")

    else:

        remaining = 15000 - distance

        print("Your vehicle does not need servicing yet.")

        print("Service due after", remaining, "km")
