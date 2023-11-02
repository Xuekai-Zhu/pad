def solution():
    
    old_system_cost = 250
    trade_in_value = old_system_cost * 0.8
    new_system_cost_before_discount = 600
    discount_percentage = 0.25
    discount_amount = new_system_cost_before_discount * discount_percentage
    new_system_cost = new_system_cost_before_discount - discount_amount
    total_cost = new_system_cost - trade_in_value
    result = total_cost
    return result

print(solution())