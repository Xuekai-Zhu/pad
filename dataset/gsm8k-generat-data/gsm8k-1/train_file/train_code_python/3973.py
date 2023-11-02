def solution():
    """John reads his bible every day. He reads for 2 hours a day and reads at a rate of 50 pages an hour. If the bible is 2800 pages long how many weeks will it take him to read it all?"""
    daily_reading_rate = 50 * 2 # pages per day
    days_to_complete = 2800 / daily_reading_rate # total days to read
    weeks_to_complete = days_to_complete / 7 # total weeks to read
    result = weeks_to_complete
    return result

print(solution())