def solution():
    """William washes cars as a side job. He typically spends 4 minutes washing a car’s windows, 7 minutes washing the car body, 4 minutes cleaning the tires, and 9 minutes waxing the car. This morning he washed 2 normal cars and one big SUV, which took twice as long as a normal car. How many minutes did William spend washing all the vehicles?"""
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