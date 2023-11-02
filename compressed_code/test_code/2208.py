def solution():
    
    car_wheels = 5
    motorcycle_wheels = 2
    total_cars = 19
    total_wheels = 117
    car_wheels_count = total_cars * car_wheels
    motorcycle_wheels_count = total_wheels - car_wheels_count
    motorcycle_count = motorcycle_wheels_count / motorcycle_wheels
    result = motorcycle_count
    return result

print(solution())