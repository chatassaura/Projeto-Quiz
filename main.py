from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    new_q = Question(item['question'], item['correct_answer'])
    question_bank.append(new_q)

# print(question_bank)
# print(question_bank[0].answer)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()


print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(question_bank)}\n")