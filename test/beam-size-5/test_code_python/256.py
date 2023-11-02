def solution():
    
    flour_per_dozen = 2
    cookies_today = 36
    cookies_tomorrow = 30
    total_cookies = cookies_today + cookies_tomorrow
    total_flour = flour_per_dozen * total_cookies
    result = total_flour
    return result

print(solution())