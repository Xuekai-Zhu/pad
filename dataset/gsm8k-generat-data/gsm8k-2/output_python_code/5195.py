def solution():
    """Mark is reading books, for 2 hours each day. He decided to increase his time spent on reading books weekly, by 4 hours. How much time does Mark want to spend during one week on reading books?"""
    daily_reading_time = 2
    additional_weekly_reading_time = 4
    weekly_reading_time = (daily_reading_time * 7) + additional_weekly_reading_time
    result = weekly_reading_time
    return result

print(solution())