def solution():
    normal_car_time = 4 + 7 + 4 + 9 # Time to wash a normal car (in minutes)
    suv_time = normal_car_time * 2 # Time to wash an suv (in minutes)

    # Calculate the total time William spent washing the cars
    total_time = (2 * normal_car_time) + suv_time
    
    result = total_time
    return result

print(solution())