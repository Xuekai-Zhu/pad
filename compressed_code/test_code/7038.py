def solution():
    
    original_price = 2
    raised_price = original_price * 1.5
    original_coffees = 4
    new_coffees = original_coffees / 2
    original_total_cost = original_price * original_coffees
    new_total_cost = raised_price * new_coffees
    savings = original_total_cost - new_total_cost
    result = savings
    return result

print(solution())