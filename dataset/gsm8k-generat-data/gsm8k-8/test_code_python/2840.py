def solution():
    # Define the number of cars and the total number of wheels in the lot
    num_cars = 19
    total_wheels = 117

    # Calculate the number of wheels from the cars
    car_wheels = num_cars * 5

    # Calculate the number of wheels from the motorcycles
    moto_wheels = total_wheels - car_wheels

    # Calculate the number of motorcycles
    num_motors = moto_wheels / 2
    result = num_motors
    return result

print(solution())