def solution():
    
    total_vehicles = 300
    car_truck_ratio = 2
    total_cars = (2/3) * total_vehicles
    total_trucks = (1/3) * total_vehicles
    truck_ratio = 1 / (car_truck_ratio + 1)
    actual_trucks = truck_ratio * total_vehicles
    result = actual_trucks
    return result

print(solution())