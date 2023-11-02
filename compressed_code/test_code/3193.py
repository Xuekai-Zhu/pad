def solution():
    
    budget = 60
    shower_gel_price = 4
    toothpaste_price = 3
    remaining_budget = 30
    shower_gel_total_price = shower_gel_price * 4
    total_spent = budget - remaining_budget - shower_gel_total_price - toothpaste_price
    detergent_price = total_spent
    result = detergent_price
    return result

print(solution())