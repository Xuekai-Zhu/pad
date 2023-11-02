def solution():
    living_room_area = 600  # Walls in the living room take up 600 square feet
    bedroom_area = 400  # Walls in each bedroom take up 400 square feet
    num_bedrooms = 3  # Henrietta has three bedrooms

    # Calculate total area to be painted
    total_area = living_room_area + (num_bedrooms * bedroom_area)

    # Calculate the number of gallons of paint needed
    gallons_needed = total_area / 600  # One gallon of paint can cover 600 square feet
    result = gallons_needed
    return result

print(solution())