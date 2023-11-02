def solution():
    # Define the water usage per day
    daily_water_usage = 4 + 6  # 10 liters per day

    # Calculate the number of days it will take to use 50 liters
    days_to_reach_50_liter = 50 / daily_water_usage

    result = int(round(days_to_reach_50_liter)) # Round up to the nearest integer
    return result

print(solution())