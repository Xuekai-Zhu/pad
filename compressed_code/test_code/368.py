def solution():
    
    electricity_price = 0.10
    consumption_rate = 2.4
    total_hours = 25
    total_consumed = consumption_rate * total_hours
    total_cost = total_consumed * electricity_price
    result = total_cost
    return result

print(solution())