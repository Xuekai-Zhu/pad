def solution():
    ingredients_cost_per_pan = 10.00  # Jenny spends $10 on ingredients per pan
    price_per_pan = 25.00  # Jenny sells each pan for $25
    pans_made = 20  # Jenny makes and sells 20 pans

    # Calculate the total revenue from selling lasagna
    total_revenue = price_per_pan * pans_made

    # Calculate the total expenses on ingredients
    total_expenses = ingredients_cost_per_pan * pans_made

    # Calculate Jenny's profit
    profit = total_revenue - total_expenses
    result = profit
    return result

print(solution())