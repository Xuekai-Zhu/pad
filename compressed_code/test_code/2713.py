def solution():
    
    time_spent = 2 * 60  
    time_per_question = 2
    answered_questions = time_spent // time_per_question
    unanswered_questions = 100 - answered_questions
    result = unanswered_questions
    return result

print(solution())