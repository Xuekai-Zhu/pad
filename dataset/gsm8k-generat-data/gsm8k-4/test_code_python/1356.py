def solution():
    """Johan has a ten-bedroom house with 8 walls in each room. He paints 3/5 of the rooms in the house green and paints the rest of the rooms with purple color. How many walls in the house did he paint purple?"""
    # Define the number of rooms in the house and the number of walls in each room
    num_rooms = 10
    walls_per_room = 8

    # Calculate the total number of walls in the house
    total_walls = num_rooms * walls_per_room

    # Calculate the number of rooms painted green
    green_rooms = int(num_rooms * 3/5)

    # Calculate the number of walls painted green
    green_walls = green_rooms * walls_per_room

    # Calculate the number of walls painted purple
    purple_walls = total_walls - green_walls

    # Return the result
    result = purple_walls
    return result

print(solution())