def solution():
    num_trips_per_month = 2
    hours_per_trip = 3
    num_months_per_year = 12

    # Calculate the total number of hours Melissa spends driving in a year
    total_hours = num_trips_per_month * hours_per_trip * num_months_per_year
    result = total_hours
    return result

print(solution())