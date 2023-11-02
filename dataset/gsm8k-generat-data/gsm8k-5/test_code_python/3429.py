def solution():
    minutes_weekdays = 30 * 5  # Elle practices for 30 minutes on each weekday
    minutes_saturday = 30 * 3  # Elle practices three times as much on Saturday
    total_minutes = minutes_weekdays + minutes_saturday  # Calculate the total number of minutes Elle practices
    total_hours = total_minutes / 60  # Convert minutes to hours
    result = total_hours
    return result

print(solution())