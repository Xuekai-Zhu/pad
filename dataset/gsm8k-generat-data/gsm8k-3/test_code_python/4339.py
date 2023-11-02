def solution():
    """Matilda bought a smartphone for $300. Then she decided she wouldn't use it anyway and sold it for $255. What percentage of the initial cost did she lose?"""
    # Define the initial cost and the selling price
    initial_cost = 300
    selling_price = 255

    # Calculate the amount of loss
    loss = initial_cost - selling_price

    # Calculate the percentage of loss
    percentage_loss = (loss / initial_cost) * 100

    # Display the percentage of loss
    result = percentage_loss
    return result

print(solution())