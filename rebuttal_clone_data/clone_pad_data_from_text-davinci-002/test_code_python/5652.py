def solution():
    total_questions_project1 = 518
    total_questions_project2 = 476
    total_questions = total_questions_project1 + total_questions_project2
    days_available = 7
    questions_per_day = total_questions / days_available
    result = questions_per_day
    
    return result

print(solution())