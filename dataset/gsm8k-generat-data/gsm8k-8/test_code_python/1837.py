def solution():
    # Convert arrival time to minutes - 9.00 a.m. = 540
    arrival_time = 540

    # Convert bus pickup time to minutes - 6.00 a.m. = 360
    pickup_time = 360

    # Calculate the time taken for the bus to reach the first station
    first_stop_time = 40

    # Calculate the time taken from the first station to Mr. Langsley's workplace
    travel_time = arrival_time - (pickup_time + first_stop_time)

    result = travel_time
    return result

print(solution())