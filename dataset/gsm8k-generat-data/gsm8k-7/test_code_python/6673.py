def solution():
    time_to_office = 30    # minutes
    time_home = 30         # minutes
    weekend_drive = 2 * 60 # 2 hours in minutes

    # Calculate total driving time during the weekdays
    total_weekday_drive = (time_to_office + time_home) * 5 # 5 weekdays

    # Calculate total driving time during the weekends
    total_weekend_drive = weekend_drive * 2 # 2 weekend days

    # Calculate total driving time for the week
    total_drive_time = (total_weekday_drive + total_weekend_drive) / 60 # convert to hours

    result = total_drive_time
    return result

print(solution())