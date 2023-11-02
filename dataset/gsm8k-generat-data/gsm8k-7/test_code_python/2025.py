def solution():
    buses_per_hour = 2  # a bus leaves every half-hour
    hours_per_day = 12
    days = 5

    # Calculate the total number of buses that leave in a day
    buses_per_day = buses_per_hour * hours_per_day

    # Calculate the total number of buses that leave in 5 days
    total_buses = buses_per_day * days
    result = total_buses
    return result

print(solution())