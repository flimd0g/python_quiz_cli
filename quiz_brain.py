class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list


    @property
    def still_has_questions(self):
        self.final_q = len(self.question_list)
        if self.question_number == self.final_q:
            return False
        else:
            return True


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}. (True or False?): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
            print(f"Your score is {self.score}/{self.question_number}")
        else:
            print("That's wrong.")
            print(f"Your score is {self.score}/{self.question_number}")
        print(f"The correct answer was {correct_answer}")
        print("\n")
