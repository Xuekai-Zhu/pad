def solution():
    # Calculate the area of the bedrooms
    bedroom_area = 4 * (11 * 11)

    # Calculate the area of the bathrooms
    bathroom_area = 2 * (6 * 8)

    # Calculate the area of the kitchen and living area combined
    kitchen_living_area = 1110 - bedroom_area - bathroom_area

    # Divide the area of the kitchen and living area by 2 to get the area of just the kitchen
    kitchen_area = kitchen_living_area / 2

    result = kitchen_area
    return result

print(solution())