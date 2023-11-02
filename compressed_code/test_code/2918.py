def solution():
    
    clementine_cookies = 72
    jake_cookies = 2 * clementine_cookies
    tory_cookies = (clementine_cookies + jake_cookies) / 2
    total_cookies = clementine_cookies + jake_cookies + tory_cookies
    sale_price = 2
    total_money = total_cookies * sale_price
    result = total_money
    return result

print(solution())