def solution():
    """If I give my brother 2 marbles I will have double his number of marbles, but my friend will have triple the number I do. The total number of marbles we have together is 63. How many marbles do I have?"""
    # Let x be my number of marbles
    # Then my brother has x-2 marbles
    # And my friend has 3*(2x-2) = 6x-6 marbles
    # The total number of marbles is x + (x-2) + (6x-6) = 8x - 8
    # So we have 8x - 8 = 63
    # Solving for x, we get:
    x = (63 + 8) / 8
    result = x
    return result

print(solution())