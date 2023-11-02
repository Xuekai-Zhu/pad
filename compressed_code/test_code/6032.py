def solution():
    
    num_floors = 4
    rooms_per_floor = 10
    hours_per_room = 6
    hourly_rate = 15
    total_rooms = num_floors * rooms_per_floor
    total_hours = total_rooms * hours_per_room
    total_pay = total_hours * hourly_rate
    result = total_pay
    return result

print(solution())