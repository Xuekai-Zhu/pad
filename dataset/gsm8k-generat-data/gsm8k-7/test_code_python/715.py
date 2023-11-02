def solution():
    num_bracelets = 25
    string_cost_per_bracelet = 1
    bead_cost_per_bracelet = 3
    selling_price_per_bracelet = 6

    # Calculate the total cost of making all the bracelets
    total_cost = (string_cost_per_bracelet + bead_cost_per_bracelet) * num_bracelets

    # Calculate the total revenue from selling all the bracelets
    total_revenue = selling_price_per_bracelet * num_bracelets

    # Calculate the profit
    profit = total_revenue - total_cost
    result = profit
    return result

print(solution())