def solution():
     total_questions = 80
     questions_answered = 16
     minutes_used = 12
     minutes_left = 60 - minutes_used
     time_per_question = minutes_left / (total_questions - questions_answered)
     minutes_remaining = time_per_question * (total_questions - questions_answered)
     result = minutes_remaining
     return result

print(solution())