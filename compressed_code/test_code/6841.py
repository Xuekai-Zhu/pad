def solution():
    
    questions_per_hour = 15
    hours_worked = 2
    total_questions = 60
    questions_completed = questions_per_hour * hours_worked
    questions_remaining = total_questions - questions_completed
    result = questions_remaining
    return result

print(solution())