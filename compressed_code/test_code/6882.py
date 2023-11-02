def solution():
    
    initial_price = 5
    online_price = initial_price * 2
    shipping_cost = online_price * 0.8
    total_cost = online_price + shipping_cost
    result = total_cost
    return result

print(solution())