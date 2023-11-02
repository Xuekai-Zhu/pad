def solution():
    # Calculate the total number of walls in the house
    total_walls = 10 * 8

    # Calculate the number of rooms he painted green and purple
    green_rooms = round((10 * 3) / 5)
    purple_rooms = 10 - green_rooms

    # Calculate the number of walls he painted purple
    purple_walls = purple_rooms * 8

    result = purple_walls
    return result

print(solution())