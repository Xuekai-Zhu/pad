def solution():
    """Carl is taking a class where the whole grade is based on four tests that are graded out of 100. He got an 80, a 75 and a 90 on his first three tests. If he wants an 85 average for the class, what is the minimum grade he needs to get on his last test?"""
    desired_average = 85
    current_average = (80 + 75 + 90) / 3
    fourth_test_needed = (desired_average * 4) - (80 + 75 + 90)
    result = fourth_test_needed
    return result

print(solution())