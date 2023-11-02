def solution():
    """Ann is cutting fabric to make curtains. She cuts a 4 foot by 6 foot rectangle for the living room, and a 2 foot by 4 foot rectangle for the bedroom. If the bolt of fabric is 16 feet by 12 feet, how much fabric is left in square feet?"""
    # Define the dimensions of the living room curtains and bedroom curtains
    living_room = 4 * 6
    bedroom = 2 * 4

    # Calculate the total area of fabric needed for the curtains
    total_area = living_room + bedroom

    # Define the dimensions of the bolt of fabric
    fabric_width = 16
    fabric_height = 12

    # Calculate the total area of the bolt of fabric
    fabric_area = fabric_width * fabric_height

    # Calculate the area of fabric left
    fabric_left = fabric_area - total_area

    # return the result
    result = fabric_left
    return result

print(solution())