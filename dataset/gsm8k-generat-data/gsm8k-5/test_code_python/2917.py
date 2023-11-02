def solution():
    total_toys = 120  # The total number of toys in both piles combined
    larger_pile_ratio = 2  # The ratio of the larger pile to the smaller pile

    # Set up a system of equations to solve for the number of toys in each pile
    # Let x be the number of toys in the smaller pile
    # Then 2x is the number of toys in the larger pile
    # And x + 2x = 120, since the total number of toys is 120
    # Solving for x, we get x = 40
    smaller_pile = 40
    larger_pile = 2 * smaller_pile
    result = larger_pile
    return result

print(solution())