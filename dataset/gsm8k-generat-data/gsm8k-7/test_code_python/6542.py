def solution():
    num_bedrooms = 3
    num_other_rooms = num_bedrooms * 2
    gallons_per_room = 2

    # Calculate the total number of gallons required for the bedrooms
    total_bedroom_gallons = num_bedrooms * gallons_per_room

    # Calculate the total number of gallons required for the other rooms
    total_other_room_gallons = num_other_rooms * gallons_per_room

    # Calculate the number of 1-gallon cans of colored paint needed for the bedrooms
    num_bedroom_cans = num_bedrooms

    # Calculate the number of 3-gallon cans of white paint needed for the other rooms
    num_other_room_cans = (total_other_room_gallons + 2) // 3

    # Calculate the total number of cans of paint needed
    total_cans = num_bedroom_cans + num_other_room_cans
    result = total_cans
    return result

print(solution())