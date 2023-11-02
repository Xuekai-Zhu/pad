def solution():
    """At a bus station, a bus leaves every half-hour for 12 hours a day. How many buses leave the station for 5 days?"""
    # Define the number of buses leaving per half-hour
    BUSES_PER_HALF_HOUR = 1

    # Define the number of hours per day
    HOURS_PER_DAY = 12

    # Define the number of days
    DAYS = 5

    # Calculate the total number of buses leaving the station
    total_buses = BUSES_PER_HALF_HOUR * 2 * HOURS_PER_DAY * DAYS

    # Display the total number of buses leaving the station
    result = total_buses
    return result

print(solution())