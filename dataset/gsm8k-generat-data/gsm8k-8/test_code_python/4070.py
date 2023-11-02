def solution():
    # Calculate the total cost of ingredients per week
    ingredient_cost = 10 * 7

    # Calculate the total revenue from selling French fries and Poutine
    french_fries_revenue = 12 * 7
    poutine_revenue = 8 * 7
    total_revenue = french_fries_revenue + poutine_revenue

    # Calculate the tax amount
    tax = total_revenue * 0.1

    # Calculate the net income after taxes and ingredient costs
    net_income = total_revenue - tax - ingredient_cost
    result = net_income
    return result

print(solution())