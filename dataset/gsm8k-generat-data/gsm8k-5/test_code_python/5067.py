def solution():
    slab_volume = 100 * 100 * 0.5  # volume of one slab of concrete in cubic feet

    # Total amount of concrete needed for 3 homes
    total_concrete = slab_volume * 3

    # Total weight of the concrete in pounds
    total_weight = total_concrete * 150

    # Total cost of the concrete
    total_cost = total_weight * 0.02

    result = total_cost
    return result

print(solution())