def solution():
    bedroom_light = 6  # Noah's bedroom light uses 6 watts per hour
    office_light = bedroom_light * 3  # Noah's office light uses three times as much energy as his bedroom light
    living_room_light = bedroom_light * 4  # Noah's living room light uses four times as much energy as his bedroom light
    total_time = 2  # Noah has left all the lights on for 2 hours

    # Calculate the total energy used by all the lights
    total_watts = (bedroom_light + office_light + living_room_light) * total_time
    result = total_watts
    return result

print(solution())