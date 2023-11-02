def solution():
    # Calculate the total amount of time Grayson spent on the test in minutes
    time_spent = 2 * 60  # 2 hours multiplied by 60 minutes

    # Calculate the number of questions Grayson answered
    questions_answered = time_spent / 2  # Grayson takes 2 minutes per question

    # Calculate the number of questions Grayson left unanswered
    questions_unanswered = 100 - questions_answered

    result = questions_unanswered
    return result

print(solution())