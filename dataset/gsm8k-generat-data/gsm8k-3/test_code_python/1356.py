def solution():
    """Johan has a ten-bedroom house with 8 walls in each room. He paints 3/5 of the rooms in the house green and paints the rest of the rooms with purple color. How many walls in the house did he paint purple?"""
    # Define the number of bedrooms, walls per room, and green room ratio
    BEDROOMS = 10
    WALLS_PER_ROOM = 8
    GREEN_ROOM_RATIO = 3/5

    # Calculate the number of green rooms and purple rooms
    green_rooms = int(BEDROOMS * GREEN_ROOM_RATIO)
    purple_rooms = BEDROOMS - green_rooms

    # Calculate the number of purple walls
    purple_walls = purple_rooms * WALLS_PER_ROOM

    # Display the number of purple walls
    result = purple_walls
    return result

print(solution())