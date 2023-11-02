def solution():
    # Calculate the number of questions Shirley completed
    shirley_questions = 2 * 36  # Shirley completed twice as many questions as Fiona

    # Calculate the total number of questions completed by Fiona and Shirley
    total_questions_FS = 36 + shirley_questions  # Fiona and Shirley's math questions

    # Calculate the number of questions Kiana completed
    kiana_questions = 0.5 * total_questions_FS  # Kiana completed half of the total math questions

    # Calculate the total number of questions completed by all three girls in one hour
    total_questions = total_questions_FS + kiana_questions  # Total math questions completed by all three girls

    # Calculate the total number of questions completed by all three girls in two hours
    total_questions_2hours = 2 * total_questions

    result = total_questions_2hours
    return result

print(solution())