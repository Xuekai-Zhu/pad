def solution():
    """The parking lot in front of the school has 52 parking spaces. The parking lot in the back of the school has 38 spaces. If 39 cars have parked and 1/2 of the spaces of the back are filled, how many parking spaces are still available in the school?"""
    front_spaces = 52
    back_spaces = 38
    parked_cars = 39
    back_filled_spaces = 0.5 * back_spaces
    total_filled_spaces = parked_cars + back_filled_spaces
    total_spaces = front_spaces + back_spaces
    available_spaces = total_spaces - total_filled_spaces
    result = available_spaces
    return result

print(solution())