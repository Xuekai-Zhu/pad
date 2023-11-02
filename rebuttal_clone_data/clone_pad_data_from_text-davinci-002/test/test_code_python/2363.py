def solution():
    time_normal_car_windows = 4
    time_normal_car_body = 7
    time_normal_car_tires = 4
    time_normal_car_waxing = 9
    time_suv_car_windows = time_normal_car_windows * 2
    time_suv_car_body = time_normal_car_body * 2
    time_suv_car_tires = time_normal_car_tires * 2
    time_suv_car_waxing = time_normal_car_waxing * 2
    total_time = (time_normal_car_windows + time_normal_car_body + time_normal_car_tires + time_normal_car_waxing) * 2 + (time_suv_car_windows + time_suv_car_body + time_suv_car_tires + time_suv_car_waxing)
    result = total_time
    return result

print(solution())