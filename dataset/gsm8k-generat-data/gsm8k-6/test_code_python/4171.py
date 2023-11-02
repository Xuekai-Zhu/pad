def solution():
    normal_car_time = 4 + 7 + 4 + 9  # time to wash a normal car
    suv_time = normal_car_time * 2  # time to wash the big SUV
    total_time = 2 * normal_car_time + suv_time  # total time to wash all the vehicles
    result = total_time
    return result

print(solution())