def solution():
    # Calculate the number of questions Kim answered correctly
    kim_correct = 22 + 3  # Nicole answered 3 fewer questions correctly than Kim
    # Calculate the number of questions Cherry answered correctly
    cherry_correct = kim_correct - 8  # Kim answered 8 more questions correctly than Cherry
    result = cherry_correct
    return result

print(solution())