def solution():
    
    box_cost = 7
    total_cost = box_cost * 5
    tip = total_cost / 7
    total_cost_with_tip = total_cost + tip
    payment = 100
    change = payment - total_cost_with_tip
    result = change
    return result

print(solution())