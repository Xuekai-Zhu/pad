def solution():
    total_money = 260
    num_shirts = 2
    shirt_price = 18.5
    trouser_price = 63
    num_additional_items = 4

    # Calculate the total cost of Sophie's initial purchases
    total_initial_cost = (num_shirts * shirt_price) + trouser_price

    # Calculate the remaining budget after the initial purchases
    remaining_budget = total_money - total_initial_cost

    # Calculate the total cost of the 4 additional items
    total_additional_cost = remaining_budget / num_additional_items

    # Calculate the cost per item by splitting the total cost evenly among the 4 items
    cost_per_item = total_additional_cost / 4
    result = cost_per_item
    return result

print(solution())