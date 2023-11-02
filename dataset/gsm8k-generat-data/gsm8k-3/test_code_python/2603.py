def solution():
    """Anna has 3 times as many toys as Mandy and 2 fewer toys than Amanda. If they have 142 toys all together, how many toys does Mandy have?"""
    # Let's assume that Mandy has x toys
    # Anna has 3 times as many toys as Mandy
    # Amanda has 2 more toys than Anna
    # Altogether, they have 142 toys

    # So, we have the following equations:
    # 3x = number of toys Anna has
    # (3x + 2) = number of toys Amanda has
    # x + 3x + (3x + 2) = 142

    # Simplifying the last equation:
    # 7x + 2 =142
    # 7x = 140
    # x = 20

    # Therefore, Mandy has 20 toys
    result = 20
    return result

print(solution())