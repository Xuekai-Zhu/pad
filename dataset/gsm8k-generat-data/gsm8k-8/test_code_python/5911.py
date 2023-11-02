def solution():
    normal_floor_height = 3
    last_two_floors_extra_height = 0.5 * 2
    total_floors = 20
    building_height = (normal_floor_height * (total_floors-2)) + (last_two_floors_extra_height * 2)
    result = building_height
    return result

print(solution())