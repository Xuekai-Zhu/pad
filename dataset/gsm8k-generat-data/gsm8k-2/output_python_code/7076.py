def solution():
    """Boston had .5 feet of snow on the first day of winter. The next day they got an additional 8 inches. Over the next 2 days, 2 inches of the snow melted. On the fifth day, they received another 2 times the amount of snow they received on the first day. How many feet of snow do they now have?"""
    initial_snow = 0.5
    second_day_snow = 8 / 12  # convert inches to feet
    melted_snow = 2 / 12  # convert inches to feet
    total_snow_after_three_days = initial_snow + second_day_snow - melted_snow
    fifth_day_snow = 2 * initial_snow
    total_snow = total_snow_after_three_days + fifth_day_snow
    result = total_snow
    return result

print(solution())