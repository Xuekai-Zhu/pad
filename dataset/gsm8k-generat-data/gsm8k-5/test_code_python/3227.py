def solution():
    total_area = 1110  # Raj's house has a total area of 1,110 square feet
    bedroom_area = 4 * (11 * 11)  # There are 4 bedrooms, each measuring 11 x 11 feet
    bathroom_area = 2 * (6 * 8)  # There are 2 bathrooms, each measuring 6 x 8 feet
    occupied_area = bedroom_area + bathroom_area  # Calculate the total area occupied by bedrooms and bathrooms
    remaining_area = total_area - occupied_area  # Calculate the remaining area for the kitchen and living area
    kitchen_area = remaining_area / 2  # The kitchen and living area have the same sized area
    result = kitchen_area
    return result

print(solution())