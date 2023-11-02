def solution():
    """Stuart is going on a cross-country trip and wants to find the fastest route. On one route the total distance is 1500 miles and the average speed is 75 MPH. On the second trip, the total distance is 750 but the average speed is 25 MPH. How long does his trip take if he goes on the fastest route?"""
    # Calculate the time taken for the first route
    time_route1 = 1500 / 75

    # Calculate the time taken for the second route
    time_route2 = 750 / 25

    # Compare the times and choose the fastest route
    if time_route1 < time_route2:
        fastest_route_time = time_route1
    else:
        fastest_route_time = time_route2

    # Display the fastest route time
    result = fastest_route_time
    return result

print(solution())