def solution():
    initial_room_area = 13 * 18
    increased_room_area = (13 + 2) * (18 + 2)
    three_room_areas = 3 * increased_room_area
    double_room_area = 2 * increased_room_area
    total_area = initial_room_area + three_room_areas + double_room_area
    result = total_area
    
    return result

print(solution())