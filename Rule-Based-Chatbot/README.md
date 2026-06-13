# Rule-Based Chatbot

## Project Overview

This project is a simple Rule-Based Chatbot developed using Python. The chatbot interacts with users by responding to predefined questions and commands using if-else statements.

The project demonstrates the basic concepts of Natural Language Processing (NLP), conversation flow, and user interaction.

## Features

- Greets users
- Responds to common questions
- Provides predefined answers
- Handles unknown inputs
- Allows users to exit the conversation using "bye"

## Technologies Used

- Python 3

## Project Structure

```
Rule-Based-Chatbot/
│
├── chatbot.py
└── README.md
```

## How It Works

The chatbot continuously accepts user input and compares it with predefined rules.

If the input matches a known command, the chatbot provides the corresponding response. Otherwise, it displays a default message.

## Supported Commands

| User Input | Chatbot Response |
|------------|------------------|
| hello / hi | Hello! How are you? |
| how are you | I am fine. Thank you for asking! |
| what is your name | My name is CodSoft Chatbot. |
| who created you | I was created using Python. |
| help | You can ask me simple questions. |
| good morning | Good Morning! Have a great day. |
| good night | Good Night! Sweet dreams. |
| thank you | You're welcome! |
| bye | Goodbye! Have a nice day. |

## How to Run

1. Install Python 3.
2. Download or clone the project.
3. Open the terminal in the project folder.
4. Run the following command:

```bash
python chatbot.py
```

## Sample Output

```
===================================
      RULE BASED CHATBOT
===================================

Hello! I am your chatbot.
Type 'bye' to exit.

You: hello
Bot: Hello! How are you?

You: what is your name
Bot: My name is CodSoft Chatbot.

You: bye
Bot: Goodbye! Have a nice day.
```

## Learning Outcomes

- Understanding rule-based chatbots
- Basic Natural Language Processing concepts
- Python conditional statements
- User input handling
- Conversation flow design

## Future Improvements

- Add more responses and commands
- Implement pattern matching
- Add GUI using Tkinter
- Integrate speech recognition
- Connect with AI APIs for advanced conversations

## Author

Created as part of the CodSoft Artificial Intelligence Internship Program.

## License

This project is developed for educational and internship purposes.