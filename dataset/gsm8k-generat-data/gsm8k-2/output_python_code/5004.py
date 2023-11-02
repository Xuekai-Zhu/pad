def solution():
    """Melissa works on a poultry farm. She drives to town twice each month to buy supplies. If it takes her 3 hours to drive to town and back, how many hours does Melissa spend driving in a year?"""
    trips_per_month = 2
    total_trips_per_year = 12 * trips_per_month
    round_trip_time = 3
    total_drive_time_per_year = total_trips_per_year * round_trip_time
    result = total_drive_time_per_year
    return result

print(solution())