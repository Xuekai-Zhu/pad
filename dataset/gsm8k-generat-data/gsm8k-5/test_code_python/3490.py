def solution():
    total_questions = 100  # Grayson has 100 questions on the test
    time_spent_answering = 2 * 60  # Grayson spends 2 hours (120 minutes) answering questions
    time_per_question = 2  # Grayson takes 2 minutes to answer each question

    # Calculate the number of questions Grayson answered
    answered_questions = time_spent_answering / time_per_question

    # Calculate the number of unanswered questions
    unanswered_questions = total_questions - answered_questions
    result = unanswered_questions
    return result

print(solution())