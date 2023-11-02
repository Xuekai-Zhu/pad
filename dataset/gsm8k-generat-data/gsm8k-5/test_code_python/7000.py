def solution():
    cost_price = 0.8 # Jen buys candy bars at 80 cents each
    selling_price = 1 # Jen sells candy bars at $1 each
    num_bought = 50 # Jen buys 50 candy bars
    num_sold = 48 # Jen sells 48 candy bars

    # Calculate total cost and total selling price
    total_cost = cost_price * num_bought
    total_selling_price = selling_price * num_sold

    # Calculate profit in cents
    profit_in_cents = (total_selling_price - total_cost) * 100
    result = profit_in_cents
    return result

print(solution())