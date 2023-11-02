def solution():
    math_questions = 40
    math_right = math_questions * 0.75
    english_questions = 50
    english_right = english_questions * 0.98
    total_right = math_right + english_right
    result = total_right
    return result

print(solution())