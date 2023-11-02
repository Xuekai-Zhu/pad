def solution():
    # Total liters of water used by cows on the farm in a week
    cow_water_weekly = 40 * 80 * 7

    # Total number of sheep on the ranch
    num_sheep = 40 * 10

    # Liters of water required by each sheep daily
    sheep_water_daily = 1/4 * 80

    # Total liters of water used by sheep on the ranch in a week
    sheep_water_weekly = num_sheep * sheep_water_daily * 7

    # Total liters of water used by all animals in a week
    total_water_weekly = cow_water_weekly + sheep_water_weekly
    result = total_water_weekly
    return result

print(solution())