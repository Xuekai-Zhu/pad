def solution():
    """Stuart is going on a cross-country trip and wants to find the fastest route. On one route the total distance is 1500 miles and the average speed is 75 MPH. On the second trip, the total distance is 750 but the average speed is 25 MPH. How long does his trip take if he goes on the fastest route?"""
    time1 = 1500 / 75
    time2 = 750 / 25
    fastest_time = min(time1, time2)
    result = fastest_time
    return result

print(solution())