def solution():
    # Convert milliliters to liters for the two smaller bottles
    bottle2 = 750 / 1000
    bottle3 = 250 / 1000

    # Add up the volumes of all three bottles
    total_volume = 2 + bottle2 + bottle3
    result = total_volume
    return result

print(solution())