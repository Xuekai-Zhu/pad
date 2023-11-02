def solution():
    
    battery_life = 10
    time_per_room = 4
    num_rooms = 4
    time_to_clean = time_per_room * num_rooms
    num_charges = time_to_clean // battery_life + 1
    result = num_charges
    return result

print(solution())