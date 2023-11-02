def solution():
    # Calculate the total weight of the sugar cubes
    sugar_cubes_weight = 2 * 1

    # Calculate the total weight of the carrots
    carrots_weight = 4 * 12 * 75

    # Calculate the total weight of the horses
    total_weight = sugar_cubes_weight + carrots_weight

    # Calculate the weight of the oats
    oats_weight = total_weight - 2 * 75

    result = oats_weight
    return result

print(solution())