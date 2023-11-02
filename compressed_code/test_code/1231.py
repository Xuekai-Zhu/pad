def solution():
    
    old_price = 2
    new_price = old_price * 1.5
    old_quantity = 4
    new_quantity = old_quantity / 2
    old_spending = old_quantity * old_price
    new_spending = new_quantity * new_price
    savings = old_spending - new_spending
    result = savings
    return result

print(solution())