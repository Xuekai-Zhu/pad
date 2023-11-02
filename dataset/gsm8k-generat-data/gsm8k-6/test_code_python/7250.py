def solution():
    # Calculate the total number of car wheels in the parking lot
    num_cars = 10
    num_wheels = (num_cars * 4) + (2 * 4)  # each car has 4 wheels, and there are 2 cars belonging to Dylan's parents
    result = num_wheels
    return result

print(solution())