def solution():
    
    plates_needed = 65
    green_plates = 22
    blue_plates = 24
    total_plates = green_plates + blue_plates
    plates_to_buy = plates_needed - total_plates
    result = plates_to_buy
    return result

print(solution())