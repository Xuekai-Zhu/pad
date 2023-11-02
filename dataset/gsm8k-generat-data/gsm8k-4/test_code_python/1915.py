def solution():
    """Building one birdhouse requires 7 planks and 20 nails. If 1 nail costs $0.05, and one plank costs $3, what is the cost, in dollars, to build 4 birdhouses?"""
    # Define the number of planks and nails needed to build one birdhouse
    PLANKS_PER_BIRDHOUSE = 7
    NAILS_PER_BIRDHOUSE = 20
    NAIL_PRICE = 0.05
    PLANK_PRICE = 3

    # Calculate the total cost of materials for one birdhouse
    material_cost_per_birdhouse = PLANKS_PER_BIRDHOUSE * PLANK_PRICE + NAILS_PER_BIRDHOUSE * NAIL_PRICE

    # Calculate the total cost of materials for 4 birdhouses
    material_cost_4_birdhouses = 4 * material_cost_per_birdhouse

    result = material_cost_4_birdhouses
    return result

print(solution())