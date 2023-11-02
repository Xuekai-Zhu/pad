def solution():
    """Jordan noticed that there are 2 cars in his driveway that each have 4 wheels. There are 2 bikes and a trash can that each have 2 wheels. There is also a tricycle and a pair of old roller skates. How many wheels are there?"""
    car_wheels = 2 * 4
    bike_wheels = 2 * 2
    trash_can_wheels = 2 * 1
    tricycle_wheels = 3
    roller_skates_wheels = 2
    total_wheels = car_wheels + bike_wheels + trash_can_wheels + tricycle_wheels + roller_skates_wheels
    result = total_wheels
    return result

print(solution())