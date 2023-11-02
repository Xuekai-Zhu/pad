def solution():
    total_cookies = 60
    cookies_with_nuts = total_cookies * (1/4)
    cookies_with_chocolate = total_cookies * (40/100)
    cookies_with_both = total_cookies - (cookies_with_nuts + cookies_with_chocolate)
    total_nuts = (cookies_with_nuts * 2) + (cookies_with_both * 2)
    result = total_nuts
    return result

print(solution())