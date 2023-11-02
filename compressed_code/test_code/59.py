def solution():
    
    craft_price = 12
    sold_crafts = 3
    extra_money = 7
    total_profit = (sold_crafts * craft_price) + extra_money
    deposit_amount = 18
    left_amount = total_profit - deposit_amount
    result = left_amount
    return result

print(solution())