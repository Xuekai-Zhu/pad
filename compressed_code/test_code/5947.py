def solution():
    
    initial_cars = 16
    growth_factor = 1.5
    total_cars = initial_cars * (growth_factor ** 3)
    result = total_cars
    return result

print(solution())