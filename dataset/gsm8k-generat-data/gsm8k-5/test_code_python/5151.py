def solution():
    initial_cars = 80  # There were initially 80 cars in the parking lot
    cars_left = 13  # 13 cars left the parking lot
    cars_in = cars_left + 5  # 5 more cars went in than left

    # Calculate the current number of cars in the parking lot
    current_cars = initial_cars - cars_left + cars_in
    result = current_cars
    return result

print(solution())