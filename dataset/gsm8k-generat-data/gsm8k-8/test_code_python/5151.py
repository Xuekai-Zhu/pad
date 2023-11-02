def solution():
    starting_cars = 80
    cars_left = 13
    cars_in_out_diff = 5

    cars_in_lot_now = starting_cars - cars_left + cars_in_out_diff
    result = cars_in_lot_now
    return result

print(solution())