def solution():
    # Define the number of wheels for each type of vehicle
    bike_wheels = 2
    car_wheels = 4
    moto_wheels = 2

    # Calculate the total number of wheels in the garage
    total_wheels = (20 * bike_wheels) + (10 * car_wheels) + (5 * moto_wheels)
    result = total_wheels
    return result

print(solution())