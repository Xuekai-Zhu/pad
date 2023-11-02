def solution():
    initial_cost = 300  # dollars
    selling_price = 255  # dollars
    loss = initial_cost - selling_price  # dollars
    loss_percentage = (loss / initial_cost) * 100  # percentage
    result = loss_percentage
    return result

print(solution())