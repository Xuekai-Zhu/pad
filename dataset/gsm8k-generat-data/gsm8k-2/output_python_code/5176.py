def solution():
    """Sylvia had one-fifth of incorrect answers in the exam, while Sergio got 4 mistakes. If there were 50 questions, how many more correct answers does Sergio have than Sylvia?"""
    total_questions = 50
    sylvia_incorrect_answers = total_questions * (1/5)
    sylvia_correct_answers = total_questions - sylvia_incorrect_answers
    sergio_correct_answers = total_questions - 4
    difference = sergio_correct_answers - sylvia_correct_answers
    result = difference
    return result

print(solution())