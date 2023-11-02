def solution():
    # Calculate total reading time from Monday to Friday
    weekday_reading_time = 5 * (30 + 60)  # morning newspaper reading + evening novel reading

    # Double reading time on weekends
    weekend_reading_time = 2 * (2 * 30 + 2 * 60)  # 2 times the usual time for both morning and evening reading

    # Calculate total weekly reading time
    total_reading_time = weekday_reading_time + weekend_reading_time

    result = total_reading_time
    return result

print(solution())