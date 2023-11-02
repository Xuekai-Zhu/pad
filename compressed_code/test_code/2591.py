def solution():
    
    plates_weight = 10 / 16  
    max_weight = 20
    num_plates = 38
    current_weight = plates_weight * num_plates
    while current_weight > max_weight:
        num_plates -= 1
        current_weight = plates_weight * num_plates
    result = 38 - num_plates
    return result

print(solution())