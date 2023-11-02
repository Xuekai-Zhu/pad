def solution():
    morning_water = 4
    evening_water = 6
    total_water_per_day = morning_water + evening_water  # 10 liters

    target_water = 50

    # Calculate the number of days needed to reach the target water usage
    num_days = target_water / total_water_per_day
    result = num_days
    return result

print(solution())