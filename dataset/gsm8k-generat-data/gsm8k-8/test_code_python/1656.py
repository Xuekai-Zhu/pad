def solution():
    # Convert fence length from yards to feet
    fence_length_feet = 25 * 3

    # Calculate number of trees needed
    trees_needed = fence_length_feet / 1.5

    # Round up to nearest whole number of trees
    trees_needed = math.ceil(trees_needed)

    # Calculate total cost of trees
    total_cost = trees_needed * 8.0

    result = total_cost
    return result

print(solution())