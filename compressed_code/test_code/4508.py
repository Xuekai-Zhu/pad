def solution():
    
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