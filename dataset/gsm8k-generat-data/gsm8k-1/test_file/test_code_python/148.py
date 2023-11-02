def solution():
    """Carl buys ten packs of cookies. Each pack of cookies has six cookies inside. Each cookie cost $0.10. How much change does Carl receive if he pay with a $10 bill?"""
    packs_of_cookies = 10
    cookies_per_pack = 6
    price_per_cookie = 0.1
    total_price = packs_of_cookies * cookies_per_pack * price_per_cookie
    change = 10 - total_price
    result = change
    return result

print(solution())