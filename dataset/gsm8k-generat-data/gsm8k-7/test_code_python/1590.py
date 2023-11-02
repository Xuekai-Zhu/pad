def solution():
    old_price = 2
    new_price = old_price * 1.5  # 50% increase
    old_quantity = 4
    new_quantity = old_quantity / 2  # half the quantity

    # Calculate the old total cost
    old_total_cost = old_price * old_quantity

    # Calculate the new total cost
    new_total_cost = new_price * new_quantity

    # Calculate the savings
    savings = old_total_cost - new_total_cost
    result = savings
    return result

print(solution())