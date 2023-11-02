def solution():
    """John reads his bible every day. He reads for 2 hours a day and reads at a rate of 50 pages an hour. If the bible is 2800 pages long how many weeks will it take him to read it all?"""
    daily_reading_time = 2  # hours
    reading_rate = 50  # pages per hour
    bible_length = 2800  # pages
    daily_reading_progress = daily_reading_time * reading_rate
    total_days = bible_length // daily_reading_progress
    weeks = total_days // 7
    result = weeks
    return result

print(solution())