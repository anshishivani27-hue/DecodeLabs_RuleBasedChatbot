import time

print("=" * 40)
print("🤖 Welcome to DecodeBot!")
print("=" * 40)
print("Type 'help' to see available commands.\n")

while True:
    user = input("You: ").lower()

    if user == "hi" or user == "hello" or user == "hii":
        print("Bot: Hello! Nice to meet you. 😊")

    elif user == "good morning":
        print("Bot: Good Morning! Have a wonderful day ahead! ☀️")

    elif user == "good afternoon":
        print("Bot: Good Afternoon! Hope your day is going well. 😊")

    elif user == "good evening":
        print("Bot: Good Evening! Hope you had a great day. 🌇")

    elif user == "how are you":
        print("Bot: I'm doing great! Thanks for asking. How about you?")

    elif user == "what is your name":
        print("Bot: My name is DecodeBot.")

    elif user == "who created you":
        print("Bot: I was created by Ankam Shivani.")

    elif user == "what can you do":
        print("Bot: I can greet you, tell the time, answer simple questions, and chat with you!")

    elif user == "time":
        print("Bot: Current Time is", time.strftime("%H:%M:%S"))

    elif user == "date":
        print("Bot: Today's Date is", time.strftime("%d-%m-%Y"))

    elif user == "thank you" or user == "thanks":
        print("Bot: You're welcome! 😊")

    elif user == "help":
        print("\n📋 Available Commands:")
        print("- hi / hello / hii")
        print("- good morning")
        print("- good afternoon")
        print("- good evening")
        print("- how are you")
        print("- what is your name")
        print("- who created you")
        print("- what can you do")
        print("- time")
        print("- date")
        print("- thank you")
        print("- bye\n")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day. 👋")
        break

    else:
        print("Bot: Sorry, I don't understand that. Type 'help' to see available commands.")