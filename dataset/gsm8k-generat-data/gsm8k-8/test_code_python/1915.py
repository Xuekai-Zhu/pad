def solution():
    # Define the number of planks and nails required for one birdhouse
    planks_per_birdhouse = 7
    nails_per_birdhouse = 20

    # Define the cost of one plank and one nail
    plank_cost = 3
    nail_cost = 0.05

    # Calculate the total cost of materials for one birdhouse
    material_cost_per_birdhouse = planks_per_birdhouse * plank_cost + nails_per_birdhouse * nail_cost

    # Calculate the total cost of materials for 4 birdhouses
    total_cost = 4 * material_cost_per_birdhouse
    result = total_cost
    return result

print(solution())