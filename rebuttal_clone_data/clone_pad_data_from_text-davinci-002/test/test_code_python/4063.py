def solution():
    kg_of_meat = 2
    cost_per_kg = 82
    wallet_amount = 180
    total_cost = kg_of_meat * cost_per_kg
    money_left = wallet_amount - total_cost
    result = money_left
    
    return result

print(solution())