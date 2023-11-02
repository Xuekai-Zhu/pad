def solution():
    """Three planes are going to the same place but each has a different number of passengers. The first plane has 50, the second had 60, and the third has 40. An empty plane can go 600 MPH, but each passenger makes it go 2 MPH slower. What is their average speed?"""
    # Define the number of passengers for each plane
    passengers1 = 50
    passengers2 = 60
    passengers3 = 40

    # Define the speed reduction per passenger
    speed_reduction = 2

    # Calculate the total number of passengers
    total_passengers = passengers1 + passengers2 + passengers3

    # Calculate the total speed reduction
    total_reduction = speed_reduction * total_passengers

    # Calculate the final speed of the planes
    final_speed = 600 - total_reduction

    # Calculate the average speed of the planes
    average_speed = final_speed / 3

    # Display the average speed
    result = average_speed
    return result

print(solution())