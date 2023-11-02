def solution():
    math_questions = 40
    math_correct = math_questions * 0.75
    english_questions = 50
    english_correct = english_questions * 0.98
    total_correct = math_correct + english_correct
    result = total_correct
    return result

print(solution())