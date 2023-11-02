def solution():
    """On Miss Lawrence's math exam, 80% of the 50 questions are problem-solving while the rest are multiple-choice questions. How many multiple-choice questions are there?"""
    # Define the total number of questions and the percentage of problem-solving questions
    total_questions = 50
    problem_solving_percentage = 80

    # Calculate the number of problem-solving questions
    problem_solving_questions = total_questions * (problem_solving_percentage / 100)

    # Calculate the number of multiple-choice questions
    multiple_choice_questions = total_questions - problem_solving_questions

    # Display the number of multiple-choice questions
    result = multiple_choice_questions
    return result

print(solution())