def solution():
    # Nicole answered 3 fewer questions correctly than Kim
    # Kim answered 8 more questions correctly than Cherry
    # If Nicole answered 22 correctly, we can calculate how many Kim answered
    kim_correct = 22 + 3  # Kim answered 3 more questions correctly than Nicole
    cherry_correct = kim_correct - 8  # Cherry answered 8 fewer questions correctly than Kim
    result = cherry_correct
    return result

print(solution())