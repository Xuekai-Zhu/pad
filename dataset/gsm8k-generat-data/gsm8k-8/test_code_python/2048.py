def solution():
    # Calculate the total number of questions asked by all members in an hour
    questions_per_member = 3
    total_questions_per_hour = questions_per_member * 200

    # Calculate the average number of answers posted by each member
    answers_per_question = 3
    average_answers_per_member = answers_per_question * questions_per_member

    # Calculate the total number of answers posted by all members in an hour
    total_answers_per_hour = average_answers_per_member * 200

    # Calculate the total number of questions and answers posted in a day
    hours_per_day = 24
    total_questions = total_questions_per_hour * hours_per_day
    total_answers = total_answers_per_hour * hours_per_day

    # Calculate the result
    result = total_questions + total_answers
    return result

print(solution())