def solution():
    # Each car has 4 wheels, including the spare tire
    wheels_per_car = 4

    # There are 30 4-wheel drive cars in the parking lot
    num_cars = 30

    # Multiply the number of cars by the number of wheels per car to get the total number of wheels
    total_wheels = num_cars * wheels_per_car

    # Multiply the total number of wheels by 2 to get the total number of tires, since each tire consists of 2 wheels
    total_tires = total_wheels * 2
    result = total_tires
    return result

print(solution())