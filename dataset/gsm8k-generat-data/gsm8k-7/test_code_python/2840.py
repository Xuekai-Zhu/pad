def solution():
    num_cars = 19
    wheels_per_car = 5
    wheels_per_motorcycle = 2
    total_wheels = 117

    # Calculate the total number of wheels from all cars
    total_wheels_from_cars = num_cars * wheels_per_car

    # Calculate the total number of wheels from all motorcycles
    total_wheels_from_motorcycles = total_wheels - total_wheels_from_cars

    # Calculate the number of motorcycles
    num_motorcycles = total_wheels_from_motorcycles / wheels_per_motorcycle
    result = num_motorcycles
    return result

print(solution())