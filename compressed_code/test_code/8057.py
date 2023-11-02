def solution():
    
    pizza_boxes = 5
    box_cost = 7
    total_cost = pizza_boxes * box_cost
    tip_percent = 1/7
    tip_amount = tip_percent * total_cost
    total_amount = total_cost + tip_amount
    payment = 100
    change = payment - total_amount
    result = change
    return result

print(solution())