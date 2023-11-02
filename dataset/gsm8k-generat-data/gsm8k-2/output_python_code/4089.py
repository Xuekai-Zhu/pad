def solution():
    """How much money did you make if you sold 220 chocolate cookies at $1 per cookie and 70 vanilla cookies at $2 per cookie?"""
    chocolate_cookies_sold = 220
    vanilla_cookies_sold = 70
    chocolate_cookie_price = 1
    vanilla_cookie_price = 2
    total_income = (chocolate_cookies_sold * chocolate_cookie_price) + (vanilla_cookies_sold * vanilla_cookie_price)
    result = total_income
    return result

print(solution())