def solution():
    
    cars = 57
    motorcycles = 73
    wheels_per_car = 4
    wheels_per_motorcycle = 2
    total_wheels = (cars * wheels_per_car) + (motorcycles * wheels_per_motorcycle)
    remaining_wheels = 650 - total_wheels
    result = remaining_wheels
    return result

print(solution())