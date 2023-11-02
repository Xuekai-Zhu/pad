def solution():
    
    initial_balance = 85
    item_cost = 15
    sale_price = 20
    towels_price = 30
    sale_discount = 0.2
    towels_discount = 0.1
    new_balance = initial_balance - (item_cost * sale_discount) - (item_cost * towels_discount) - (item_cost * towels_discount)
    result = new_balance
    return result

print(solution())