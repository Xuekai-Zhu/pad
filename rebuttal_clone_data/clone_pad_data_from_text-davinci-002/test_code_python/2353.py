def solution():
    cost_per_meal = 12.0
    cost_per_appetizer = 6.00
    tip_percent = 20
    tip_amount = (cost_per_meal + cost_per_appetizer) * (tip_percent / 100)
    rush_delivery_fee = 5.00
    total_cost = cost_per_meal + cost_per_appetizer + tip_amount + rush_delivery_fee
    result = total_cost
    
    return result

print(solution())