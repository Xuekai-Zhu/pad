def solution():
    """Tony drinks 72 ounces of water per day. He decides that to stop wasting plastic, he will buy a reusable metal bottle. If he buys an 84-ounce water bottle, how many times will he fill it each week?"""
    daily_water_consumption = 72
    weekly_water_consumption = daily_water_consumption * 7
    bottle_size = 84
    fill_times_per_week = weekly_water_consumption // bottle_size
    result = fill_times_per_week
    return result

print(solution())