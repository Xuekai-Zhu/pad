def solution():
    """Stuart is going on a cross-country trip and wants to find the fastest route. On one route the total distance is 1500 miles and the average speed is 75 MPH. On the second trip, the total distance is 750 but the average speed is 25 MPH. How long does his trip take if he goes on the fastest route?"""
    # Calculate the time it takes for the first route
    time1 = 1500 / 75

    # Calculate the time it takes for the second route
    time2 = 750 / 25

    # Choose the faster route and calculate the total time
    if time1 < time2:
        total_time = time1
    else:
        total_time = time2

    result = total_time
    return result

print(solution())