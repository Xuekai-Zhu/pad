def solution():
    """A store gives a 10% discount for the amount of the sell that was over $1000. John buys 7 items that each cost $200. What does his order cost after the discount?"""
    item_cost = 200
    num_items = 7
    total_cost = item_cost * num_items
    discount_threshold = 1000
    if total_cost > discount_threshold:
        discount_amount = 0.1 * (total_cost - discount_threshold)
        total_cost -= discount_amount

    result = total_cost
    return result

print(solution())