def solution():
    """Bart fills out surveys to earn money. He receives $0.2 for every question he answers in the survey. Each survey has 10 questions. On Monday he finished 3 surveys, and on Tuesday 4 surveys. How much money did he earn during these two days?"""
    # Define the payment per question
    PAYMENT_PER_QUESTION = 0.2

    # Define the number of surveys completed on each day
    monday_surveys = 3
    tuesday_surveys = 4

    # Calculate the number of questions answered on each day
    monday_questions = monday_surveys * 10
    tuesday_questions = tuesday_surveys * 10

    # Calculate Bart's earnings for each day
    monday_earnings = monday_questions * PAYMENT_PER_QUESTION
    tuesday_earnings = tuesday_questions * PAYMENT_PER_QUESTION

    # Calculate Bart's total earnings for both days
    total_earnings = monday_earnings + tuesday_earnings

    # Display Bart's total earnings
    result = total_earnings
    return result

print(solution())