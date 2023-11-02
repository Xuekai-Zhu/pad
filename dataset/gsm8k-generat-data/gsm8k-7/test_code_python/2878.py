def solution():
    bedroom_light_watts = 6
    office_light_watts = 3 * bedroom_light_watts
    living_room_light_watts = 4 * bedroom_light_watts
    hours_on = 2

    # Calculate the total number of watts used by all three lights
    total_watts = (bedroom_light_watts + office_light_watts + living_room_light_watts) * hours_on
    result = total_watts
    return result

print(solution())