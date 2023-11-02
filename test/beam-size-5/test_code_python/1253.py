def solution():
    
    sticks_needed = 56
    popsicles_per_box = 8
    boxes_needed = sticks_needed / popsicles_per_box
    cost_per_box = 2
    total_cost = boxes_needed * cost_per_box
    result = total_cost
    return result

print(solution())