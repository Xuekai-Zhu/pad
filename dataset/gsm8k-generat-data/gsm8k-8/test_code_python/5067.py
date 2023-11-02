def solution():
    # Calculate the volume of one slab of concrete in cubic feet
    volume_per_slab = 100 * 100 * 0.5

    # Calculate the total volume of concrete needed for 3 slabs
    total_volume = volume_per_slab * 3

    # Calculate the total weight of the concrete in pounds
    total_weight = total_volume * 150

    # Calculate the total cost of the concrete in dollars
    total_cost = total_weight * 0.02

    result = total_cost
    return result

print(solution())