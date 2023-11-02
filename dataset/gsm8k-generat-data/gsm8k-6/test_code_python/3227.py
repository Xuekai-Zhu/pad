def solution():
    # Calculate the total area of the bedrooms
    total_bedroom_area = 4 * (11 * 11)

    # Calculate the total area of the bathrooms
    total_bathroom_area = 2 * (6 * 8)

    # Calculate the total area of the house without the kitchen and living area
    house_area = 1110 - total_bedroom_area - total_bathroom_area

    # Calculate the area of the kitchen and living area
    kitchen_area = house_area / 2

    result = kitchen_area
    return result

print(solution())