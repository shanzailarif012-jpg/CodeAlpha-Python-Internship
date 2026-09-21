                # Project- 3 Basic Chatbot 
                # Goal: Build a simple rule-based chatbot

def get_response(user_input):
    if user_input == "hello":
        return "Hi!"
    
    elif user_input == "how are you":
        return "I'm fine, Thanks!"

    elif user_input == "what's your name":
        return "I'm a chatbot made in Python!"

    elif user_input == "what can you do":
        return "I can chat with you about a few basic things!"
    
    elif user_input == "good morning":
        return "Good morning to you too!"
    
    elif user_input == "bye":
        return "GoodBye!"
    
    else:
        return "Sorry, I don't understand that."

    
while True:
    user_input = input("Enter Chat to talk: ").strip().lower()

    reply = get_response(user_input)
    print(reply)

    if user_input == "bye":
        break

