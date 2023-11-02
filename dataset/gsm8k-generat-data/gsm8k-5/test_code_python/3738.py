def solution():
    backpack_price = 50 + 5  # The price of the backpack increased by $5
    ringbinder_price = 20 - 2  # The price of a ring-binder decreased by $2
    num_ringbinders = 3  # Julieta bought 3 ring-binders

    # Calculate the total cost of the backpack and the ring-binders
    total_cost = backpack_price + ringbinder_price * num_ringbinders
    result = total_cost
    return result

print(solution())