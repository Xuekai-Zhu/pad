def solution():
    # Convert milliliters to liters
    rain_per_day = 800 / 1000  # liters of water from rain per day
    river_per_day = 1700 / 1000  # liters of water from river per day

    # Calculate the number of days needed to fill the water tank
    days_to_fill = (50 / (rain_per_day + river_per_day))
    result = days_to_fill
    return result

print(solution())