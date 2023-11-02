def solution():
    # Define the number of passengers on each plane
    plane1_passengers = 50
    plane2_passengers = 60
    plane3_passengers = 40

    # Calculate the total number of passengers
    total_passengers = plane1_passengers + plane2_passengers + plane3_passengers

    # Calculate the total slowdown caused by passengers
    total_slowdown = 2 * total_passengers

    # Calculate the total speed of the planes
    total_speed = 3 * 600 - total_slowdown

    # Calculate the average speed
    average_speed = total_speed / 3
    result = average_speed
    return result

print(solution())