def solution():
    
    gallons_per_box = 30
    cost_per_box = 40
    boxes_per_week = 180 // gallons_per_box
    total_cost = boxes_per_week * cost_per_box
    result = total_cost
    return result

print(solution())