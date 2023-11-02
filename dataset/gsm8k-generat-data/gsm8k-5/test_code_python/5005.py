def solution():
    # Calculate the total number of trips Melissa makes to town in a year
    trips_per_month = 2
    trips_per_year = trips_per_month * 12

    # Calculate the total time Melissa spends driving in a year
    time_per_trip = 3
    total_time = time_per_trip * trips_per_year
    result = total_time
    return result

print(solution())