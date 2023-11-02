def solution():
    # Define the time Grayson spends on answering questions
    time_spent_answering = 2 * 60

    # Calculate the number of questions Grayson can answer in the given time
    questions_answered = time_spent_answering // 2

    # Calculate the number of unanswered questions
    unanswered_questions = 100 - questions_answered

    result = unanswered_questions
    return result

print(solution())