questions = [
    {
        "question": "1. What is the capital of Pakistan?",
        "options": ["A. Lahore", "B. Islamabad", "C. Karachi", "D. Peshawar"],
        "answer": "B",
        "prize": 1000
    },
    {
        "question": "2. Who is the founder of Pakistan?",
        "options": ["A. Allama Iqbal", "B. Liaquat Ali Khan", "C. Quaid-e-Azam", "D. Sir Syed Ahmed Khan"],
        "answer": "C",
        "prize": 5000
    },
    {
        "question": "3. Which language is used for web apps?",
        "options": ["A. Python", "B. Java", "C. JavaScript", "D. C++"],
        "answer": "C",
        "prize": 10000
    }
]

total_amount = 0

print("===== Welcome to KBC Game =====")

for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()

    if user_answer == q["answer"]:
        print("Correct Answer!")
        total_amount += q["prize"]
    else:
        print("Wrong Answer! Game Over.")
        break

print(f"\nYou are taking home: Rs. {total_amount}")