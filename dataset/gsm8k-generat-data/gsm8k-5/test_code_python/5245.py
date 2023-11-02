def solution():
    cookies_made = 6 * 12  # John makes 6 dozen cookies, which is 6*12 = 72 cookies
    cost_per_cookie = 0.25  # The cost of making each cookie is $0.25
    price_per_cookie = 1.5  # John sells each cookie for $1.5
    total_cost = cookies_made * cost_per_cookie  # The total cost of making 72 cookies is $18
    total_revenue = cookies_made * price_per_cookie  # The total revenue from selling 72 cookies is $108
    total_profit = total_revenue - total_cost  # The total profit is $90
    charity_share = total_profit / 2  # Half of the profit goes to each charity
    result = charity_share
    return result

print(solution())