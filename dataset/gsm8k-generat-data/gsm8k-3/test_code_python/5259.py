def solution():
    """I caught 4 fewer fish than the number in my tank and added them to my fish tank. If the tank has 20 fish right now, how many did I add?"""
    # Let x be the number of fish in the tank before adding more
    # The number of fish caught and added is x - 4
    # The total number of fish in the tank after adding more is x - 4 + the number added = x - 4 + y, where y is the number added
    # We know that x - 4 + y = 20
    # Solving for y, we get y = 24 - x

    # We don't know the value of x, but we can guess and check
    for x in range(1, 20):
        # Check if y = 24 - x is a valid number of fish added
        if 24 - x >= 0 and x - 4 + 24 - x == 20:
            result = 24 - x
            return result

    # If we haven't found a valid solution, return None
    return None

print(solution())