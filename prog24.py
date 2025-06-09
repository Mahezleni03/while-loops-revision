print("🧠 Welcome to Quiz Game!")
score = 0
question_no = 0
questions = [["What is capital of India","Dheli"],["Who wrote the Romeo and Juliet","Shakesphere"],["What is 236 + 24","260"],["Which is the hottest planet in the solar system","Venus"],["Which is the brain of the computer","CPU"]]

while question_no < len(questions):
    print("\n Question",question_no + 1)
    print(questions[question_no[0]])
    ans = input("Your Name : ").strip().lower()
    if ans == questions[question_no][1]:
        print("✅ Correct Answer")
        score = score + 1
    else:
        print("❌ Incorrect Answer",questions[question_no][1])

    question_no += 1
print("\n Quiz Completed")
print("Your final score is",score,"/",len(questions))