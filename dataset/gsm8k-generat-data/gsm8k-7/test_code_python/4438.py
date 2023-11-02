def solution():
    weekdays = 15 * 5  # 75 days
    weekend_days = 15 * 2  # 30 days

    weekday_hours = 3
    weekend_hours = 4 + 5  # 9 hours

    # Calculate the total number of hours Paris studies on weekdays
    weekday_study_hours = weekdays * weekday_hours

    # Calculate the total number of hours Paris studies on weekends
    weekend_study_hours = weekend_days * weekend_hours

    # Calculate the total number of hours Paris studies during the semester
    total_study_hours = weekday_study_hours + weekend_study_hours
    result = total_study_hours
    return result

print(solution())