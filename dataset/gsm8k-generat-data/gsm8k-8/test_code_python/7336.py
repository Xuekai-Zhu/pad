def solution():
    # Define the number of weekdays in a week
    weekdays_per_week = 5

    # Define the number of weeks
    weeks = 3

    # Define the distance Damien jogs per weekday
    distance_per_weekday = 5

    # Calculate the total distance Damien jogs over three weeks
    total_distance = weekdays_per_week * distance_per_weekday * weeks

    result = total_distance
    return result

print(solution())