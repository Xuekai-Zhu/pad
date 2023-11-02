def solution():
    """It takes a duck 40 days to fly to the south during winter, twice as much time to fly to the north during summer, and 60 days to travel to the East during spring. How many days is the duck flying during these seasons?"""
    south_time = 40
    north_time = south_time * 2
    east_time = 60
    total_flying_time = south_time + north_time + east_time
    result = total_flying_time
    return result

print(solution())