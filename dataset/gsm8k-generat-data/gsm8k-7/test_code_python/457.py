def solution():
    fiona_questions = 36
    shirley_questions = 2 * fiona_questions
    kiana_questions = 0.5 * (fiona_questions + shirley_questions)

    # Calculate the total number of questions they completed in the first hour
    total_questions_hour1 = fiona_questions + shirley_questions + kiana_questions

    # Calculate the total number of questions they each completed in the second hour
    each_questions_hour2 = total_questions_hour1 / 3

    # Calculate the total number of questions they completed in the second hour
    total_questions_hour2 = each_questions_hour2 * 3

    # Calculate the total number of questions they completed in 2 hours
    total_questions = total_questions_hour1 + total_questions_hour2
    result = total_questions
    return result

print(solution())