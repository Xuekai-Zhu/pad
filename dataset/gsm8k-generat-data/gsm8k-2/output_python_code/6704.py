def solution():
    """Mark is injured so decides to spend more time reading. He used to read 2 hours a day but increased that by 150%. Before he read 100 pages a day. How many pages does he read a week now?"""
    previous_reading_time = 2 * 7  # 2 hours a day for 7 days
    increased_reading_time = previous_reading_time * 2.5  # 150% increase
    previous_daily_reading = 100
    increased_daily_reading = previous_daily_reading * 2.5  # 150% increase
    total_weekly_reading = (previous_daily_reading * 7) + (increased_daily_reading * 7)
    result = total_weekly_reading
    return result

print(solution())