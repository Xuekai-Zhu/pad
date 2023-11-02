def solution():
    # Calculate the number of problem-solving questions
    problem_solving = round(0.8 * 50)  # 80% of 50 questions

    # Calculate the number of multiple-choice questions
    multiple_choice = 50 - problem_solving

    result = multiple_choice
    return result

print(solution())