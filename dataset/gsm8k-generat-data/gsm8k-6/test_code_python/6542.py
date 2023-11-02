def solution():
    # Calculate the number of other rooms in the house
    num_bedrooms = 3
    num_other_rooms = 2*num_bedrooms

    # Calculate the total number of rooms in the house
    total_rooms = num_bedrooms + num_other_rooms

    # Calculate the total amount of paint needed for the bedrooms
    bedroom_paint = 2*num_bedrooms  # Each bedroom takes 2 gallons of paint

    # Calculate the total amount of paint needed for the other rooms
    other_room_paint = 2*num_other_rooms  # Each other room takes 2 gallons of paint

    # Calculate the total amount of white paint needed
    white_paint = 3*(total_rooms - num_bedrooms)  # Each white room takes 3 gallons of paint

    # Calculate the total number of paint cans needed
    total_paint = bedroom_paint + other_room_paint + white_paint
    total_cans = total_paint//1 + (total_paint%1 > 0)  # Round up to the nearest can

    result = total_cans
    return result

print(solution())