def solution():
    """Lisa has 18 more dresses than Ana. If the number of their dresses combined is 48, how many dresses does Ana have?"""
    # Let x be the number of dresses Ana has
    # Then Lisa has x + 18 dresses
    # The total number of dresses is x + x + 18 = 2x + 18

    # Set up the equation 2x + 18 = 48
    # Solve for x
    x = (48 - 18) / 2

    # Return the result
    result = x
    return result

print(solution())