def solution():
    # Calculate the number of cars in the parking lot after lunch
    cars_left = 13
    cars_in_out = cars_left - 5
    cars_now = 80 - cars_left + cars_in_out
    result = cars_now
    return result

print(solution())