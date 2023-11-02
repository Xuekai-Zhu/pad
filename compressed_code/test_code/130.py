def solution():
    
    initial_car_value = 20000
    sold_car_value = initial_car_value * 0.8
    new_car_value = 30000 * 0.9
    out_of_pocket = new_car_value - sold_car_value
    result = out_of_pocket
    return result

print(solution())