def solution():
    
    total_questions = 50
    problem_solving_questions = int(total_questions * 0.8)
    multiple_choice_questions = total_questions - problem_solving_questions
    result = multiple_choice_questions
    return result

print(solution())