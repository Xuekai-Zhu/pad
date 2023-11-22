def solution():
    
    cookies_per_dozen = 12
    cookies_today = 36
    cookies_tomorrow = 30
    total_cookies = cookies_today + cookies_tomorrow
    flour_per_dozen = 2
    total_flour = total_cookies * flour_per_dozen
    result = total_flour
    return result

print(solution())