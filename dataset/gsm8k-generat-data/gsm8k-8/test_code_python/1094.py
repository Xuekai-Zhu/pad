def solution():
    # Calculate the amount of water left after evaporation
    water_left = 16 - 4

    # Calculate the total amount of liquid in the jug after quadrupling the water
    total_liquid = 2 + (4 * water_left)

    # Calculate the percentage of the liquid that is koolaid powder
    koolaid_percentage = (2 / total_liquid) * 100

    result = koolaid_percentage
    return result

print(solution())