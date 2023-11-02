def solution():
    """Calculate the total price of a refrigerator and washing machine."""
    # Define the price of the refrigerator
    fridge_price = 4275

    # Calculate the price of the washing machine
    washer_price = fridge_price - 1490

    # Calculate the total price of the purchases
    total_price = fridge_price + washer_price

    # Return the total price
    result = total_price
    return result

print(solution())