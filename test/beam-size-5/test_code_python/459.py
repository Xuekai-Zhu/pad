def solution():
    
    delivery_cost = 15
    tip_ratio = 1/5
    tip_amount = delivery_cost * tip_ratio
    total_amount = delivery_cost + tip_amount
    result = total_amount
    return result

print(solution())