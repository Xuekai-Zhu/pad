def solution():
    
    trays_per_day = 2
    days = 6
    cookies_per_tray = 12
    total_cookies = trays_per_day * cookies_per_tray * days
    frank_cookies = days  
    ted_cookies = 4
    cookies_left = total_cookies - frank_cookies - ted_cookies
    result = cookies_left
    return result

print(solution())