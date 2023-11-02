def solution():
    """Three planes are going to the same place but each has a different number of passengers. The first plane has 50, the second had 60, and the third has 40. An empty plane can go 600 MPH, but each passenger makes it go 2 MPH slower. What is their average speed?"""
    plane1_passengers = 50
    plane2_passengers = 60
    plane3_passengers = 40
    empty_plane_speed = 600
    passenger_slowdown_speed = 2
    total_passengers = plane1_passengers + plane2_passengers + plane3_passengers
    total_slowdown = total_passengers * passenger_slowdown_speed
    total_speed = empty_plane_speed - total_slowdown
    average_speed = total_speed / 3
    result = average_speed
    return result

print(solution())