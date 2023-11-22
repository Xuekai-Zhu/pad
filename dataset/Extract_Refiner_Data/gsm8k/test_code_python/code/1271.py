def solution():
    
    car_weight = 1200
    luggage_weight = 250
    children_weight = 75 * 2
    total_weight = car_weight + luggage_weight + children_weight
    force_percent = 1/100
    force_amount = total_weight * force_percent
    result = force_amount
    return result

print(solution())