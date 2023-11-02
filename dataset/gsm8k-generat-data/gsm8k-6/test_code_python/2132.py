def solution():
    # Calculate the total revenue from selling cupcakes and cookies
    revenue_cupcakes = 50 * 2
    revenue_cookies = 40 * 0.5
    total_revenue = revenue_cupcakes + revenue_cookies

    # Calculate the total cost of two basketballs
    basketball_cost = 2 * 40

    # Calculate the remaining amount of money after buying the basketballs
    remaining_money = total_revenue - basketball_cost

    # Calculate the cost of one bottle of energy drink
    cost_per_bottle = remaining_money / 20
    result = cost_per_bottle
    return result

print(solution())