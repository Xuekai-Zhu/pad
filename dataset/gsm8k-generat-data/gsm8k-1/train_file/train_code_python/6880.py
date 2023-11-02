def solution():
    """On Miss Lawrence's math exam, 80% of the 50 questions are problem-solving while the rest are multiple-choice questions. How many multiple-choice questions are there?"""
    total_questions = 50
    problem_solving_questions = total_questions * 0.8
    multiple_choice_questions = total_questions - problem_solving_questions
    result = multiple_choice_questions
    return result

print(solution())