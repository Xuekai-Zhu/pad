def solution():
    """If two piles of toys added together make 120 toys in total, and the larger of the two piles is twice as big as the smaller one, how many toys are in the larger pile?"""
    # Let x be the size of the smaller pile
    # Then the larger pile is 2x
    # The total number of toys is x + 2x = 3x
    # So 3x = 120, and x = 40
    # Therefore, the larger pile is 2x = 80

    # Return the size of the larger pile
    result = 80
    return result

print(solution())