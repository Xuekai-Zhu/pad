def solution():
    soap_per_cup_of_water = 3
    ounces_per_cup = 8
    max_capacity_ounces = 40

    # Calculate the number of cups of water that will fit in the container
    max_capacity_cups = max_capacity_ounces / ounces_per_cup

    # Calculate the number of tablespoons of soap needed for that amount of water
    soap_needed = max_capacity_cups * soap_per_cup_of_water

    result = soap_needed
    return result

print(solution())