def solution():
    total_vehicles = 300
    car_count = 2
    truck_count = 1
    total_cars = car_count * truck_count
    total_trucks = (total_vehicles // (car_count + truck_count)) * truck_count
    result = total_trucks
    return result

print(solution())