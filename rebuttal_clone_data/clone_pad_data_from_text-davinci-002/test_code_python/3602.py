def solution():
    oldest_son_cookies = 4
    youngest_son_cookies = 2
    total_cookies = 54
    cookies_ eaten_per_day = oldest_son_cookies + youngest_son_cookies
    days_until_finished = total_cookies / cookies_eaten_per_day
    result = days_until_finished
    
    return result

print(solution())