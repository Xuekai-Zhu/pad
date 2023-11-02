def solution():
    """Phillip is taking a math test and an English test on Monday. The math test has 40 questions and he gets 75% of them right. The English test has 50 questions and he gets 98% of them right. How many total questions does he get right?"""
    # Define the number of questions on the math test and Phillip's success rate
    MATH_QUESTIONS = 40
    MATH_SUCCESS_RATE = 0.75

    # Define the number of questions on the English test and Phillip's success rate
    ENGLISH_QUESTIONS = 50
    ENGLISH_SUCCESS_RATE = 0.98

    # Calculate the number of questions Phillip gets right on each test
    math_right = MATH_QUESTIONS * MATH_SUCCESS_RATE
    english_right = ENGLISH_QUESTIONS * ENGLISH_SUCCESS_RATE

    # Calculate the total number of questions Phillip gets right
    total_right = math_right + english_right

    # Display the total number of questions Phillip gets right
    result = total_right
    return result

print(solution())