def solution():
    # Calculate the total cost for Steve to order the DVD online
    online_cost = 2 * 5  # Steve paid twice as much as Mike
    shipping_cost = 0.8 * online_cost  # 80% of the price of the film is the shipping cost
    total_cost = online_cost + shipping_cost

    result = total_cost
    return result

print(solution())