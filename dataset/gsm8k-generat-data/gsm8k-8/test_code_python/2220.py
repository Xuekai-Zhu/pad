def solution():
    # Calculate Paula's time to arrive at work
    paula_time = 3/5 * 70

    # Calculate Luke's total time to travel to work and back by bus
    bus_time = 70 * 2

    # Calculate Luke's time to travel back home by bike
    bike_time = 70 * 5

    # Calculate the total time for Luke and Paula to travel to work and back each day
    total_time = paula_time + bus_time + bike_time
    result = total_time
    return result

print(solution())