import random
def ask_question(q, index):
    print(f"\nQuestion {index}: {q['question']}")
    
    for option in q['options']:
        print(option)

    while True:
        answer = input("Your answer (A/B/C/D): ").upper()
        if answer in ['A', 'B', 'C', 'D']:
            break
        else:
            print("⚠️ Please enter a valid option (A, B, C, or D).")

    if answer == q['answer']:
        print("✅ Correct!")
        return 1
    else:
        print(f"❌ Wrong! Correct answer is {q['answer']}")
        return 0


def run_quiz(questions):
    score = 0
    random.shuffle(questions)

    for i, q in enumerate(questions, start=1):
        score += ask_question(q, i)

    total = len(questions)
    percentage = (score / total) * 100

    print("\n🎯 Quiz Completed!")
    print(f"Score: {score}/{total}")
    print(f"Percentage: {percentage:.2f}%")

    if percentage == 100:
        print("🔥 Excellent! Perfect score!")
    elif percentage >= 70:
        print("👏 Great job!")
    elif percentage >= 40:
        print("👍 Not bad, keep practicing!")
    else:
        print("💡 Try again to improve!")


def play():
    questions = [
        {
            "question": "What is the capital of India?",
            "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
            "answer": "B"
        },
        {
            "question": "Which language is used for AI?",
            "options": ["A. Python", "B. HTML", "C. CSS", "D. Excel"],
            "answer": "A"
        },
        {
            "question": "2 + 2 * 2 = ?",
            "options": ["A. 6", "B. 8", "C. 4", "D. 10"],
            "answer": "A"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Earth", "B. Mars", "C. Venus", "D. Jupiter"],
            "answer": "B"
        }
    ]

    while True:
        run_quiz(questions)

        again = input("\n🔁 Do you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("👋 Thanks for playing!")
            break


play()
