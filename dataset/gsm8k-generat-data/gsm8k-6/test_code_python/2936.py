def solution():
    # Calculate the number of blue and red cars in the parking lot
    blue_cars = 516 / 3
    red_cars = 516 / 2

    # Calculate the number of black cars in the parking lot
    black_cars = 516 - blue_cars - red_cars
    result = black_cars
    return result

print(solution())