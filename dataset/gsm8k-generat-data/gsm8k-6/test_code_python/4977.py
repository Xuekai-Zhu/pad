def solution():
    # Calculate the total amount of water used by the sprinkler system each day
    total_water_per_day = 4 + 6  # four liters in the morning and six liters in the evening

    # Calculate the number of days it will take to use 50 liters of water
    days = 50 // total_water_per_day  # using integer division to get whole number of days
    result = days
    return result

print(solution())