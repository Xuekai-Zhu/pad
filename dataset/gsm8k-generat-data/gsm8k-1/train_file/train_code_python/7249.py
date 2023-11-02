def solution():
    """Dylan's mother is throwing a baby shower for her best friend. She is expecting 40 guests, of whom she has cleared the parking lot to park in to, leaving only her car and her husband's jeep in the parking lot. The 40 guests, though, arrive in only 10 cars that they park in the parking lot. If each car has 4 wheels, how many car wheels are there in the parking lot, including both of Dylan's parent's car wheels?"""
    guests = 40
    cleared_parking_spots = 2
    cars = 10
    wheels_per_car = 4
    total_wheels = (cleared_parking_spots + cars) * wheels_per_car
    result = total_wheels
    return result

print(solution())