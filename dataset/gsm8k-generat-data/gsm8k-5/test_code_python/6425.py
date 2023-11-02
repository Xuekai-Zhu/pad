def solution():
    payment_per_question = 0.2  # Bart earns $0.2 for each question he answers
    questions_per_survey = 10  # Each survey has 10 questions

    # Bart completed 3 surveys on Monday
    monday_surveys = 3
    monday_questions = monday_surveys * questions_per_survey
    monday_payment = monday_questions * payment_per_question

    # Bart completed 4 surveys on Tuesday
    tuesday_surveys = 4
    tuesday_questions = tuesday_surveys * questions_per_survey
    tuesday_payment = tuesday_questions * payment_per_question

    # Calculate the total payment Bart earned over the two days
    total_payment = monday_payment + tuesday_payment
    result = total_payment
    return result

print(solution())