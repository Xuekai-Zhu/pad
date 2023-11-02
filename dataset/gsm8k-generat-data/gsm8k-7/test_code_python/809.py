def solution():
    morning_walk = 1.5  # miles
    evening_walk = 1.5  # miles
    num_days = 30

    # Calculate the total number of miles walked in one day
    total_miles_per_day = morning_walk + evening_walk

    # Calculate the total number of miles walked in 30 days
    total_miles = total_miles_per_day * num_days
    result = total_miles
    return result

print(solution())