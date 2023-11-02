def solution():
    initial_cost = 300  # Matilda bought the smartphone for $300
    selling_price = 255  # Matilda sold the smartphone for $255

    # Calculate the loss percentage
    loss_percentage = ((initial_cost - selling_price) / initial_cost) * 100
    result = loss_percentage
    return result

print(solution())