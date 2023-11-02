def solution():
    front_spaces = 52
    back_spaces = 38
    parked_cars = 39
    back_filled = 0.5

    # Calculate the number of cars parked in the back
    back_parked = back_spaces * back_filled

    # Calculate the total number of parked cars
    total_parked = parked_cars + back_parked

    # Calculate the number of available parking spaces
    available_spaces = front_spaces + back_spaces - total_parked
    result = available_spaces
    return result

print(solution())