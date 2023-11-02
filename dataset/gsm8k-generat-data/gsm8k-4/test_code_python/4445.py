def solution():
    """Matt wants to repaint his house. He needs to paint three walls in his living room, which is a square 40 feet by 40 feet, and all four walls in his bedroom, which is a rectangle 10 feet by 12 feet. All the walls in Matt's house are 10 feet tall. How many total square feet of wall does Matt need to paint?"""
    # Calculate the area of the living room walls
    living_room_area = 3 * 40 * 10

    # Calculate the area of the bedroom walls
    bedroom_area = 2 * 10 * 10 + 2 * 12 * 10

    # Calculate the total area of wall to paint
    total_area = living_room_area + bedroom_area

    # return the result
    result = total_area
    return result

print(solution())