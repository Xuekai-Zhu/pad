def solution():
    total_liters = 0

    # Add the liters from the three 2-liter containers
    total_liters += 3 * 2

    # Add the liters from the two 0.75-liter containers
    total_liters += 2 * 0.75

    # Add the liters from the five 0.5-liter containers
    total_liters += 5 * 0.5

    result = total_liters
    return result

print(solution())