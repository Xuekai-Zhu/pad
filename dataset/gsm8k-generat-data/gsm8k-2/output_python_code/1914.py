def solution():
    """Building one birdhouse requires 7 planks and 20 nails. If 1 nail costs $0.05, and one plank costs $3, what is the cost, in dollars, to build 4 birdhouses?"""
    planks_cost = 3
    nails_cost = 0.05
    birdhouses = 4
    planks_needed = 7 * birdhouses
    nails_needed = 20 * birdhouses
    total_cost = (planks_cost * planks_needed) + (nails_cost * nails_needed)
    result = total_cost
    return result

print(solution())