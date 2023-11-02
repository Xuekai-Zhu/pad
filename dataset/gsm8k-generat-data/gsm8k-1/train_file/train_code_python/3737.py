def solution():
    """Julieta went to the store to buy a backpack and three ring-binders for her school supplies. 
    She knew the backpack was $50, and each ring-binder cost was $20. However, at the store, 
    she found out that the price of a back had increased by $5, and the price of a ring-binder had reduced by $2.
    Calculate the total amount of money Julieta spent at the store."""
    backpack_price = 55
    ringbinder_price = 18
    num_ringbinders = 3
    total_cost = (backpack_price + num_ringbinders * ringbinder_price)
    result = total_cost
    return result

print(solution())