def solution():
    item_cost = 200  # Each item costs $200
    num_items = 7  # John buys 7 items
    total_cost = item_cost * num_items  # Calculate the total cost before discount

    if total_cost > 1000:
        # Calculate the amount of the sale that exceeds $1000
        discount_amount = (total_cost - 1000) * 0.1

        # Apply the discount to the total cost
        total_cost -= discount_amount

    result = total_cost
    return result

print(solution())