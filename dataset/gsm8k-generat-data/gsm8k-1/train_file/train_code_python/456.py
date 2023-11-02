def solution():
    """Fiona completed 36 math questions in an hour. Shirley was able to complete twice as many math questions within that same time, and Kiana completed half of the sum of Fiona and Shirley's math questions. If they each did the same number of questions the following hour, how many math questions did all three girls complete in 2 hours?"""
    fiona_questions = 36
    shirley_questions = fiona_questions * 2
    kiana_questions = (fiona_questions + shirley_questions) / 2
    total_questions_first_hour = fiona_questions + shirley_questions + kiana_questions
    total_questions_second_hour = total_questions_first_hour * 3
    result = total_questions_second_hour
    return result

print(solution())