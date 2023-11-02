def solution():
    
    total_donuts = 10 * 12
    donuts_left = total_donuts - 12 - 8
    donuts_per_box = 10
    boxes_filled = donuts_left // donuts_per_box
    result = boxes_filled
    return result

print(solution())