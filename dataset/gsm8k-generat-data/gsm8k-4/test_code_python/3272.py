def solution():
    """John has a very inefficient toilet that uses 5 gallons of water per flush and his household flushed 15 times per day. He replaced it with a toilet that uses 80% less water per flush. How much water did John save in June?"""
    # Define the number of flushes per day and the number of days in June
    flushes_per_day = 15
    days_in_june = 30

    # Calculate the water used by the old toilet in June
    old_toilet_water = 5 * flushes_per_day * days_in_june

    # Calculate the water used by the new toilet in June
    new_toilet_water = 0.2 * old_toilet_water

    # Calculate the amount of water saved in June
    water_saved = old_toilet_water - new_toilet_water

    result = water_saved
    return result

print(solution())