def solution():
    
    packets_per_day = 2
    packets_per_box = 30
    cost_per_box = 4
    days = 90
    packets_needed = packets_per_day * days
    boxes_needed = packets_needed / packets_per_box
    cost = boxes_needed * cost_per_box
    result = cost
    return result

print(solution())