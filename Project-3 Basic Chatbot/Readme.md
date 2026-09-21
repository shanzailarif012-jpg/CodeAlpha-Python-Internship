# Basic Chatbot

A simple rule-based chatbot built in Python that responds to predefined user inputs with fixed replies. Built as **Project 3** for the CodeAlpha Python Internship.

## 📌 Description

This program runs a command-line chat loop where the user types messages and receives predefined replies based on matching keywords/phrases. It uses a function with `if-elif-else` logic to determine the appropriate response, and continues chatting until the user types "bye".

## ✨ Features

- Responds to common greetings and phrases (e.g. "hello", "how are you", "bye")
- Handles a few extra conversational inputs (name, capabilities, good morning)
- Falls back to a default response for unrecognized input
- Case-insensitive matching (input is normalized before checking)
- Chat loop automatically ends when the user types "bye"

## 🛠️ Concepts Used

- Functions (`def`, `return`)
- `if` / `elif` / `else` conditional logic
- `while` loops and `break`
- Input/output handling
- String methods (`.strip()`, `.lower()`)

## ▶️ How to Run

```bash
python3 chatbot.py
```

Simply type a message when prompted. Try:
- `hello`
- `how are you`
- `what's your name`
- `what can you do`
- `good morning`
- `bye` (ends the chat)

## 💬 Sample Conversation

```
Enter Chat to talk: hello
Hi!
Enter Chat to talk: how are you
I'm fine, Thanks!
Enter Chat to talk: bye
GoodBye!
```

## 👤 Author

CodeAlpha Python Internship — Project 3