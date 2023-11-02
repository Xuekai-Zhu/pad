def solution():
    """Matt wants to repaint his house. He needs to paint three walls in his living room, which is a square 40 feet by 40 feet,
    and all four walls in his bedroom, which is a rectangle 10 feet by 12 feet. All the walls in Matt's house are 10 feet tall.
    How many total square feet of wall does Matt need to paint?"""
    living_room_wall_area = 3 * (40 * 10)
    bedroom_wall_area = 4 * (10 * 10 + 12 * 10)
    total_wall_area = living_room_wall_area + bedroom_wall_area
    result = total_wall_area
    return result

print(solution())