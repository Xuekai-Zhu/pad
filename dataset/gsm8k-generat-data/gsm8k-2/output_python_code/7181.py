def solution():
    """If you double a number and add 5 to the result, then that's 20 more than half of the original number. What's the original number?"""

    # Let's use x to represent the original number
    # The problem states that: 2x + 5 = (1/2)x + 20

    x = (20 - 5) / (2 - 1/2)
    result = x

    return result

print(solution())