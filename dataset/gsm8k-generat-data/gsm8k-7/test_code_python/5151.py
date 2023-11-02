def solution():
    initial_cars = 80
    cars_left = 13
    cars_in = cars_left + 5

    # Calculate the current number of cars in the parking lot
    current_cars = initial_cars - cars_left + cars_in
    result = current_cars
    return result

print(solution())