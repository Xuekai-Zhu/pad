def solution():
    
    boxes_per_week = 2
    price_per_box = 3.00
    weeks_per_year = 52
    total_boxes = boxes_per_week * weeks_per_year
    total_cost = total_boxes * price_per_box
    result = total_cost
    return result

print(solution())