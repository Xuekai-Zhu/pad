def solution():
    test1 = 0.95
    test2 = 0.80
    target_average = 0.90

    # We want to find the grade Kat needs to get on the third test
    # to bring her average up to the target average.
    # We can solve for x in the equation:
    # (test1 + test2 + x) / 3 = target_average
    # by multiplying both sides by 3 and solving for x.
    # Simplifying the equation gives us:
    # test1 + test2 + x = 3 * target_average
    # x = 3 * target_average - test1 - test2
    grade_needed = 3 * target_average - test1 - test2
    result = grade_needed
    return result

print(solution())