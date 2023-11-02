def solution():
    # Calculate the amount of water used by the old toilet per day
    old_toilet_water = 5 * 15  # 5 gallons of water per flush, 15 flushes per day

    # Calculate the amount of water used by the new toilet per day
    new_toilet_water = 0.2 * 5 * 15  # 80% less water per flush, 5 gallons per flush, 15 flushes per day

    # Calculate the amount of water saved per day
    water_saved_per_day = old_toilet_water - new_toilet_water

    # Calculate the total water saved in June (assuming 30 days)
    water_saved_in_June = water_saved_per_day * 30

    result = water_saved_in_June
    return result

print(solution())