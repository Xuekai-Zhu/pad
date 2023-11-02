def solution():
    old_system_cost= 250
    trade_in_value = old_system_cost * 0.8
    new_system_cost = 600
    discount = new_system_cost * 0.25
    total_cost = new_system_cost - discount - trade_in_value
    result = total_cost

    return result

print(solution())