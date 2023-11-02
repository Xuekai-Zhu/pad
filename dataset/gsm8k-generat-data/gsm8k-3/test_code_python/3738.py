def solution():
    """Julieta went to the store to buy a backpack and three ring-binders for her school supplies. She knew the backpack was $50, and each ring-binder cost was $20. However, at the store, she found out that the price of a back had increased by $5, and the price of a ring-binder had reduced by $2. Calculate the total amount of money Julieta spent at the store."""
    # Define the original prices of the backpack and ring-binders
    BACKPACK_PRICE = 50
    RINGBINDER_PRICE = 20

    # Define the change in prices of the backpack and ring-binders
    BACKPACK_PRICE_CHANGE = 5
    RINGBINDER_PRICE_CHANGE = -2

    # Calculate the new prices of the backpack and ring-binders
    new_backpack_price = BACKPACK_PRICE + BACKPACK_PRICE_CHANGE
    new_ringbinder_price = RINGBINDER_PRICE + RINGBINDER_PRICE_CHANGE

    # Calculate the total cost of the backpack and three ring-binders
    total_cost = new_backpack_price + (new_ringbinder_price * 3)

    # Display the total cost
    result = total_cost
    return result

print(solution())