def solution():
    # Calculate the total time for one round trip to work
    round_trip_time = 5 + 20 + 5 + 20 + 5 + 5

    # Calculate the total time for one day
    total_time_per_day = round_trip_time * 2

    # Calculate the total time for one year
    total_time_per_year = total_time_per_day * 365

    # Convert the total time to hours
    total_hours_per_year = total_time_per_year / 60

    result = total_hours_per_year
    return result

print(solution())