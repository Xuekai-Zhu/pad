def solution():
    
    plate_weight = 10 / 16  
    box_weight_limit = 20
    plates_per_box = 38

    current_weight = plates_per_box * plate_weight
    while current_weight > box_weight_limit:
        plates_per_box -= 1
        current_weight = plates_per_box * plate_weight

    removed_plates = 38 - plates_per_box
    result = removed_plates
    return result

print(solution())