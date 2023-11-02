def solution():
    """Anna has 3 times as many toys as Mandy and 2 fewer toys than Amanda. If they have 142 toys all together, how many toys does Mandy have?"""
    # Assign variables for the number of toys each person has
    mandy_toys = None
    anna_toys = None
    amanda_toys = None

    # Use algebra to solve for mandy's toys
    # Let x be the number of toys Mandy has
    # Anna has 3 times as many toys as Mandy, so she has 3x toys
    # Amanda has 2 more toys than Anna, so she has 3x + 2 toys
    # The total number of toys is 142, so:
    # x + 3x + (3x + 2) = 142
    # Simplifying the equation, we get:
    # 7x + 2 = 142
    # 7x = 140
    # x = 20

    mandy_toys = 20
    anna_toys = 3 * mandy_toys
    amanda_toys = anna_toys + 2

    result = mandy_toys
    return result

print(solution())