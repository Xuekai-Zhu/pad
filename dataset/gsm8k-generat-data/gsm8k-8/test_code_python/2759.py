def solution():
    # Calculate total time spent biking
    biking_time = 30

    # Calculate total time spent on the bus
    bus_time = (30 + 10) * 3

    # Calculate total time spent riding with friend
    friend_biking_time = biking_time * (1 - 2/3)
    friend_time = friend_biking_time + 10

    # Calculate total time spent commuting
    total_time = biking_time + bus_time + friend_time

    # Convert total time from minutes to hours and round to 2 decimal places
    result = round(total_time / 60, 2)
    return result

print(solution())