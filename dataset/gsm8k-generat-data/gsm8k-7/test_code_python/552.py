def solution():
    length = 400
    width = 500

    # Calculate the area of the parking lot
    total_area = length * width

    # Calculate the usable area for parking
    usable_area = total_area * 0.8

    # Calculate the number of cars that can be parked
    car_space = 10
    num_cars = usable_area / car_space
    result = num_cars
    return result

print(solution())