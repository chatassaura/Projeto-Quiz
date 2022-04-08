# TODO: asking the question
# TODO: Checking if the answer was correct
# TODO: Checking if we're the end of the quiz

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        if self.question_number <= (len(self.question_list)-1):
            return True
        return False

    def check_answer(self, u_answer, q_answer, q_numb):
        if u_answer.lower() == q_answer.lower():
            self.score += 1
            print("You got it right!")
        else:print("That's wrong")
        print(f"The correct answer was: {q_answer}")
        print(f"Your current score is: {self.score}/{q_numb}\n")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(answer, current_question.answer, self.question_number)


