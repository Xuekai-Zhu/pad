def solution():
    
    red_pencils = 20
    blue_pencils = red_pencils * 2
    yellow_pencils = 40
    green_pencils = red_pencils + blue_pencils
    total_pencils = red_pencils + blue_pencils + yellow_pencils + green_pencils
    boxes_needed = total_pencils // 20
    result = boxes_needed
    return result

print(solution())