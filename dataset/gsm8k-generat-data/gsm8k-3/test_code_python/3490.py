def solution():
    """Grayson has 100 questions on a test. He answers some of the questions for 2 hours, taking two minutes for each answer, then realizes he doesn't know the rest of the questions. How many questions does Grayson leave unanswered when he submits his test?"""
    # Define the total number of questions
    TOTAL_QUESTIONS = 100

    # Define the time Grayson has spent answering questions
    ANSWER_TIME = 2 * 60 # 2 hours

    # Define the time it takes to answer one question
    TIME_PER_QUESTION = 2 # 2 minutes

    # Calculate the number of questions Grayson answered
    answered_questions = ANSWER_TIME // TIME_PER_QUESTION

    # Calculate the number of unanswered questions
    unanswered_questions = TOTAL_QUESTIONS - answered_questions

    # Display the number of unanswered questions
    result = unanswered_questions
    return result

print(solution())