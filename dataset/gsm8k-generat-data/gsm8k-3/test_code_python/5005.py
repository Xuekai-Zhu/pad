def solution():
    """Melissa works on a poultry farm. She drives to town twice each month to buy supplies. If it takes her 3 hours to drive to town and back, how many hours does Melissa spend driving in a year?"""
    # Calculate the number of trips Melissa makes in a year
    trips_per_month = 2
    months_per_year = 12
    total_trips = trips_per_month * months_per_year

    # Calculate the total time Melissa spends driving in a year
    time_per_trip = 3
    total_time = total_trips * time_per_trip

    # Display the total time Melissa spends driving in a year
    result = total_time
    return result

print(solution())