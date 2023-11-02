def solution():
    
    initial_cars = 16
    growth_rate = 1.5
    final_cars = initial_cars * (growth_rate ** 3)
    result = final_cars
    return result

print(solution())