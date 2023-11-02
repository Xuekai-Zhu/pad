def solution():
    """Dylan's mother is throwing a baby shower for her best friend. She is expecting 40 guests, of whom she has cleared the parking lot to park in to, leaving only her car and her husband's jeep in the parking lot. The 40 guests, though, arrive in only 10 cars that they park in the parking lot. If each car has 4 wheels, how many car wheels are there in the parking lot, including both of Dylan's parent's car wheels?"""
    # Define the number of guests and cars
    guests = 40
    cars = 10

    # Define the number of wheels per car
    wheels_per_car = 4

    # Calculate the total number of wheels in the parking lot
    total_wheels = (cars + 2) * wheels_per_car

    # return the result
    result = total_wheels
    return result

print(solution())