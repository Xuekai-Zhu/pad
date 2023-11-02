def solution():
    """Julieta went to the store to buy a backpack and three ring-binders for her school supplies. She knew the backpack was $50, and each ring-binder cost was $20. However, at the store, she found out that the price of a back had increased by $5, and the price of a ring-binder had reduced by $2. Calculate the total amount of money Julieta spent at the store."""
    backpack_price = 50 + 5
    ringbinder_price = 20 - 2
    total_price = backpack_price + (3 * ringbinder_price)
    result = total_price
    return result

print(solution())