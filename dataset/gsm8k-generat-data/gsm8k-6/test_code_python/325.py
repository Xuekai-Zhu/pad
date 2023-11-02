def solution():
    # Calculate the number of questions created by Bob in the first hour
    questions_hour1 = 13

    # Calculate the number of questions created by Bob in the second hour
    questions_hour2 = 2 * questions_hour1

    # Calculate the number of questions created by Bob in the third hour
    questions_hour3 = 2 * questions_hour2

    # Calculate the total number of questions created by Bob in three hours
    total_questions = questions_hour1 + questions_hour2 + questions_hour3
    result = total_questions
    return result

print(solution())