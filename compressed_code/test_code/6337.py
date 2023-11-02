def solution():
    
    paintings_bought = 10
    painting_cost = 40
    toys_bought = 8
    toy_cost = 20
    painting_sell_price = painting_cost * (1 - 0.1)
    toy_sell_price = toy_cost * (1 - 0.15)
    total_paintings_sell_price = paintings_bought * painting_sell_price
    total_toys_sell_price = toys_bought * toy_sell_price
    total_cost = (paintings_bought * painting_cost) + (toys_bought * toy_cost)
    total_sell_price = total_paintings_sell_price + total_toys_sell_price
    total_loss = total_cost - total_sell_price
    result = total_loss
    return result

print(solution())