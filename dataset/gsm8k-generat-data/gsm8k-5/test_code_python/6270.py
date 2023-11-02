def solution():
    # number of wheels on a bicycle
    wheels_per_bicycle = 2

    # number of wheels on a car
    wheels_per_car = 4

    # total number of wheels in the garage
    total_wheels = (9 * wheels_per_bicycle) + (16 * wheels_per_car)
    result = total_wheels
    return result

print(solution())