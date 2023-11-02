def solution():
    # Define the initial cost and selling price
    initial_cost = 300
    selling_price = 255

    # Calculate the difference between the selling price and the initial cost
    cost_difference = initial_cost - selling_price

    # Calculate the percentage of the initial cost that was lost
    percentage_lost = cost_difference / initial_cost * 100
    result = percentage_lost
    return result

print(solution())