def solution():
    
    dog_cost = 1000
    profit_percent = 30
    selling_price = dog_cost + (dog_cost * (profit_percent / 100))
    quantity = 2
    total_cost = selling_price * quantity
    result = total_cost
    return result

print(solution())