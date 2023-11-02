def solution():
    # Calculate the cost price of the paintings and wooden toys
    cost_paintings = 10 * 40
    cost_toys = 8 * 20
    total_cost = cost_paintings + cost_toys

    # Calculate the selling price of the paintings and wooden toys after the discount
    selling_price_paintings = 0.9 * 40
    selling_price_toys = 0.85 * 20

    # Calculate the total selling price of the paintings and wooden toys
    total_selling_price = (10 * selling_price_paintings) + (8 * selling_price_toys)

    # Calculate the loss made by Mr. Callen
    total_loss = total_cost - total_selling_price
    result = total_loss
    return result

print(solution())