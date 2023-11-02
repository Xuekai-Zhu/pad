def solution():
    """Jennifer bought 12 oranges from the market, she gave her three daughters 2 oranges each, and her only boy got 3 oranges. How many oranges did she remain with?"""
    total_oranges = 12
    given_oranges = 3 * 2 + 3
    remaining_oranges = total_oranges - given_oranges
    result = remaining_oranges
    return result

print(solution())