def solution():
    # Calculate Paula's bus ride duration
    paula_bus_duration = (3/5) * 70  # Paula takes 3/5 of Luke's bus ride duration

    # Calculate Luke's bike ride duration
    luke_bike_duration = 5 * 70  # Luke's bike ride is 5 times slower than his bus ride

    # Calculate the total time they spend traveling to and from work
    total_duration = 2 * 70 + paula_bus_duration + luke_bike_duration  # 2 bus rides for Luke, 1 bus ride for Paula, 1 bike ride for Luke

    result = total_duration
    return result

print(solution())