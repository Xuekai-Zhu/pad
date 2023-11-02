def solution():
    """James writes a comic every other day for 4 years. If there was no leap year, how many comics has he written?"""
    days_per_year = 365
    years = 4
    comics_per_day = 1/2
    days_written = days_per_year * years
    comics_written = days_written * comics_per_day
    result = comics_written
    return result

print(solution())