def solution():
    required_height = 54
    current_height = 48
    growth_per_hour = 1/12
    growth_per_month = 1/3

    # Calculate how much height Alex needs to gain in total
    height_difference = required_height - current_height

    # Calculate how much height Alex would gain in a month without hanging upside down
    normal_growth_per_month = growth_per_month * 12

    # Calculate how much additional height Alex needs to gain each month by hanging upside down
    upside_down_growth_per_month = height_difference - normal_growth_per_month

    # Calculate how many hours Alex needs to hang upside down each month to gain the required additional height
    hours_per_month = upside_down_growth_per_month / growth_per_hour

    result = round(hours_per_month, 1)
    return result

print(solution())