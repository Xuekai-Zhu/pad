def solution():
    cost_per_bracelet = 1 + 3  # $1 for string and $3 for beads
    selling_price_per_bracelet = 6
    number_of_bracelets = 25

    # Calculate the total cost and total revenue
    total_cost = cost_per_bracelet * number_of_bracelets
    total_revenue = selling_price_per_bracelet * number_of_bracelets

    # Calculate the profit
    profit = total_revenue - total_cost
    result = profit
    return result

print(solution())