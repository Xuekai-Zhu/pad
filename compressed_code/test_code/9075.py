def solution():
    
    minutes_windows = 4
    minutes_body = 7
    minutes_tires = 4
    minutes_wax = 9

    normal_car_time = minutes_windows + minutes_body + minutes_tires + minutes_wax
    suv_time = normal_car_time * 2

    total_time = (normal_car_time * 2) + suv_time

    result = total_time

    return result

print(solution())