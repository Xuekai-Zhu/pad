def solution():
    # Calculate total minutes of TV watched during weekdays in a year
    weekdays_tv = 30 * 5 * 52  # 30 mins per night, 5 nights per week, 52 weeks per year

    # Calculate total hours of TV watched during weekends in a year
    weekend_tv = 2 * 2 * 52  # 2 hours per weekend day, 2 days per weekend, 52 weeks per year

    # Convert total minutes of TV to hours
    total_tv_hours = (weekdays_tv + weekend_tv) / 60
    result = total_tv_hours
    return result

print(solution())