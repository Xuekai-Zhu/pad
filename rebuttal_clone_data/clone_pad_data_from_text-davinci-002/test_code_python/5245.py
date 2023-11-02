def solution():
    cookies_made = 6 * 12
    cookie_price = 1.5
    cookie_cost = 0.25
    profit = cookies_made * (cookie_price - cookie_cost)
    charity_share = profit / 2
    result = charity_share
    return result

print(solution())