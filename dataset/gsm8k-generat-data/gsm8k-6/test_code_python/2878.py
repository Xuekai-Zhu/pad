def solution():
    bedroom_watts = 6  # watts used by bedroom light per hour
    office_watts = 3 * bedroom_watts  # watts used by office light per hour
    living_room_watts = 4 * bedroom_watts  # watts used by living room light per hour
    total_watts = (bedroom_watts + office_watts + living_room_watts) * 2  # total watts used in 2 hours
    result = total_watts
    return result

print(solution())