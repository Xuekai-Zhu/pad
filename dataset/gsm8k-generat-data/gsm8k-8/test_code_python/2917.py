def solution():
    # Define the total number of toys
    total_toys = 120

    # Define the ratio of the sizes of the two piles
    larger_to_smaller_ratio = 2

    # Set up an equation system to solve for the two pile sizes
    # Let x be the size of the smaller pile
    # Then the size of the larger pile is 2x
    # And the sum of the two piles is 120
    # So we have x + 2x = 120, which simplifies to 3x = 120
    # And solving for x gives x = 40
    smaller_pile_size = 40
    larger_pile_size = larger_to_smaller_ratio * smaller_pile_size

    result = larger_pile_size
    return result

print(solution())