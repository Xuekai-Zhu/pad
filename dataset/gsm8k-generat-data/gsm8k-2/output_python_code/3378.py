def solution():
    """On a quiz, Nicole answered 3 fewer questions correctly than Kim, and Kim answered 8 more questions correctly than Cherry. If Nicole answered 22 correctly, how many did Cherry answer correctly?"""
    nicole_correct = 22
    kim_correct = nicole_correct + 3
    cherry_correct = kim_correct - 8
    result = cherry_correct
    return result

print(solution())