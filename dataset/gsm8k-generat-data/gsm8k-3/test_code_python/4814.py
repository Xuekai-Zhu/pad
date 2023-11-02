def solution():
    """Mindy has 7 less than 9 times as many emails waiting for her as phone messages. If she has a total of 93 emails and phone messages combined, how many emails does she have?"""
    # Let x be the number of phone messages Mindy has
    # Then, according to the problem, she has 9x - 7 emails
    # And the total number of messages is x + (9x - 7) = 10x - 7
    # So we need to solve for x in the equation 10x - 7 = 93

    # Simplify the equation: 10x = 100
    # Solve for x: x = 10

    # Therefore, Mindy has 9x - 7 = 83 emails waiting for her
    result = 83
    return result

print(solution())