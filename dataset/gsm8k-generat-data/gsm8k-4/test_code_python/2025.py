def solution():
    """At a bus station, a bus leaves every half-hour for 12 hours a day. How many buses leave the station for 5 days?"""
    # Define the number of buses per day
    buses_per_day = 24 // 0.5

    # Calculate the number of buses over 5 days
    buses_5_days = buses_per_day * 12 * 5

    result = buses_5_days
    return result

print(solution())