def solution():
    # Calculate the time it takes to wash one normal car
    normal_car_time = 4 + 7 + 4 + 9

    # Calculate the time it takes to wash the SUV
    suv_time = normal_car_time * 2

    # Calculate the total time spent washing all vehicles
    total_time = (2 * normal_car_time) + suv_time

    result = total_time
    return result

print(solution())