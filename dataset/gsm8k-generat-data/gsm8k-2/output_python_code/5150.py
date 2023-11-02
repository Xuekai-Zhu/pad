def solution():
    """There were 80 cars in a parking lot. At lunchtime, 13 cars left the parking lot but 5 more cars went in than left. How many cars are in the parking lot now?"""
    initial_cars = 80
    left_cars = 13
    new_cars = left_cars - 5
    total_cars = initial_cars - left_cars + new_cars
    result = total_cars
    return result

print(solution())