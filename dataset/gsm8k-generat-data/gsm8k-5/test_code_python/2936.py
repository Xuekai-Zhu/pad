def solution():
    total_cars = 516  # There are 516 cars in the parking lot

    # Calculate the number of blue cars
    blue_cars = total_cars / 3

    # Calculate the number of red cars
    red_cars = total_cars / 2

    # Calculate the number of black cars
    black_cars = total_cars - blue_cars - red_cars
    result = black_cars
    return result

print(solution())