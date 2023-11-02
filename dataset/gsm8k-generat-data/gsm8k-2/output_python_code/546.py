def solution():
    """Tom decides to renovate a house. There are 3 bedrooms and each bedroom takes 4 hours to renovate. The kitchen takes 50% longer than each bedroom. The living room took twice as much time as everything else combined. How long did everything take?"""
    bedroom_time = 4
    kitchen_time = 1.5 * bedroom_time
    living_room_time = 2 * (bedroom_time + kitchen_time)
    total_time = (3 * bedroom_time) + kitchen_time + living_room_time
    result = total_time
    return result

print(solution())