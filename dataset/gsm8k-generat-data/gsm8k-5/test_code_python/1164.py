def solution():
    starting_water = 40  # The tank starts with 40 gallons of water
    water_loss_per_hour = 2  # The tank loses 2 gallons of water per hour
    water_added_hour_3 = 1  # Hayden adds 1 gallon of water in hour three
    water_added_hour_4 = 3  # Hayden adds 3 gallons of water in hour four

    # Calculate the amount of water left after each hour
    water_hour_1 = starting_water - (water_loss_per_hour * 1)  # No water added in hour one
    water_hour_2 = water_hour_1 - (water_loss_per_hour * 1)  # No water added in hour two
    water_hour_3 = water_hour_2 + water_added_hour_3  # 1 gallon added in hour three
    water_hour_4 = water_hour_3 + water_added_hour_4  # 3 gallons added in hour four

    result = water_hour_4
    return result

print(solution())