def solution():
    
    truck_tank = 20
    car_tank = 12
    truck_current = truck_tank / 2
    car_current = car_tank / 3
    total_added = (truck_tank - truck_current) + (car_tank - car_current)
    result = total_added
    return result

print(solution())