def solution():
    
    days = 40
    pods_per_day = 3
    pods_per_box = 30
    cost_per_box = 8.00
    total_pods = days * pods_per_day
    boxes_needed = total_pods / pods_per_box
    total_cost = boxes_needed * cost_per_box
    result = total_cost
    return result

print(solution())