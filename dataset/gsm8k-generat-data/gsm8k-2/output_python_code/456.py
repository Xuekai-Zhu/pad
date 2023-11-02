def solution():
    """Fiona completed 36 math questions in an hour. Shirley was able to complete twice as many math questions within that same time, and Kiana completed half of the sum of Fiona and Shirley's math questions. If they each did the same number of questions the following hour, how many math questions did all three girls complete in 2 hours?"""
    fiona_questions = 36
    shirley_questions = 2 * fiona_questions
    total_questions = fiona_questions + shirley_questions
    kiana_questions = total_questions / 2
    first_hour_questions = fiona_questions + shirley_questions + kiana_questions
    total_questions_2_hours = first_hour_questions * 2
    result = total_questions_2_hours
    return result

print(solution())