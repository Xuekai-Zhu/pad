def solution():
    item_cost = 200
    num_items = 7
    total_cost = item_cost * num_items

    # Check if total cost is over $1000
    if total_cost > 1000:
        discount_amount = (total_cost - 1000) * 0.1
        total_cost -= discount_amount

    result = total_cost
    return result

print(solution())