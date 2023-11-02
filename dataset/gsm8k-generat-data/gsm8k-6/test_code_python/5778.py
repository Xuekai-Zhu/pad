def solution():
    daily_hours = 2  # daily hours of driving
    weekly_hours = 6  # additional weekly hours of driving
    total_hours = (daily_hours * 7) + weekly_hours  # total hours of driving per week
    two_weeks_hours = total_hours * 2  # total hours of driving in two weeks
    result = two_weeks_hours
    return result

print(solution())