def solution():
    pay_per_question = 0.2
    num_questions_per_survey = 10

    num_surveys_monday = 3
    num_surveys_tuesday = 4

    # Calculate the total number of questions answered
    total_questions = (num_surveys_monday + num_surveys_tuesday) * num_questions_per_survey

    # Calculate the total earnings
    total_earnings = total_questions * pay_per_question
    
    result = total_earnings
    return result

print(solution())