def solution():
    
    fiona_questions = 36
    shirley_questions = 2 * fiona_questions
    total_questions = fiona_questions + shirley_questions
    kiana_questions = total_questions / 2
    first_hour_questions = fiona_questions + shirley_questions + kiana_questions
    total_questions_2_hours = first_hour_questions * 2
    result = total_questions_2_hours
    return result

print(solution())