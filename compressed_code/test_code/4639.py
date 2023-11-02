def solution():
    
    total_boxes = 80
    ali_circles = 5
    ali_boxes_used = ali_circles * 8
    remaining_boxes = total_boxes - ali_boxes_used
    ernie_circles = remaining_boxes // 10
    result = ernie_circles
    return result

print(solution())