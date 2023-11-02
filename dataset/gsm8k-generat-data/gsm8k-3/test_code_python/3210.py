def solution():
    """Anna has a certain number of phone chargers and five times more laptop chargers than phone chargers. If she has 24 chargers total, how many phone chargers does she have?"""
    # Let x be the number of phone chargers Anna has
    x = 0

    # The number of laptop chargers Anna has is 5 times more than the number of phone chargers
    y = 5 * x

    # The total number of chargers Anna has is 24
    total = x + y

    # Solve for x
    x = (24 - y) / 6

    # Display the number of phone chargers Anna has
    result = x
    return result

print(solution())