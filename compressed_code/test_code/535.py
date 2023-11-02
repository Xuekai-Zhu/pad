def solution():
    
    paintings_cost = 10 * 40
    toys_cost = 8 * 20
    total_cost = paintings_cost + toys_cost
    paintings_sell_price = 0.9 * 40
    toys_sell_price = 0.85 * 20
    total_sell_price = 10 * paintings_sell_price + 8 * toys_sell_price
    total_loss = total_cost - total_sell_price
    result = total_loss
    return result

print(solution())