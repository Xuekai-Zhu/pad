def solution():
    """Matilda bought a smartphone for $300. Then she decided she wouldn't use it anyway and sold it for $255. What percentage of the initial cost did she lose?"""
    # Define the initial cost and selling price
    initial_cost = 300
    selling_price = 255

    # Calculate the loss
    loss = initial_cost - selling_price

    # Calculate the percentage of loss
    loss_percentage = (loss / initial_cost) * 100

    # Return the result
    result = loss_percentage
    return result

print(solution())