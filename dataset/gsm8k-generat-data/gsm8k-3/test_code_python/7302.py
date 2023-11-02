def solution():
    """
    Linda is painting her bedroom. Her bedroom has 4 walls, with the room being 20 feet wide by 20 feet long by 8 feet tall. 
    One wall has a 3-foot by 7-foot doorway. A second wall has a 6-foot by 4-foot window. A third wall has a 5-foot by 7-foot 
    doorway to a walk-in-closet. And the fourth wall is completely solid. What is the total area of wall space that Linda will 
    have to paint?
    """
    # Calculate the area of each wall and subtract the area of the door and window
    wall_area = (20 * 8) + (20 * 8) + ((20 * 20) - (3 * 7)) + ((20 * 8) - (5 * 7))
    doorway_area = 3 * 7
    window_area = 6 * 4

    # Subtract the total area of the door and window from the total wall area
    total_paint_area = wall_area - doorway_area - window_area

    # Display the total area to paint
    result = total_paint_area
    return result

print(solution())