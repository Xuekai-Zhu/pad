def solution():
    daily_hours = 2
    extra_weekly_hours = 6
    num_weeks = 2

    # Calculate the total number of daily hours over two weeks
    total_daily_hours = daily_hours * 14  # 2 hours a day for 14 days

    # Calculate the total number of weekly hours over two weeks
    total_weekly_hours = (daily_hours + extra_weekly_hours) * 2  # 8 hours a week for 2 weeks

    # Calculate the total number of hours Carl will drive over two weeks
    total_hours = total_daily_hours + total_weekly_hours
    result = total_hours
    return result

print(solution())