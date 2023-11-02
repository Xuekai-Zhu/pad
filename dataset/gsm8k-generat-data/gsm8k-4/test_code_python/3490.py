def solution():
    """Grayson has 100 questions on a test. He answers some of the questions for 2 hours, taking two minutes for each answer, then realizes he doesn't know the rest of the questions. How many questions does Grayson leave unanswered when he submits his test?"""
    # Define the time Grayson spends on the test, in minutes
    total_time = 2 * 60

    # Define the time Grayson spends answering the questions he knows
    known_time = int(100 / 2)

    # Define the number of questions Grayson answers within the known time
    known_questions = known_time // 2

    # Calculate the number of questions Grayson leaves unanswered
    unanswered_questions = 100 - known_questions

    # Return the result
    result = unanswered_questions
    return result

print(solution())