def solution():
    """Mr. Callen bought 10 paintings at $40 each and 8 wooden toys at $20 each from the crafts store to resell at a profit. However, when he sold the items, the selling price of a painting was 10% less and the selling price of a hat 15% less. Calculate the total loss Mr. Callen made from the sale of the items."""
    # Define the cost of each painting and toy
    PAINTING_COST = 40
    TOY_COST = 20

    # Define the number of paintings and toys purchased
    num_paintings = 10
    num_toys = 8

    # Calculate the total cost of the paintings and toys
    total_cost = (num_paintings * PAINTING_COST) + (num_toys * TOY_COST)

    # Calculate the selling price of each painting and toy after discount
    selling_price_painting = PAINTING_COST - (PAINTING_COST * 0.1)
    selling_price_toy = TOY_COST - (TOY_COST * 0.15)

    # Calculate the total revenue from selling all the paintings and toys
    total_revenue = (num_paintings * selling_price_painting) + (num_toys * selling_price_toy)

    # Calculate the total loss
    total_loss = total_cost - total_revenue

    result = total_loss
    return result

print(solution())