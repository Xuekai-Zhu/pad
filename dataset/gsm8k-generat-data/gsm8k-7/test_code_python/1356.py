def solution():
    num_bedrooms = 10
    walls_per_room = 8

    # Calculate the total number of walls in the house
    total_walls = num_bedrooms * walls_per_room

    # Calculate the number of rooms painted green
    green_rooms = (3/5) * num_bedrooms

    # Calculate the number of rooms painted purple
    purple_rooms = num_bedrooms - green_rooms

    # Calculate the total number of purple walls
    purple_walls = purple_rooms * walls_per_room

    result = purple_walls
    return result

print(solution())