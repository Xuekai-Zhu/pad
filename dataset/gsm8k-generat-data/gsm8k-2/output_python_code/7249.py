def solution():
    """Dylan's mother is throwing a baby shower for her best friend. She is expecting 40 guests, of whom she has cleared the parking lot to park in to, leaving only her car and her husband's jeep in the parking lot. The 40 guests, though, arrive in only 10 cars that they park in the parking lot. If each car has 4 wheels, how many car wheels are there in the parking lot, including both of Dylan's parent's car wheels?"""
    num_guest_cars = 10
    num_wheels_per_car = 4
    num_dylan_cars = 2
    num_wheels_dylan_cars = num_wheels_per_car * num_dylan_cars
    total_wheels = num_wheels_dylan_cars + (num_guest_cars * num_wheels_per_car)
    result = total_wheels
    return result

print(solution())