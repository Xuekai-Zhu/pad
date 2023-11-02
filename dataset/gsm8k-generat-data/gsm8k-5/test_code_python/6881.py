def solution():
    total_questions = 50  # There are 50 questions in the exam
    problem_solving_questions = int(total_questions * 0.8)  # 80% of the questions are problem-solving
    multiple_choice_questions = total_questions - problem_solving_questions  # The rest of the questions are multiple-choice
    result = multiple_choice_questions
    return result

print(solution())