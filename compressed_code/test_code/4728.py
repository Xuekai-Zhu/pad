def solution():
    
    gas_prices = [3, 3.5, 4, 4.5]
    total_gallons = 24  
    total_cost = 0
    for i in range(4):
        gallons = 12
        cost = gallons * gas_prices[i]
        total_cost += cost
    result = total_cost
    return result

print(solution())