def solution():
    initial_cost = 300
    selling_price = 255

    # Calculate the loss in dollars
    loss = initial_cost - selling_price

    # Calculate the percentage of loss
    percentage_loss = (loss / initial_cost) * 100
    result = percentage_loss
    return result

print(solution())