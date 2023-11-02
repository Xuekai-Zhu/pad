def solution():
    
    # Define the dimensions of the bedrooms
    bedroom_length = 20
    bedroom_width = 12

    # Calculate the area of the bedrooms
    bedroom_area = bedroom_length * bedroom_width

    # Calculate the area of the living room
    living_room_area = bedroom_area * 5

    # Calculate the area of the remaining house
    remaining_house_area = 1000 - bedroom_area - living_room_area

    # Calculate the total area of the house
    total_area = bedroom_area + living_room_area + remaining_house_area

    # return the result
    result = total_area
    return result

print(solution())