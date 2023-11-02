def solution():
    """Johan has a ten-bedroom house with 8 walls in each room. He paints 3/5 of the rooms in the house green and paints the rest of the rooms with purple color. How many walls in the house did he paint purple?"""
    total_rooms = 10
    walls_per_room = 8
    green_rooms = (3/5) * total_rooms
    purple_rooms = total_rooms - green_rooms
    purple_walls = purple_rooms * walls_per_room
    result = purple_walls
    return result

print(solution())