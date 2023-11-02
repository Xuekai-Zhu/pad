def solution():
    """There were 80 cars in a parking lot. At lunchtime, 13 cars left the parking lot but 5 more cars went in than left. How many cars are in the parking lot now?"""
    # Define the initial number of cars
    INITIAL_CARS = 80

    # Calculate the number of cars that left the parking lot
    cars_left = 13

    # Calculate the number of cars that went in after lunchtime
    cars_in = cars_left - 5

    # Calculate the current number of cars in the parking lot
    current_cars = INITIAL_CARS - cars_left + cars_in

    # return the result
    result = current_cars
    return result

print(solution())