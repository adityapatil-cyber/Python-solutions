
# Simple Rule-Based Chatbot

print("WELCOME TO OUR CHATBOT")

print("You can ask me about:")
print("1. School timing")
print("2. Courses")
print("3. Holidays")
print("4. Contact")
print("Type bye to exit.")

while True:

    question = input("\nYou: ")

    question = question.lower()

    if question == "hello" or question == "hi":

        print("Bot: Hello! How can I help you?")

    elif question == "timing":

        print("Bot: School timing is 8 AM to 2 PM.")

    elif question == "courses":

        print("Bot: We offer Science, Commerce and Arts.")

    elif question == "holidays":

        print("Bot: Please check the school holiday calendar.")

    elif question == "contact":

        print("Bot: Contact the school office for information.")

    elif question == "bye":

        print("Bot: Goodbye! Have a nice day.")

        break

    else:

        print("Bot: Sorry, I do not understand.")
