def solution():
    morning_water = 4  # Four liters of water are used in the morning
    evening_water = 6  # Six liters of water are used in the evening
    water_per_day = morning_water + evening_water  # Total water used per day
    total_water = 50  # Sprinkler system needs to use 50 liters of water

    # Calculate the number of days it will take the sprinkler system to use 50 liters of water
    days_required = total_water / water_per_day
    result = days_required
    return result

print(solution())