def solution():
    starting_gallons = 40
    water_lost_per_hour = 2

    # Calculate the total amount of water lost in the first two hours
    total_water_lost = water_lost_per_hour * 2

    # Calculate the amount of water left after two hours
    water_left_after_two_hours = starting_gallons - total_water_lost

    # Calculate the amount of water after adding 1 gallon in the third hour
    water_after_third_hour = water_left_after_two_hours + 1

    # Calculate the amount of water after adding 3 gallons in the fourth hour
    water_after_fourth_hour = water_after_third_hour + 3
    result = water_after_fourth_hour
    return result

print(solution())