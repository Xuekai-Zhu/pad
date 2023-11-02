def solution():
    # Define the energy usage of each light
    bedroom_light = 6
    office_light = 3 * bedroom_light
    living_room_light = 4 * bedroom_light

    # Calculate the total energy usage in two hours
    total_watts = 2 * (bedroom_light + office_light + living_room_light)
    result = total_watts
    return result

print(solution())