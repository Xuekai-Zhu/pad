def solution():
    num_motorcycles = 12
    num_cars = 10

    # Calculate the total number of tires on all motorcycles
    total_motorcycle_tires = num_motorcycles * 2

    # Calculate the total number of tires on all cars
    total_car_tires = num_cars * 4

    # Calculate the total number of tires changed
    total_tires_changed = total_motorcycle_tires + total_car_tires
    result = total_tires_changed
    return result

print(solution())