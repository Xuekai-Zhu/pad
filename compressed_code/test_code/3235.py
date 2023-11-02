def solution():
    
    truck_half_tank = 20 / 2
    car_one_third_tank = 12 / 3
    total_gallons_added = (20 - truck_half_tank) + (12 - car_one_third_tank)
    result = total_gallons_added
    return result

print(solution())