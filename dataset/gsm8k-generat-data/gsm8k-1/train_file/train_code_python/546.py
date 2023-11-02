def solution():
    """Tom decides to renovate a house. There are 3 bedrooms and each bedroom takes 4 hours to renovate. The kitchen takes 50% longer than each bedroom. The living room took twice as much time as everything else combined. How long did everything take?"""
    bedrooms = 3
    kitchen = bedrooms * 1.5
    living_room = (bedrooms * 4 + kitchen * 4) * 2
    total_time = (bedrooms * 4) + (kitchen * 4) + living_room
    result = total_time
    return result

print(solution())