def solution():
    """Mr. Callen bought 10 paintings at $40 each and 8 wooden toys at $20 each from the crafts store to resell at a profit. However, when he sold the items, the selling price of a painting was 10% less and the selling price of a toy 15% less. Calculate the total loss Mr. Callen made from the sale of the items."""
    # Define the initial cost of the paintings and toys
    paintings_cost = 10 * 40
    toys_cost = 8 * 20

    # Calculate the selling price of the paintings and toys with the given discounts
    paintings_sell_price = 0.9 * 40
    toys_sell_price = 0.85 * 20

    # Calculate the total revenue from selling the items
    total_revenue = 10 * paintings_sell_price + 8 * toys_sell_price

    # Calculate the total loss from selling the items
    total_loss = paintings_cost + toys_cost - total_revenue

    # return the result
    result = total_loss
    return result

print(solution())