def solution():
    # Calculate the area of the parking lot
    total_area = 400 * 500

    # Calculate the usable area for parking
    usable_area = 0.8 * total_area

    # Calculate the number of cars that can be parked
    num_cars = usable_area / 10

    result = num_cars
    return result

print(solution())