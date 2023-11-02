def solution():
    original_reading_time = 2 # Mark used to read for 2 hours a day
    increased_reading_time = original_reading_time * 2.5 # Mark increased his reading time by 150%
    total_reading_time = increased_reading_time * 7 # Mark reads for 7 days a week now

    original_daily_reading = 100 # Mark used to read 100 pages a day
    total_weekly_reading = total_reading_time * original_daily_reading # Calculate total weekly reading

    result = total_weekly_reading
    return result

print(solution())