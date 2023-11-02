def solution():
    """The parking lot in front of the school has 52 parking spaces. The parking lot in the back of the school has 38 spaces. If 39 cars have parked and 1/2 of the spaces of the back are filled, how many parking spaces are still available in the school?"""
    # Define the number of parking spaces
    FRONT_SPACES = 52
    BACK_SPACES = 38

    # Calculate the number of cars parked in the back
    back_cars = BACK_SPACES * 0.5

    # Calculate the total number of cars parked
    total_cars = 39 + back_cars

    # Calculate the number of available parking spaces
    available_spaces = FRONT_SPACES + BACK_SPACES - total_cars

    # Display the number of available parking spaces
    result = available_spaces
    return result

print(solution())