def solution():
    num_cars = 30
    num_wheels_per_car = 4
    num_spare_tires_per_car = 1

    # Calculate the total number of wheels on all cars in the parking lot
    total_wheels = num_cars * num_wheels_per_car

    # Calculate the total number of spare tires in the parking lot
    total_spare_tires = num_cars * num_spare_tires_per_car

    # Calculate the total number of tires in the parking lot
    total_tires = total_wheels + total_spare_tires
    result = total_tires
    return result

print(solution())