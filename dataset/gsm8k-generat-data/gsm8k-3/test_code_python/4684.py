def solution():
    """In the second hour of a storm it rains 7 inches more than twice the amount it rained the first hour. The total amount of rain in the first two hours is 22 inches. How much did it rain in the first hour?"""
    # Let x be the amount it rained in the first hour
    # The amount it rained in the second hour is 2x + 7
    # The total amount of rain in the first two hours is x + (2x + 7) = 3x + 7
    # We know that 3x + 7 = 22, so we can solve for x
    x = (22 - 7) / 3
    result = x
    return result

print(solution())