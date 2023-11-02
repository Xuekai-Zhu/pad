def solution():
    """Linda is painting her bedroom. Her bedroom has 4 walls, with the room being 20 feet wide by 20 feet long by 8 feet tall. One wall has a 3-foot by 7-foot doorway. 
    A second wall has a 6-foot by 4-foot window. A third wall has a 5-foot by 7-foot doorway to a walk-in-closet. And the fourth wall is completely solid. 
    What is the total area of wall space that Linda will have to paint?"""
    room_width = 20
    room_length = 20
    ceiling_height = 8
    door_1_width = 3
    door_1_height = 7
    window_width = 6
    window_height = 4
    door_2_width = 5
    door_2_height = 7
    
    # Calculate the total wall area in the room
    total_area = 2 * (room_width + room_length) * ceiling_height + room_width * room_length
    
    # Calculate the area of each feature (door, window, closet)
    door_1_area = door_1_width * door_1_height
    window_area = window_width * window_height
    door_2_area = door_2_width * door_2_height
    
    # Subtract the areas of the features from the total wall area
    wall_area_to_paint = total_area - door_1_area - window_area - door_2_area
    
    result = wall_area_to_paint
    
    return result

print(solution())