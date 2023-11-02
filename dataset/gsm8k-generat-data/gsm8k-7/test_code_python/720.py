def solution():
    num_paintings = 10
    painting_cost = 40

    num_toys = 8
    toy_cost = 20

    painting_disc = 0.10
    toy_disc = 0.15

    selling_price_painting = painting_cost - (painting_cost * painting_disc)
    selling_price_toy = toy_cost - (toy_cost * toy_disc)

    # Calculate the total revenue from selling all paintings
    total_paintings_revenue = num_paintings * selling_price_painting

    # Calculate the total revenue from selling all toys
    total_toys_revenue = num_toys * selling_price_toy

    # Calculate the total cost of all items
    total_cost = (num_paintings * painting_cost) + (num_toys * toy_cost)

    # Calculate the total loss made by Mr. Callen
    total_loss = total_cost - (total_paintings_revenue + total_toys_revenue)
    result = total_loss
    return result

print(solution())