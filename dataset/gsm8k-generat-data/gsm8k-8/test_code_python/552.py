def solution():
    # Calculate the total usable area for parking
    total_area = 400 * 500
    usable_area = total_area * 0.8

    # Calculate the number of cars that can be parked
    car_area = 10
    num_cars = usable_area / car_area
    result = num_cars
    return result

print(solution())