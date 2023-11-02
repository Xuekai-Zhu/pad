def solution():
    daily_hours = 2  # The driver drives an average of 2 hours each day
    days_per_week = 5  # The driver works 5 days per week
    total_hours = daily_hours * days_per_week  # The driver works a total of 10 hours in a week

    # Calculate the distance traveled from Monday to Wednesday
    distance_mon_wed = 12 * total_hours/2  # The driver traveled at an average speed of 12 km/hr

    # Calculate the distance traveled from Thursday to Friday
    distance_thu_fri = 9 * total_hours/2  # The driver traveled at an average speed of 9 km/hr

    # Calculate the total distance traveled during the 5 days
    total_distance = distance_mon_wed + distance_thu_fri
    result = total_distance
    return result

print(solution())