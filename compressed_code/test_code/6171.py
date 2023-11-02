def solution():
    
    kw_price = 0.10
    consumption_rate = 2.4
    total_hours = 25
    total_consumption = consumption_rate * total_hours
    total_cost = total_consumption * kw_price
    result = total_cost
    return result

print(solution())