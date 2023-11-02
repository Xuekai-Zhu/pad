def solution():
    
    old_price_per_kwh = 0.12
    new_price_per_kwh = old_price_per_kwh * 1.25
    old_power_usage = 800 / 1000 
    new_power_usage = old_power_usage * 1.5
    total_power_usage = new_power_usage * 50 
    cost = total_power_usage * new_price_per_kwh
    result = cost
    return result

print(solution())