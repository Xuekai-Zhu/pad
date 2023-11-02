def solution():
    bedroom_light = 6
    office_light = 3 * bedroom_light
    living_room_light = 4 * bedroom_light
    hours_used = 2
    watts_used = (bedroom_light * hours_used) + (office_light * hours_used) + (living_room_light * hours_used) 
    result = watts_used
    return result

print(solution())