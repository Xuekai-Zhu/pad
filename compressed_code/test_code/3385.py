def solution():
    
    duck_cost = 10
    num_ducks = 30
    duck_weight = 4
    duck_sell_price = 5
    duck_purchase_price = duck_cost * num_ducks
    duck_total_weight = duck_weight * num_ducks
    duck_sell_price_total = duck_total_weight * duck_sell_price
    profit = duck_sell_price_total - duck_purchase_price
    result = profit
    return result

print(solution())