def solution():
    num_homes = 3
    length = 100
    width = 100
    height = 0.5
    density = 150
    cost_per_pound = 0.02

    # Calculate the volume of one slab of concrete
    volume = length * width * height

    # Calculate the total volume of concrete needed for all homes
    total_volume = num_homes * volume

    # Calculate the total weight of the concrete needed
    total_weight = total_volume * density

    # Calculate the total cost of the foundation
    total_cost = total_weight * cost_per_pound
    result = total_cost
    return result

print(solution())