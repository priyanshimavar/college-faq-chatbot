# Logic-Based Q/A College Information Chatbot

A simple rule-based chatbot built with Python that answers frequently asked questions about college information such as fees, library rules, class timings, dress code, admission, and passing criteria.

## Features

- Answers predefined questions about:
  - Fees
  - Library
  - Timing
  - Dress code
  - Admission
  - Passing criteria
- Rule-based keyword matching (no machine learning needed)
- Simple text interface (runs in terminal or Google Colab)
- Default fallback message when the question is not understood

## How It Works

- A Python dictionary `answers` stores predefined replies for each topic.  
- The program reads user input in a loop, converts it to lowercase, and removes extra spaces.  
- Special commands like `hi`, `help`, `bye`, and `exit` are handled with `if/elif` rules.  
- For other inputs, the chatbot checks if any keyword (e.g. `"fees"`, `"library"`) appears in the user’s message and prints the corresponding answer.  
- If no keyword matches, it shows a default message suggesting supported topics.

## Getting Started

1. Clone or download this repository.
2. Make sure you have **Python 3** installed.
3. Run the script: python chatbot.py
4. Type your questions (for example: `fees`, `library rules`, `what is the dress code?`).
5. Type `exit` or `bye` to quit the chatbot.

## Example
You: hi
Agent: Hello! How can I assist you today?
You: tell me about fees
Agent: Fees structure is as follows:
Tuition fee: Rs. 1,50,000 per year
Examination fee: Rs. 5,000 per year
Library & lab charges: Rs. 10,000 per year
Hostel (optional): Rs. 70,000 per year
Note: Exact fees may vary by course and year.


## Learning Outcomes

- Practiced Python basics: dictionaries, loops, functions, and string handling.
- Understood how rule-based chatbots work using simple keyword matching.
- Built a small AI agent suitable for academic projects and beginner portfolios.




