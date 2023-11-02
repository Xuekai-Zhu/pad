def solution():
    total_questions = 80
    answered_questions = 16
    time_left = 48  # 60 minutes - 12 minutes already used

    # Calculate the average time per question
    avg_time_per_question = time_left / answered_questions

    # Calculate the remaining time for Jessica to finish the exam
    remaining_questions = total_questions - answered_questions
    remaining_time = remaining_questions * avg_time_per_question

    result = remaining_time
    return result

print(solution())