def solution():
    """If John scored 100 on his first 3 tests and an 80 on his 4th, what was his average score across the 4 tests?"""
    test1 = 100
    test2 = 100
    test3 = 100
    test4 = 80
    total_score = test1 + test2 + test3 + test4
    num_tests = 4
    average_score = total_score / num_tests
    result = average_score
    return result

print(solution())