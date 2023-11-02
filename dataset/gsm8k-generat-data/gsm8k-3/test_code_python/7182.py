def solution():
    """If you double a number and add 5 to the result, then that's 20 more than half of the original number. What's the original number?"""
    # Let's assume the original number is x
    # According to the problem, we have the equation: 2x + 5 = (1/2)x + 20

    # Solving for x
    x = (20 - 5) / (1/2 - 2)
    result = x
    return result

print(solution())