def solution():
    """Julieta went to the store to buy a backpack and three ring-binders for her school supplies. She knew the backpack was $50, and each ring-binder cost was $20. However, at the store, she found out that the price of a back had increased by $5, and the price of a ring-binder had reduced by $2. Calculate the total amount of money Julieta spent at the store."""
    # Define the original prices of the backpack and ring-binders
    original_backpack_price = 50
    original_ringbinder_price = 20

    # Calculate the new prices of the backpack and ring-binders
    new_backpack_price = original_backpack_price + 5
    new_ringbinder_price = original_ringbinder_price - 2

    # Calculate the total cost of the backpack and three ring-binders
    total_cost = new_backpack_price + (3 * new_ringbinder_price)
    
    result = total_cost
    return result

print(solution())