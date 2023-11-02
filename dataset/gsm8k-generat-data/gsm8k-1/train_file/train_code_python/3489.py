def solution():
    """Grayson has 100 questions on a test. He answers some of the questions for 2 hours, taking two minutes for each answer, then realizes he doesn't know the rest of the questions. How many questions does Grayson leave unanswered when he submits his test?"""
    total_time = 2 * 60  # convert hours to minutes
    time_per_question = 2  # in minutes
    answered_questions = total_time // time_per_question
    unanswered_questions = 100 - answered_questions
    result = unanswered_questions
    return result

print(solution())