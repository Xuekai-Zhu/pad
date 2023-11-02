def solution():
    """There were 80 cars in a parking lot. At lunchtime, 13 cars left the parking lot but 5 more cars went in than left. How many cars are in the parking lot now?"""
    initial_cars = 80
    cars_left = 13
    cars_in = cars_left + 5
    total_cars = initial_cars - cars_left + cars_in
    result = total_cars
    return result

print(solution())