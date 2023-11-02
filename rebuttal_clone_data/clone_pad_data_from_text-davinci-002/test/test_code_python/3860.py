def solution():
    total_questions = 50
    percent_problem_solving = 80
    question_type_multiple_choice = 100 - percent_problem_solving
    number_of_multiple_choice = total_questions * (question_type_multiple_choice / 100)
    result = number_of_multiple_choice
    
    return result

print(solution())