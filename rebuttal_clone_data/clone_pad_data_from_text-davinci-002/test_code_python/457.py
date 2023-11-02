def solution():
    fiona_questions = 36
    shirley_questions = fiona_questions * 2
    kiana_questions = (fiona_questions + shirley_questions) / 2
    total_questions = fiona_questions + shirley_questions + kiana_questions
    result = total_questions
    return result

print(solution())