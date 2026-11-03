def get_reply(message):
    """Return a predefined reply based on the user's message."""
    message = message.strip().lower()

    if message in ("hello", "hi", "hey"):
        return "Hi!"
    elif message == "how are you":
        return "I'm fine, thanks!"
    elif message in ("what is your name", "who are you", "your name"):
        return "I'm a simple chatbot."
    elif message in ("thanks", "thank you"):
        return "You're welcome!"
    elif message in ("bye", "goodbye", "exit", "quit"):
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."


def main():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        reply = get_reply(user_input)
        print(f"Chatbot: {reply}")

        if reply == "Goodbye!":
            break


if __name__ == "__main__":
    main()