def solution():
    """Jenna's doctor tells her that she should tan no more than 200 minutes a month. If she tans 30 minutes a day, two days a week for the first two weeks of the month, how many minutes can she tan in the last two weeks of the month?"""
    total_minutes_first_two_weeks = 30 * 2 * 2
    total_minutes_allowed_last_two_weeks = 200 - total_minutes_first_two_weeks
    minutes_per_day_last_two_weeks = total_minutes_allowed_last_two_weeks / (14 - 4)
    result = minutes_per_day_last_two_weeks
    return result

print(solution())