def solution():
    """John makes 6 dozen cookies for a bake sale. He sells each cookie for $1.5 and each cookie costs $0.25 to make.
    He splits the profit between two charities evenly. How much does each charity get?"""
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