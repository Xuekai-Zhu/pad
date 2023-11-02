def solution():
    total_time = 2*60  # 2 hours in minutes
    time_per_question = 2  # 2 minutes per question
    num_answered_questions = total_time // time_per_question
    num_unanswered_questions = 100 - num_answered_questions
    result = num_unanswered_questions
    return result

print(solution())