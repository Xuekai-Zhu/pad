def solution():
    """John makes 6 dozen cookies for a bake sale. He sells each cookie for $1.5 and each cookie costs $0.25 to make. He splits the profit between two charities evenly. How much does each charity get?"""
    cookies_per_dozen = 12
    dozens_of_cookies = 6
    cost_per_cookie = 0.25
    price_per_cookie = 1.5
    total_cost = dozens_of_cookies * cookies_per_dozen * cost_per_cookie
    total_income = dozens_of_cookies * cookies_per_dozen * price_per_cookie
    profit = total_income - total_cost
    charity_profit = profit / 2
    result = charity_profit
    return result

print(solution())