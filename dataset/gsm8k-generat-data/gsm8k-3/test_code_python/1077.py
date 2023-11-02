def solution():
    """Louie obtained 80% on a math quiz. He had 5 mistakes. How many items were there on the math quiz?"""
    # Calculate the percentage of correct answers
    correct_percentage = 100 - 80

    # Calculate the number of correct answers
    correct_answers = (100 - correct_percentage) / 100

    # Calculate the number of questions on the quiz
    total_questions = round(5 / correct_answers)

    # Display the total number of questions
    result = total_questions
    return result

print(solution())