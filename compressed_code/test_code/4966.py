def solution():
    
    questions_per_survey = 10
    earnings_per_question = 0.2
    monday_surveys = 3
    tuesday_surveys = 4
    total_questions_answered = questions_per_survey * (monday_surveys + tuesday_surveys)
    total_earnings = total_questions_answered * earnings_per_question
    result = total_earnings
    return result

print(solution())