def solution():
     """Ann is cutting fabric to make curtains. She cuts a 4 foot by 6 foot rectangle for the living room, and a 2 foot by 4 foot rectangle for the bedroom. If the bolt of fabric is 16 feet by 12 feet, how much fabric is left in square feet?"""
    fabric_width = 16
    fabric_length = 12
    living_room_width = 4
    living_room_length = 6
    bedroom_width = 2
    bedroom_length = 4
    living_room_square_feet = living_room_width * living_room_length
    bedroom_square_feet = bedroom_width * bedroom_length
    total_square_feet = living_room_square_feet + bedroom_square_feet
    fabric_square_feet = fabric_width * fabric_length
    fabric_left_over = fabric_square_feet - total_square_feet
    result = fabric_left_over
    
    return result

print(solution())