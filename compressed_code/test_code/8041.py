def solution():
    
    car_wheels = 5
    motorcycle_wheels = 2
    total_vehicles = 19
    total_wheels = 117
    
    car_total_wheels = total_vehicles * car_wheels
    
    motorcycle_total_wheels = total_wheels - car_total_wheels
    
    motorcycles = motorcycle_total_wheels // motorcycle_wheels
    result = motorcycles
    return result

print(solution())