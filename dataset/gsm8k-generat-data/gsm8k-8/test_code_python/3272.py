def solution():
    # Calculate the total water used in a day with the old toilet
    old_toilet_water = 5 * 15

    # Calculate the water used in a day with the new toilet
    new_toilet_water = 0.2 * old_toilet_water

    # Calculate the water saved per day
    water_saved_per_day = old_toilet_water - new_toilet_water

    # Calculate the water saved in June (assuming 30 days)
    water_saved_in_june = 30 * water_saved_per_day
    result = water_saved_in_june
    return result

print(solution())