def solution():
    buses_per_hour = 2  # A bus leaves every half-hour
    hours_per_day = 12  # Buses operate for 12 hours a day
    days = 5  # We want to know how many buses leave in 5 days

    # Calculate the total number of buses that leave in 1 day
    buses_per_day = buses_per_hour * hours_per_day

    # Calculate the total number of buses that leave in 5 days
    buses_total = buses_per_day * days
    result = buses_total
    return result

print(solution())