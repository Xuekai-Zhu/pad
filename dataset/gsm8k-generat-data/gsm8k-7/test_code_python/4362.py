def solution():
    math_questions = 40
    math_percent_correct = 0.75

    english_questions = 50
    english_percent_correct = 0.98

    # Calculate the number of math questions he gets right
    math_correct = math_questions * math_percent_correct

    # Calculate the number of English questions he gets right
    english_correct = english_questions * english_percent_correct

    # Calculate the total number of questions he gets right
    total_correct = math_correct + english_correct
    result = total_correct
    return result

print(solution())