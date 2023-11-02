def solution():
    plane1_passengers = 50
    plane2_passengers = 60
    plane3_passengers = 40
    empty_plane_speed = 600
    passenger_speed_reduction = 2

    # Calculate the total number of passengers on all three planes
    total_passengers = plane1_passengers + plane2_passengers + plane3_passengers

    # Calculate the speed reduction due to passengers on all three planes
    total_speed_reduction = total_passengers * passenger_speed_reduction

    # Calculate the total speed of all three planes with passengers
    total_speed = empty_plane_speed - total_speed_reduction

    # Calculate the average speed of all three planes
    avg_speed = total_speed / 3
    result = avg_speed
    return result

print(solution())