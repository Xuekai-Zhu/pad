def solution():
    bedrooms = 10  # Johan's house has 10 bedrooms
    walls_per_room = 8  # Each room has 8 walls
    total_walls = bedrooms * walls_per_room  # Calculate the total number of walls in the house

    green_rooms = int(3/5 * bedrooms)  # Calculate the number of rooms painted green
    purple_rooms = bedrooms - green_rooms  # Calculate the number of rooms painted purple

    green_walls = green_rooms * walls_per_room  # Calculate the number of walls painted green
    purple_walls = total_walls - green_walls  # Calculate the number of walls painted purple

    result = purple_walls
    return result

print(solution())