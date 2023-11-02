def solution():
    
    rooms = 4
    time_per_room = 4
    total_time_per_charge = 10
    total_time = rooms * time_per_room
    total_charges = total_time // total_time_per_charge + 1
    result = total_charges
    return result

print(solution())