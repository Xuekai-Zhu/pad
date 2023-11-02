def solution():
    
    cookies_sold_morning = 3 * 12
    cookies_sold_lunch = 57
    cookies_sold_afternoon = 16
    total_cookies_sold = cookies_sold_morning + cookies_sold_lunch + cookies_sold_afternoon
    cookies_left = 120 - total_cookies_sold
    result = cookies_left
    return result

print(solution())