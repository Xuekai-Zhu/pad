def solution():
    shower_time_per_day = 10  # in minutes
    shower_frequency = 2  # every other day
    num_weeks = 4

    # Calculate the total number of showers John takes in 4 weeks
    total_showers = (num_weeks * 7) / shower_frequency

    # Calculate the total amount of water John uses in all his showers
    water_per_minute = 2  # gallons per minute
    total_water_usage = total_showers * shower_time_per_day * water_per_minute

    result = total_water_usage
    return result

print(solution())