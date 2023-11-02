def solution():
    
    car_weight = 1200
    luggage_weight = 250
    young_weight = 75 * 2
    total_weight = car_weight + luggage_weight + young_weight
    force_to_move = total_weight * 0.01
    result = force_to_move
    return result

print(solution())