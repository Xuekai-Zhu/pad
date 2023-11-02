def solution():
    # Define the number of questions and percentage correct for each test
    math_questions = 40
    math_correct_percentage = 0.75
    english_questions = 50
    english_correct_percentage = 0.98

    # Calculate the number of questions Phillip gets right for each test
    math_correct = math_questions * math_correct_percentage
    english_correct = english_questions * english_correct_percentage

    # Calculate the total number of questions Phillip gets right
    total_correct = math_correct + english_correct
    result = total_correct
    return result

print(solution())