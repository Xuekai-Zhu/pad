def solution():
    morning_reading_time = (30 * 5)  # 30 minutes per day for 5 days in a week
    evening_reading_time = (60 * 5)  # 1 hour per day for 5 days in a week

    # Double the reading time on weekends
    weekend_morning_reading_time = (30 * 2) * 2  # 2 hours of reading time on Saturday and Sunday
    weekend_evening_reading_time = (60 * 2) * 2  # 4 hours of reading time on Saturday and Sunday

    # Calculate the total reading time for the week
    total_reading_time = morning_reading_time + evening_reading_time + weekend_morning_reading_time + weekend_evening_reading_time
    result = total_reading_time
    return result

print(solution())