def solution():
    item_cost = 200
    num_items = 7
    total_cost = item_cost * num_items

    # Calculate the amount of the sell that was over $1000
    over_1000 = total_cost - 1000

    # Calculate the discount for the amount over $1000
    discount = 0.1 * over_1000

    # Calculate the total cost after the discount
    final_cost = total_cost - discount
    result = final_cost
    return result

print(solution())