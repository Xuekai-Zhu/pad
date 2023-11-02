def solution():
    
    total_floors = 10
    available_floors = total_floors - 1
    rooms_per_floor = 10
    total_rooms = available_floors * rooms_per_floor
    result = total_rooms
    return result

print(solution())