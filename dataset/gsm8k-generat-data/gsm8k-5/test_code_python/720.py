def solution():
    paintings = 10
    toys = 8
    cost_paintings = 40
    cost_toys = 20
    selling_price_paintings = 40 * 0.9  # selling price of a painting is 10% less
    selling_price_toys = 20 * 0.85  # selling price of a toy is 15% less

    # Calculate the total cost of the items purchased
    total_cost = (paintings * cost_paintings) + (toys * cost_toys)

    # Calculate the total revenue from selling the items
    total_revenue = (paintings * selling_price_paintings) + (toys * selling_price_toys)

    # Calculate the total loss from the sale
    total_loss = total_cost - total_revenue
    result = total_loss
    return result

print(solution())