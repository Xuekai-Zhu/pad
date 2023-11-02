def solution():
    sweaters = 28  # Chantal is selling 28 sweaters
    yarn_per_sweater = 4  # Each sweater takes 4 balls of yarn
    cost_per_yarn = 6  # Each ball of yarn costs $6
    price_per_sweater = 35  # Chantal sells each sweater for $35

    # Calculate the total cost of yarn for all sweaters
    total_yarn_cost = sweaters * yarn_per_sweater * cost_per_yarn

    # Calculate the total revenue from selling all sweaters
    total_revenue = sweaters * price_per_sweater

    # Calculate the profit from selling all sweaters
    profit = total_revenue - total_yarn_cost
    result = profit
    return result

print(solution())