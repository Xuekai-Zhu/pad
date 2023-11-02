def solution():
    """Henrietta is repainting her house. The walls in the living room take up 600 square feet. She has three bedrooms. The walls in each bedroom take up 400 square feet. If one gallon of paint can cover 600 square feet, how many gallons of paint does Henrietta need to paint her house?"""
    # Define the area of each room
    living_room_area = 600
    bedroom_area = 400

    # Calculate the total area to be painted
    total_area = living_room_area + (3 * bedroom_area)

    # Calculate the number of gallons of paint needed
    gallons_needed = total_area / 600

    # Display the number of gallons of paint needed
    result = gallons_needed
    return result

print(solution())