def solution():
    """Mr. Callen bought 10 paintings at $40 each and 8 wooden toys at $20 each from the crafts store to resell at a profit. However, when he sold the items, the selling price of a painting was 10% less and the selling price of a hat 15% less. Calculate the total loss Mr. Callen made from the sale of the items."""
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