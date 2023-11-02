def solution():
    # Calculate the total cost of the paintings and toys
    cost_paintings = 10 * 40
    cost_toys = 8 * 20
    total_cost = cost_paintings + cost_toys

    # Calculate the total selling price of the paintings and toys
    selling_paintings = 10 * 0.9 * 40
    selling_toys = 8 * 0.85 * 20
    total_selling = selling_paintings + selling_toys

    # Calculate the total loss
    total_loss = total_cost - total_selling
    result = total_loss
    return result

print(solution())