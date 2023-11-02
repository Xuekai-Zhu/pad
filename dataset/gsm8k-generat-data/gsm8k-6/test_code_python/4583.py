def solution():
    # Calculate the cost of pizza for the children and the toppings
    cost_children = (10 + 2 * 1) * 2  # 2 pizzas for the children with 2 toppings each

    # Calculate the cost of pizza for Ruby and her husband and the toppings
    cost_adults = (10 + 2 * 2) + (1 * 2) # 1 pizza for Ruby and her husband with 4 toppings total

    # Add the costs together and include the tip
    total_cost = cost_children + cost_adults + 5
    result = total_cost
    return result

print(solution())