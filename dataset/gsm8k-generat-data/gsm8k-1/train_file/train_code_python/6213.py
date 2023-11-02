def solution():
    """Three planes are going to the same place but each has a different number of passengers. The first plane has 50, the second had 60, and the third has 40. An empty plane can go 600 MPH, but each passenger makes it go 2 MPH slower. What is their average speed?"""
    plane1_passengers = 50
    plane2_passengers = 60
    plane3_passengers = 40
    empty_speed = 600
    passenger_speed_reduction = 2
    
    # Calculate the speed of each plane based on the number of passengers
    plane1_speed = empty_speed - (plane1_passengers * passenger_speed_reduction)
    plane2_speed = empty_speed - (plane2_passengers * passenger_speed_reduction)
    plane3_speed = empty_speed - (plane3_passengers * passenger_speed_reduction)
    
    # Calculate the total speed of all three planes
    total_speed = plane1_speed + plane2_speed + plane3_speed
    
    # Calculate the average speed
    average_speed = total_speed / 3
    
    result = average_speed
    
    return result

print(solution())