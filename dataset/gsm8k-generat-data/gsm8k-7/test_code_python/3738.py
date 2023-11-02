def solution():
    original_backpack_price = 50
    backpack_price_increase = 5
    ringbinder_original_price = 20
    ringbinder_price_decrease = 2
    num_ringbinders = 3

    # Calculate the new price of the backpack
    new_backpack_price = original_backpack_price + backpack_price_increase

    # Calculate the new price of each ring-binder
    new_ringbinder_price = ringbinder_original_price - ringbinder_price_decrease

    # Calculate the total cost of the backpack and ring-binders
    total_cost = new_backpack_price + (num_ringbinders * new_ringbinder_price)
    result = total_cost
    return result

print(solution())