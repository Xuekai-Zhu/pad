def solution():
    living_room_area = 3 * (40 * 10)  # Three walls, each 40 feet by 10 feet
    bedroom_area = 4 * ((10 * 10) + (12 * 10))  # Four walls, two with area 10 x 10 feet and two with area 12 x 10 feet

    total_wall_area = living_room_area + bedroom_area
    result = total_wall_area
    return result

print(solution())