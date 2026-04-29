def run_quiz(questions):
    score = 0

    for i, q in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {q['question']}")
        
        for option in q['options']:
            print(option)
        
        answer = input("Your answer (A/B/C/D): ").upper()

        if answer == q['answer']:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer is {q['answer']}")

    print("\n🎯 Quiz Completed!")
    print(f"Your Score: {score}/{len(questions)}")


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
    }
]

run_quiz(questions)
