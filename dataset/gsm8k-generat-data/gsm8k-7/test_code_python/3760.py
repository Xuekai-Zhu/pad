def solution():
    clementine_cookies = 72
    jake_cookies = clementine_cookies * 2
    tory_cookies = (clementine_cookies + jake_cookies) / 2
    total_cookies = clementine_cookies + jake_cookies + tory_cookies
    price_per_cookie = 2
    total_money = total_cookies * price_per_cookie
    result = total_money
    return result

print(solution())