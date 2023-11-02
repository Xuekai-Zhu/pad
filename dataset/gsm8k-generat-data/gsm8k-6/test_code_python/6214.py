def solution():
    # Calculate the total number of passengers
    total_passengers = 50 + 60 + 40
    # Calculate the reduction in speed per passenger
    speed_reduction = total_passengers * 2
    # Calculate the total speed reduction
    total_speed_reduction = speed_reduction * 3
    # Calculate the total speed of the planes
    total_speed = 600 * 3
    # Calculate the average speed
    average_speed = (total_speed - total_speed_reduction) / 3
    result = average_speed
    return result

print(solution())