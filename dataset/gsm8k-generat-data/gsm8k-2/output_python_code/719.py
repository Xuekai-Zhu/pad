def solution():
    """Mr. Callen bought 10 paintings at $40 each and 8 wooden toys at $20 each from the crafts store to resell at a profit.
    However, when he sold the items, the selling price of a painting was 10% less and the selling price of a hat 15% less.
    Calculate the total loss Mr. Callen made from the sale of the items."""
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