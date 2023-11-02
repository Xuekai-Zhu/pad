def solution():
    """William washes cars as a side job. He typically spends 4 minutes washing a car’s windows, 7 minutes washing the car body, 4 minutes cleaning the tires, and 9 minutes waxing the car. This morning he washed 2 normal cars and one big SUV, which took twice as long as a normal car. How many minutes did William spend washing all the vehicles?"""
    normal_car_time = 4 + 7 + 4 + 9
    suv_time = 2 * normal_car_time
    total_time = (2 * normal_car_time) + suv_time
    result = total_time
    return result

print(solution())