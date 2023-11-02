def solution():
    english_questions = 30
    math_questions = 15
    english_time = 60
    math_time = 90
    time_per_english_question = english_time / english_questions
    time_per_math_question = math_time / math_questions
    time_difference = time_per_math_question - time_per_english_question
    result = time_difference * math_questions
    return result

print(solution())