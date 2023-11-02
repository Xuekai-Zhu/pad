def solution():
    # Calculate the total number of minutes of TV watched on weekdays in a week
    weekday_tv = 30 * 5

    # Calculate the total number of hours of TV watched on weekends in a week
    weekend_tv = 2

    # Calculate the total number of hours of TV watched in a week
    total_tv = (weekday_tv + weekend_tv) / 60

    # Calculate the total number of hours of TV watched in 52 weeks
    yearly_tv = total_tv * 52

    result = yearly_tv
    return result

print(solution())