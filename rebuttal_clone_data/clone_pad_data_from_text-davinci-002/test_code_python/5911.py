def solution():
    total_floors = 20
    standard_floor = 3
    last_two_floors = 0.5
    total_height = (total_floors - 2) * standard_floor + (last_two_floors * 2)
    result = total_height
    return result

print(solution())