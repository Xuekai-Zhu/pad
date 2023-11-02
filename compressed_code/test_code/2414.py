def solution():
    
    soda_per_box = 30
    price_per_box = 40
    total_boxes_needed = 180 / soda_per_box
    total_cost = total_boxes_needed * price_per_box
    result = total_cost
    return result

print(solution())