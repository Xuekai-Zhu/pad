def solution():
    
    bedroom_light_watt = 6
    office_light_watt = 3 * bedroom_light_watt
    living_room_light_watt = 4 * bedroom_light_watt
    total_watts = (bedroom_light_watt + office_light_watt + living_room_light_watt) * 2
    result = total_watts
    return result

print(solution())