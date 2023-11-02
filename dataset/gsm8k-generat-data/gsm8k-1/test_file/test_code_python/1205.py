def solution():
    """Brian's dehumidifier removes 1 liter of water per day on the low setting, twice as much on the medium setting,
    and twice as much as the medium setting on the high setting. He runs the dehumidifier for 3 days on low, 3 on medium,
    and 5 on high. How much water has been removed in total?"""
    low_speed = 1
    medium_speed = low_speed * 2
    high_speed = medium_speed * 2
    low_days = 3
    medium_days = 3
    high_days = 5
    total_water = (low_speed * low_days) + (medium_speed * medium_days) + (high_speed * high_days)
    result = total_water
    return result

print(solution())