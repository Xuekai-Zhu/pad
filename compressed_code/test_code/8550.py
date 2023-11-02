def solution():
    
    total_time = 2 * 60  
    time_per_question = 2  
    answered_questions = total_time // time_per_question
    unanswered_questions = 100 - answered_questions
    result = unanswered_questions
    return result

print(solution())