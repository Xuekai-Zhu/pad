def solution():
    marathon_distance = 26  # Marathon is 26 miles
    first_10_miles_time = 1  # Time to run the first 10 miles is 1 hour

    # Calculate the time to run the remaining 16 miles
    remaining_distance = marathon_distance - 10
    remaining_pace = 0.8 * (60 / 7)  # 80% of the original pace of 7 miles per hour
    remaining_time = remaining_distance / remaining_pace

    # Calculate total race time
    total_time = first_10_miles_time + remaining_time
    result = total_time
    return result

print(solution())