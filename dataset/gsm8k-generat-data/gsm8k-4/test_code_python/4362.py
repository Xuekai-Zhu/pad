def solution():
    """Phillip is taking a math test and an English test on Monday. The math test has 40 questions and he gets 75% of them right. The English test has 50 questions and he gets 98% of them right. How many total questions does he get right?"""
    # Define the number of questions on the math and English tests
    math_questions = 40
    english_questions = 50

    # Calculate the number of questions Phillip gets right on each test
    math_correct = math_questions * 0.75
    english_correct = english_questions * 0.98

    # Calculate the total number of questions Phillip gets right
    total_correct = math_correct + english_correct

    # return the result
    result = total_correct
    return result

print(solution())