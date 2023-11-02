def solution():
    """If two piles of toys added together make 120 toys in total, and the larger of the two piles is twice as big as the smaller one, how many toys are in the larger pile?"""
    # Define the total number of toys
    total_toys = 120

    # Define the size of the smaller pile
    smaller_pile = x

    # Define the size of the larger pile
    larger_pile = 2 * smaller_pile

    # Calculate the total of the two piles
    total_piles = smaller_pile + larger_pile

    # Determine the size of the smaller pile by solving for x in the equation total_piles = 120
    smaller_pile = (total_toys / 3)

    # Calculate the size of the larger pile
    larger_pile = 2 * smaller_pile

    result = larger_pile
    return result

print(solution())