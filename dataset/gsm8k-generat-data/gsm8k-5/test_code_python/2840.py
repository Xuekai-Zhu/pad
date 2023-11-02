def solution():
    cars = 19  # number of cars in the parking lot
    car_wheels = 5  # each car has 5 wheels
    motorbike_wheels = 2  # each motorcycle has 2 wheels
    total_wheels = 117  # total number of wheels in the parking lot

    # Calculate the total number of car wheels
    total_car_wheels = cars * car_wheels

    # Calculate the total number of motorcycle wheels
    total_motorbike_wheels = total_wheels - total_car_wheels

    # Calculate the number of motorcycles
    motorcycles = total_motorbike_wheels // motorbike_wheels
    result = motorcycles
    return result

print(solution())