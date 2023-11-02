def solution():
    total_area = 400 * 500  # Total area of the parking lot
    usable_area = 0.8 * total_area  # Only 80% of the total area is usable for parking
    car_area = 10  # It takes 10 square feet to park a car

    # Calculate the number of cars that can be parked
    num_cars = usable_area // car_area
    result = num_cars
    return result

print(solution())