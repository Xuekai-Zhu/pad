def solution():
    num_questions = 50
    problem_solving_percent = 0.8

    # Calculate the number of problem-solving questions
    num_problem_solving = num_questions * problem_solving_percent

    # Calculate the number of multiple-choice questions
    num_multiple_choice = num_questions - num_problem_solving
    result = num_multiple_choice
    return result

print(solution())