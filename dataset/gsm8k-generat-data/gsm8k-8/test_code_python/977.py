def solution():
    # Calculate the number of wheels from the trucks
    truck_wheels = 12 * 4

    # Calculate the number of wheels from the cars
    car_wheels = 13 * 4

    # Calculate the total number of wheels seen
    total_wheels_seen = truck_wheels + car_wheels

    result = total_wheels_seen
    return result

print(solution())