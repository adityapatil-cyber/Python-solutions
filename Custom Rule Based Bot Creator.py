# Custom Rule-Based Chatbot Generator

print("WELCOME TO CHATBOT CREATOR")

bot_name = input("Enter your chatbot name: ")

n = int(input("How many questions do you want to add? "))

questions = []
answers = []

for i in range(n):

    print("\nRule", i + 1)

    question = input("Enter a question or keyword: ").lower()

    answer = input("Enter the chatbot's reply: ")

    questions.append(question)
    answers.append(answer)


print("\nYour chatbot is ready!")
print("You can now start chatting with", bot_name)
print("Type 'bye' to stop.\n")


while True:

    user = input("You: ").lower()

    if user == "bye":

        print(bot_name + ": Goodbye!")
        break

    found = False

    for i in range(n):

        if questions[i] in user:

            print(bot_name + ":", answers[i])
            found = True
            break

    if found == False:

        print(bot_name + ": Sorry, I don't know that yet.")
