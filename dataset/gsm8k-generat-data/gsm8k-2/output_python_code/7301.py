def solution():
    """Linda is painting her bedroom. Her bedroom has 4 walls, with the room being 20 feet wide by 20 feet long by 8 feet tall. One wall has a 3-foot by 7-foot doorway. A second wall has a 6-foot by 4-foot window. A third wall has a 5-foot by 7-foot doorway to a walk-in-closet. And the fourth wall is completely solid. What is the total area of wall space that Linda will have to paint?"""
    room_width = 20
    room_length = 20
    room_height = 8
    door1_width = 3
    door1_height = 7
    window_width = 6
    window_height = 4
    door2_width = 5
    door2_height = 7

    area1 = room_width * room_height  # solid wall
    area2 = room_length * room_height  # solid wall
    area3 = room_width * room_height  # solid wall
    area4 = room_length * room_height  # solid wall

    area1 -= door1_width * door1_height  # deduct door1
    area2 -= window_width * window_height  # deduct window
    area3 -= door2_width * door2_height  # deduct door2

    total_area = area1 + area2 + area3 + area4
    result = total_area
    return result

print(solution())