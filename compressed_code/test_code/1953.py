def solution():
    
    nuggets_per_box = 20
    cost_per_box = 4
    total_nuggets = 100
    boxes_needed = total_nuggets // nuggets_per_box + (1 if total_nuggets % nuggets_per_box > 0 else 0)
    total_cost = boxes_needed * cost_per_box
    result = total_cost
    return result

print(solution())