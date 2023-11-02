def solution():
    """Linda is painting her bedroom. Her bedroom has 4 walls, with the room being 20 feet wide by 20 feet long by 8 feet tall. One wall has a 3-foot by 7-foot doorway. A second wall has a 6-foot by 4-foot window. A third wall has a 5-foot by 7-foot doorway to a walk-in-closet. And the fourth wall is completely solid. What is the total area of wall space that Linda will have to paint?"""
    # Define the dimensions of the room and the openings
    room_width = 20
    room_length = 20
    room_height = 8
    doorway_1_width = 3
    doorway_1_height = 7
    window_width = 6
    window_height = 4
    doorway_2_width = 5
    doorway_2_height = 7

    # Calculate the area of each wall
    wall_1_area = room_length * room_height
    wall_2_area = room_width * room_height
    wall_3_area = room_length * room_height
    wall_4_area = room_width * room_height

    # Calculate the area of the openings on the walls
    doorway_1_area = doorway_1_width * doorway_1_height
    window_area = window_width * window_height
    doorway_2_area = doorway_2_width * doorway_2_height

    # Calculate the total area of the walls to be painted
    total_area = (wall_1_area + wall_2_area + wall_3_area + wall_4_area) - (doorway_1_area + window_area + doorway_2_area)

    result = total_area
    return result

print(solution())