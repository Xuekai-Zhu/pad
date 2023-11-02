def solution():
    
    cookies_per_dozen = 12
    total_cookies = 6 * cookies_per_dozen
    cost_per_cookie = 0.25
    price_per_cookie = 1.5
    profit_per_cookie = price_per_cookie - cost_per_cookie
    total_profit = profit_per_cookie * total_cookies
    charity_share = total_profit / 2
    result = charity_share
    return result

print(solution())