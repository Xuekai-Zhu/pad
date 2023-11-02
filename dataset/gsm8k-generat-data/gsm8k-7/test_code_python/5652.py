def solution():
    num_questions_project_1 = 518
    num_questions_project_2 = 476
    num_days = 7  # one week

    # Calculate the total number of questions he needs to complete
    total_questions = num_questions_project_1 + num_questions_project_2

    # Calculate the number of questions he needs to complete each day
    questions_per_day = total_questions / num_days
    result = questions_per_day
    return result

print(solution())