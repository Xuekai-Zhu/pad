def solution():
    """Sasha can complete 15 questions an hour. If she has 60 questions to complete and she works for 2 hours, how many questions does she still need to complete?"""
    questions_per_hour = 15
    total_questions = 60
    hours_worked = 2
    questions_completed = questions_per_hour * hours_worked
    questions_remaining = total_questions - questions_completed
    result = questions_remaining
    return result

print(solution())