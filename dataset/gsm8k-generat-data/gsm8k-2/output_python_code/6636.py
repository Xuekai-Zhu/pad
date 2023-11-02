def solution():
    """If eight liters is 20% the capacity of a container filled with water, calculate the total capacity of 40 such containers filled with water."""
    eight_liters_percent = 20
    eight_liters = 8
    total_percent = 100
    total_containers = 40
    # calculate capacity per container
    capacity_percent = total_percent - eight_liters_percent
    capacity_per_container = (eight_liters * 100) / capacity_percent
    # calculate total capacity
    total_capacity = capacity_per_container * total_containers
    result = total_capacity
    return result

print(solution())