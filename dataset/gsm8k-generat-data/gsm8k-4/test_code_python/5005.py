def solution():
    """Melissa works on a poultry farm. She drives to town twice each month to buy supplies. If it takes her 3 hours to drive to town and back, how many hours does Melissa spend driving in a year?"""
    # Define the number of trips Melissa takes to town each month
    trips_per_month = 2

    # Define the time it takes for Melissa to drive to town and back
    time_per_trip = 3

    # Calculate the total time Melissa spends driving in a year
    driving_time_per_year = trips_per_month * time_per_trip * 12

    # return the result
    result = driving_time_per_year
    return result

print(solution())