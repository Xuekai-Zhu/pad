def solution():
    daily_water = 72
    bottle_size = 84
    days_per_week = 7

    # Calculate the number of times Tony will fill the water bottle in one day
    fills_per_day = daily_water / bottle_size

    # Calculate the total number of times Tony will fill the water bottle in one week
    fills_per_week = fills_per_day * days_per_week
    result = fills_per_week
    return result

print(solution())