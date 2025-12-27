# ==== LOGIC BASED Q/A COLLEGE INFORMATION CHATBOT ====

# Predefined answers
answers = {
    "fees": (
        "Fees structure is as follows:\n"
        "- Tuition fee: Rs. 1,50,000 per year\n"
        "- Examination fee: Rs. 5,000 per year\n"
        "- Library & lab charges: Rs. 10,000 per year\n"
        "- Hostel (optional): Rs. 70,000 per year\n"
        "Note: Exact fees may vary by course and year."
    ),

    "library": (
        "Library rules are as follows:\n"
        "- Carry your valid college ID card to enter the library.\n"
        "- Maintain silence and keep your phone on silent mode.\n"
        "- Books must be returned within 14 days to avoid fines.\n"
        "- Any damage or loss of books must be reported and paid for."
    ),

    "timming": (
        "College timing is as follows:\n"
        "- Regular classes: 9:00 AM to 3:30 PM (Mon-Sat).\n"
        "- Students should reach college at least 10-15 minutes early.\n"
        "- Late entry after first period may be marked absent."
    ),

    "dress": (
        "Dress criteria are as follows:\n"
        "- Students must wear proper, decent and formal dress.\n"
        "- Uniform (if applicable) should be worn on all working days.\n"
        "- Shorts, ripped jeans, sleeveless or overly casual clothes are not allowed.\n"
        "- College ID card must be worn and clearly visible at all times."
    ),

    "pass": (
        "Passing criteria are as follows:\n"
        "- Minimum 40-50% marks (as per university rule) required in each subject.\n"
        "- Students must pass both internal assessment and final exam.\n"
        "- Shortage of attendance may make a student ineligible for exams."
    ),

    "admission": (
        "Admission criteria are as follows:\n"
        "- Eligibility: 10+2 with required subjects and minimum percentage.\n"
        "- Admission may be based on entrance exam / merit list.\n"
        "- Required documents: mark sheets, ID proof, photos, and caste/income certificates if applicable."
    ),
}

print("Hi, I am your college FAQ bot.")
print("I can answer about:", list(answers.keys()))
print("Type 'exit' to quit.")

## unknown question saving function (stub)
def log_unknown_question(user_input: str, filename: str = "unknown_queries.txt") -> None:
    with open(filename, "a", encoding="utf-8") as f:
        f.write(user_input + "\n")


def get_response(user_input: str, answer_dict: dict) -> None:
    """Match user input with predefined keywords and print a reply."""
    found = False
    for keyword, reply in answer_dict.items():
        if keyword in user_input:
            print("Agent:", reply)
            found = True
            break

    if not found:
        print("Agent: I'm sorry, I don't understand your question. "
              "Please try asking about fees, library, timing, dress, admission, or passing criteria.")
        log_unknown_question(user_input)
        
while True:
    user_input = input("You: ").lower().strip()

    if user_input == "exit":
        print("Agent: Goodbye!")
        break
    elif user_input == "help":
        print("Agent: I can answer questions about:", ", ".join(answers.keys()))
        continue
    elif user_input in ("hi", "hello"):
        print("Agent: Hello! How can I assist you today?")
        continue
    elif user_input in ("bye", "goodbye"):
        print("Agent: Goodbye! Have a great day!")
        break
    elif user_input in ("thank you", "thanks"):
        print("Agent: Oh! This is my pleasure.")
        continue
    else:
        get_response(user_input, answers)
