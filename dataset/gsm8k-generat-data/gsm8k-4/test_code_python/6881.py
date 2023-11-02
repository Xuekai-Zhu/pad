def solution():
    """On Miss Lawrence's math exam, 80% of the 50 questions are problem-solving while the rest are multiple-choice questions. How many multiple-choice questions are there?"""
    # Define the total number of questions and the percentage of problem-solving questions
    total_questions = 50
    problem_percent = 80

    # Calculate the number of problem-solving questions and the number of multiple-choice questions
    problem_questions = total_questions * (problem_percent / 100)
    mc_questions = total_questions - problem_questions

    # return the result
    result = mc_questions
    return result

print(solution())