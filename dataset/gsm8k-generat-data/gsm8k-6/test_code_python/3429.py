def solution():
    # Calculate the total amount of time Elle practices piano in a week
    weekday_minutes = 30 * 5  # Elle practices for 30 minutes from Monday to Friday
    saturday_minutes = 3 * 30  # Elle practices three times as much on Saturday as on a weekday
    total_minutes = weekday_minutes + saturday_minutes  # total minutes of practice in a week
    total_hours = total_minutes / 60  # convert minutes to hours
    result = total_hours
    return result

print(solution())