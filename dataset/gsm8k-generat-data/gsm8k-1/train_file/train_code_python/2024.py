def solution():
    """At a bus station, a bus leaves every half-hour for 12 hours a day. How many buses leave the station for 5 days?"""
    buses_per_hour = 2
    hours_per_day = 12
    days = 5
    total_buses = buses_per_hour * hours_per_day * days
    result = total_buses
    return result

print(solution())