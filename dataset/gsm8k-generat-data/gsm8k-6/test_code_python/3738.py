def solution():
    # Calculate the new prices
    backpack_price = 50 + 5  # the price of the backpack increased by $5
    ringbinder_price = 20 - 2  # the price of a ring-binder reduced by $2

    # Calculate the total cost of the backpack and three ring-binders
    total_cost = backpack_price + (3 * ringbinder_price)

    result = total_cost
    return result

print(solution())