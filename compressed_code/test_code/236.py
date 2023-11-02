def solution():
    
    floors = 4
    rooms_per_floor = 10
    room_time = 6
    hourly_pay = 15
    total_rooms = floors * rooms_per_floor
    total_time = total_rooms * room_time
    total_pay = total_time * hourly_pay
    result = total_pay
    return result

print(solution())