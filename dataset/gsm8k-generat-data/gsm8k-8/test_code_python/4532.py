def solution():
    # Calculate the total amount of water used by the cows in a week
    cow_water_weekly = 40 * 80 * 7

    # Calculate the number of sheep on the ranch
    sheep_count = 10 * 40

    # Calculate the amount of water used by one sheep in a day
    sheep_water_daily = 0.25 * 80

    # Calculate the total amount of water used by the sheep in a week
    sheep_water_weekly = sheep_count * sheep_water_daily * 7

    # Calculate the total amount of water used for all animals in a week
    total_water_weekly = cow_water_weekly + sheep_water_weekly
    result = total_water_weekly
    return result

print(solution())