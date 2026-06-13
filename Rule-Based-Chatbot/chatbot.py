print("===================================")
print("      RULE BASED CHATBOT")
print("===================================")

print("Hello! I am your chatbot.")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hello! How are you?")

    elif user == "how are you":
        print("Bot: I am fine. Thank you for asking!")

    elif user == "what is your name":
        print("Bot: My name is CodSoft Chatbot.")

    elif user == "who created you":
        print("Bot: I was created using Python.")

    elif user == "help":
        print("Bot: You can ask me simple questions.")

    elif user == "good morning":
        print("Bot: Good Morning! Have a great day.")

    elif user == "good night":
        print("Bot: Good Night! Sweet dreams.")

    elif user == "thank you":
        print("Bot: You're welcome!")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")