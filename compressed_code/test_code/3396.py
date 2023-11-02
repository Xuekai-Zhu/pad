def solution():
    
    math_questions = 40
    math_percentage = 0.75
    english_questions = 50
    english_percentage = 0.98

    math_correct = math_questions * math_percentage
    english_correct = english_questions * english_percentage
    total_correct = math_correct + english_correct

    result = total_correct
    return result

print(solution())