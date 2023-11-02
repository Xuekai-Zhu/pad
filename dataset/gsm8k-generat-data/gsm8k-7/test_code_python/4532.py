def solution():
    num_cows = 40
    cow_water = 80
    num_sheep = num_cows * 10
    sheep_water = cow_water * 0.25
    num_days = 7

    # Calculate the total water used by all cows in a day
    cow_water_daily = num_cows * cow_water

    # Calculate the total water used by all sheep in a day
    sheep_water_daily = num_sheep * sheep_water

    # Calculate the total water used by all animals in a day
    total_water_daily = cow_water_daily + sheep_water_daily

    # Calculate the total water used by all animals in a week
    total_water_weekly = total_water_daily * num_days
    result = total_water_weekly
    return result

print(solution())