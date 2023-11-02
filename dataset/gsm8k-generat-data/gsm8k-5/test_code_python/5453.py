def solution():
    # Calculate the total amount of time Bryan spends traveling in one round trip
    total_time = (5 + 20 + 5) * 2  # Bryan walks 5 minutes to the station, rides the bus for 20 minutes, then walks 5 minutes to his job, and does the same on the way back

    # Convert the total time to hours
    hours_per_round_trip = total_time / 60

    # Calculate the number of workdays in a year
    workdays_per_year = 365

    # Calculate the total number of hours Bryan spends traveling per year
    total_hours = hours_per_round_trip * workdays_per_year
    result = total_hours
    return result

print(solution())