def solution():
    meters_per_minute = 10
    minutes_per_hour = 60
    hours_per_day = 24
    days = 2

    # Calculate the total number of minutes Lisa walks in two days
    total_minutes = hours_per_day * days * minutes_per_hour

    # Calculate the total number of meters Lisa walks in two days
    total_meters = meters_per_minute * total_minutes
    result = total_meters
    return result

print(solution())