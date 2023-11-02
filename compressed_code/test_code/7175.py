def solution():
    
    packets_per_day = 2
    packets_per_box = 30
    days_per_box = packets_per_box / packets_per_day
    boxes_needed = 90 / days_per_box
    cost_per_box = 4
    total_cost = boxes_needed * cost_per_box

    result = total_cost
    return result

print(solution())