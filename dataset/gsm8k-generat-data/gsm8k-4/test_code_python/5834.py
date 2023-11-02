def solution():
    """The parking lot in front of the school has 52 parking spaces. The parking lot in the back of the school has 38 spaces. If 39 cars have parked and 1/2 of the spaces of the back are filled, how many parking spaces are still available in the school?"""
    # Define the total number of parking spaces
    total_spaces = 52 + 38

    # Calculate the number of cars parked in the back lot
    back_lot_cars = 0.5 * 38

    # Calculate the total number of parked cars
    parked_cars = 39 + back_lot_cars

    # Calculate the number of available parking spaces
    available_spaces = total_spaces - parked_cars

    # return the result
    result = available_spaces
    return result

print(solution())