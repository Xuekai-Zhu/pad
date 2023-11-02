def solution():
    first_hour_rate = 13
    second_hour_rate = first_hour_rate * 2
    third_hour_rate = second_hour_rate * 2

    # Calculate the total number of questions created in each hour
    first_hour_questions = first_hour_rate
    second_hour_questions = second_hour_rate
    third_hour_questions = third_hour_rate

    # Calculate the total number of questions created in the three hours
    total_questions = first_hour_questions + second_hour_questions + third_hour_questions
    result = total_questions
    return result

print(solution())