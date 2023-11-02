def solution():
    """James writes a comic every other day for 4 years. If there was no leap year, how many comics has he written?"""
    days_in_4_years = 365 * 4
    comics_every_other_day = days_in_4_years // 2
    result = comics_every_other_day
    return result

print(solution())