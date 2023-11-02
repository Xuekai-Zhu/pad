def solution():
    """The parking lot in front of the school has 52 parking spaces. The parking lot in the back of the school has 38 spaces. If 39 cars have parked and 1/2 of the spaces of the back are filled, how many parking spaces are still available in the school?"""
    front_spaces = 52
    back_spaces = 38
    cars_parked = 39
    back_filled = back_spaces / 2
    total_filled = cars_parked + back_filled
    total_available = front_spaces + back_spaces - total_filled
    result = total_available
    return result

print(solution())