def solution():
    
    lunch_cost = 100
    sales_tax = 0.04 * lunch_cost
    tip = 0.06 * lunch_cost
    total_cost = lunch_cost + sales_tax + tip
    result = total_cost
    return result

print(solution())