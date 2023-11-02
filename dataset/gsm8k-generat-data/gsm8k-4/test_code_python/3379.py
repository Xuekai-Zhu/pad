def solution():
    """On a quiz, Nicole answered 3 fewer questions correctly than Kim, and Kim answered 8 more questions correctly than Cherry. If Nicole answered 22 correctly, how many did Cherry answer correctly?"""
    # Define Nicole's correct answers
    nicole_correct = 22

    # Calculate Kim's correct answers
    kim_correct = nicole_correct + 3

    # Calculate Cherry's correct answers
    cherry_correct = kim_correct - 8

    # return Cherry's correct answers
    result = cherry_correct
    return result

print(solution())