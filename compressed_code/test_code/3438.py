def solution():
    
    boxes_of_pencils = 2
    pencils_per_box = 12
    total_pencils = boxes_of_pencils * pencils_per_box
    lauren_pencils = 6
    matt_pencils = 3 + lauren_pencils
    total_given_pencils = lauren_pencils + matt_pencils
    remaining_pencils = total_pencils - total_given_pencils
    result = remaining_pencils
    return result

print(solution())