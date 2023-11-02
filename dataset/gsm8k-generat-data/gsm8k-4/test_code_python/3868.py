def solution():
    """A 220-liter barrel has a small leak. It lost 10% of its contents before anyone noticed. How many liters are left in the barrel?"""
    # Define the initial size of the barrel and the percentage of the contents lost
    initial_size = 220
    loss_percentage = 10

    # Calculate the amount of contents lost
    loss = initial_size * (loss_percentage / 100)

    # Calculate the amount of contents remaining
    remaining = initial_size - loss

    # return the result
    result = remaining
    return result

print(solution())