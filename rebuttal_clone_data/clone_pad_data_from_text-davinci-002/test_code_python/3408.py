def solution():
    old_watts = 800
    new_watts = old_watts * 1.5
    hrs = 50
    price_increase = 25
    old_price = 0.12
    new_price = old_price * (1 + (price_increase / 100))
    old_cost = ((old_watts / 1000) * hrs) * old_price
    new_cost = ((new_watts / 1000) * hrs) * new_price
    cost_increase = new_cost - old_cost
    result = cost_increase
    
    return result

print(solution())