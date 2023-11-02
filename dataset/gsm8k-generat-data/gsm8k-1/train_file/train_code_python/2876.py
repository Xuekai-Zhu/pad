def solution():
    """Stuart is going on a cross-country trip and wants to find the fastest route. On one route the total distance is 1500 miles and the average speed is 75 MPH. On the second trip, the total distance is 750 but the average speed is 25 MPH. How long does his trip take if he goes on the fastest route?"""
    distance_1 = 1500
    speed_1 = 75
    time_1 = distance_1 / speed_1
    
    distance_2 = 750
    speed_2 = 25
    time_2 = distance_2 / speed_2
    
    fastest_time = min(time_1, time_2)
    result = fastest_time
    
    return result

print(solution())