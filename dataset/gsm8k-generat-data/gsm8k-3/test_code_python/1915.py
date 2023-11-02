def solution():
    """Building one birdhouse requires 7 planks and 20 nails.  If 1 nail costs $0.05, and one plank costs $3, what is the cost, in dollars, to build 4 birdhouses?"""
    # Define the number of planks and nails required for one birdhouse
    PLANKS_PER_BIRDHOUSE = 7
    NAILS_PER_BIRDHOUSE = 20
    NAIL_COST = 0.05
    PLANK_COST = 3

    # Calculate the cost of one birdhouse
    cost_per_birdhouse = (PLANKS_PER_BIRDHOUSE * PLANK_COST) + (NAILS_PER_BIRDHOUSE * NAIL_COST)

    # Calculate the cost of 4 birdhouses
    cost_for_4_birdhouses = cost_per_birdhouse * 4

    # Display the cost of building 4 birdhouses
    result = cost_for_4_birdhouses
    return result

print(solution())