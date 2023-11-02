def solution():
    """Bart fills out surveys to earn money. He receives $0.2 for every question he answers in the survey. Each survey has 10 questions. On Monday he finished 3 surveys, and on Tuesday 4 surveys. How much money did he earn during these two days?"""
    questions_per_survey = 10
    earnings_per_question = 0.2
    monday_surveys = 3
    tuesday_surveys = 4
    total_questions_answered = questions_per_survey * (monday_surveys + tuesday_surveys)
    total_earnings = total_questions_answered * earnings_per_question
    result = total_earnings
    return result

print(solution())