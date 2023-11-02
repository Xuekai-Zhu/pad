def solution():
    # Calculate the total area of the walls
    living_room = 600
    bedrooms = 3 * 400
    total_area = living_room + bedrooms

    # Calculate the number of gallons of paint needed
    gallons_needed = total_area / 600

    result = gallons_needed
    return result

print(solution())