def solution():
    """Three planes are going to the same place but each has a different number of passengers. The first plane has 50, the second had 60, and the third has 40. An empty plane can go 600 MPH, but each passenger makes it go 2 MPH slower. What is their average speed?"""
    # Define the number of passengers and the speed reduction per passenger
    passengers = [50, 60, 40]
    speed_reduction = 2

    # Calculate the total speed of each plane
    plane_speeds = []
    for p in passengers:
        plane_speed = 600 - p * speed_reduction
        plane_speeds.append(plane_speed)

    # Calculate the total distance (assuming they are all going the same distance)
    distance = 1000

    # Calculate the total time taken for all three planes
    total_time = 0
    for speed in plane_speeds:
        time = distance / speed
        total_time += time

    # Calculate the average speed
    average_speed = distance / total_time

    # Return the result
    result = round(average_speed)
    return result

print(solution())