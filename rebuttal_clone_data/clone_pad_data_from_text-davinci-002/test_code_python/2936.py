def solution():
    cars_in_lot = 516
    blue_cars = cars_in_lot / 3
    red_cars = cars_in_lot / 2
    black_cars = cars_in_lot - (blue_cars + red_cars)
    result = black_cars
    return result

print(solution())