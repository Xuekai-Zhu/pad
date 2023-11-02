def solution():
    cookies_baked = 60
    cookies_eaten = 2
    mom_cookies = 1
    brownies_baked = 32
    brownies_eaten = 2
    mom_brownies = 2
    price_cookie = 1
    price_brownie = 1.5
    cookies_sold = cookies_baked - cookies_eaten - mom_cookies
    brownies_sold = brownies_baked - brownies_eaten - mom_brownies
    total_cookies = cookies_sold * price_cookie
    total_brownies = brownies_sold * price_brownie
    total_profit = total_cookies + total_brownies
    result = total_profit
    
    return result

print(solution())