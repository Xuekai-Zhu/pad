def solution():
    
    bedroom_light = 6
    office_light = bedroom_light * 3
    living_room_light = bedroom_light * 4
    total_watts = (bedroom_light + office_light + living_room_light) * 2
    result = total_watts
    return result

print(solution())