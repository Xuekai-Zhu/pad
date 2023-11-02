def solution():
    
    smores_per_box = 3
    kids = 9
    adults = 6
    smores_per_kid = 2
    adults_smores = 1
    total_smores = (kids * smores_per_kid) + (adults * adults_smores)
    total_boxes = total_smores / smores_per_box
    result = total_boxes
    return result

print(solution())