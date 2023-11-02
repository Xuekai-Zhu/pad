def solution():
    """Madeline wants to drink 100 ounces of water in a day. Her water bottle can hold 12 ounces of water. She refills her water bottle 7 times. How much more water does she need to drink?"""
    water_goal = 100
    water_bottle_size = 12
    refills = 7
    total_water_consumed = water_bottle_size * refills
    remaining_water_needed = water_goal - total_water_consumed
    result = remaining_water_needed
    return result

print(solution())