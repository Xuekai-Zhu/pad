def solution():
    
    milk_price = 1.5
    fruit_price = 2
    milk_per_batch = 10
    fruit_per_batch = 3
    total_cost_per_batch = (milk_price * milk_per_batch) + (fruit_price * fruit_per_batch)
    total_cost = total_cost_per_batch * 3
    result = total_cost
    return result

print(solution())