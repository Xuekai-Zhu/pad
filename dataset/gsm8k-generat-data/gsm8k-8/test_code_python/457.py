def solution():
    # Fiona completed 36 math questions
    fiona_questions = 36

    # Shirley completed twice as many math questions as Fiona
    shirley_questions = fiona_questions * 2

    # Kiana completed half of the sum of Fiona and Shirley's math questions
    kiana_questions = (fiona_questions + shirley_questions) / 2

    # Total number of questions completed in one hour
    total_questions = fiona_questions + shirley_questions + kiana_questions

    # Total number of questions completed in two hours
    total_questions_2_hours = total_questions * 2

    result = total_questions_2_hours
    return result

print(solution())